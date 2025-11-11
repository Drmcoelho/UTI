"""Ferramentas para o simulador do módulo 05 (oximetria e capnografia)."""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ALARMES_PATH = PROJECT_ROOT / "recursos" / "05_oximetria_capnografia" / "alarmes_padrao.csv"


@dataclass(frozen=True)
class AlarmePadrao:
    parametro: str
    limite_inferior: float | None
    limite_superior: float | None
    recomendacao: str


def carregar_alarmes() -> dict[str, AlarmePadrao]:
    """Carrega limites de alarme sugeridos para o módulo."""

    alarmes: dict[str, AlarmePadrao] = {}
    with ALARMES_PATH.open(encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            alarmes[row["parametro"]] = AlarmePadrao(
                parametro=row["parametro"],
                limite_inferior=float(row["limite_inferior"]) if row["limite_inferior"] else None,
                limite_superior=float(row["limite_superior"]) if row["limite_superior"] else None,
                recomendacao=row["recomendacao"],
            )
    return alarmes


def avaliar_oximetria(spo2: float, indice_perfusao: float) -> str:
    """Interpreta SpO₂ e índice de perfusão para orientar condutas."""

    if not 0 <= spo2 <= 100:
        raise ValueError("SpO₂ deve estar entre 0 e 100%")
    if indice_perfusao < 0:
        raise ValueError("Índice de perfusão deve ser não negativo")

    mensagens: list[str] = []
    if spo2 < 92:
        mensagens.append("SpO₂ abaixo do alvo padrão (92-96%)")
    elif spo2 > 98:
        mensagens.append("SpO₂ elevada — ajustar alvo para evitar hiperóxia se necessário")
    else:
        mensagens.append("SpO₂ dentro da faixa segura para a maioria dos pacientes")

    if indice_perfusao < 0.5:
        mensagens.append("PI < 0,5% — leitura pouco confiável, otimizar perfusão")
    elif indice_perfusao < 1.0:
        mensagens.append("PI baixo — correlacionar com perfusão periférica")
    else:
        mensagens.append("PI adequado para interpretação confiável")

    return " | ".join(mensagens)


def calcular_gradiente_co2(etco2: float, paco2: float) -> tuple[float, str]:
    """Retorna gradiente ETCO₂-PaCO₂ e classificação."""

    if paco2 <= 0 or etco2 < 0:
        raise ValueError("PaCO₂ deve ser positiva e ETCO₂ não pode ser negativo")
    gradiente = paco2 - etco2
    if gradiente < 0:
        status = "ETCO₂ acima da PaCO₂ — verificar calibração"
    elif gradiente <= 10:
        status = "Gradiente dentro da faixa esperada"
    else:
        status = "Gradiente elevado (>10 mmHg) — investigar aumento de espaço morto ou hipoperfusão"
    return gradiente, status


def interpretar_capnograma(
    *,
    retorno_base: bool,
    formato_plato: str,
    co2_inspiratorio: float,
) -> str:
    """Sugere diagnóstico com base na morfologia do capnograma."""

    formato = formato_plato.lower()
    if co2_inspiratorio < 0:
        raise ValueError("CO₂ inspiratório não pode ser negativo")

    if not retorno_base:
        if co2_inspiratorio > 3:
            return "Reinalação de CO₂ — revisar absorvedor ou válvulas expiratorias"
        return "Retorno incompleto à base sem CO₂ inspirado elevado — suspeitar fluxo inadequado no circuito"
    if "tubar" in formato or "dente" in formato:
        return "Padrão em dente de tubarão — broncoespasmo ou obstrução expiratória"
    if "desc" in formato or "rebaix" in formato:
        return "Platô descendente — considerar ventilação unipulmonar ou pressão intratorácica elevada"
    return "Capnograma com morfologia dentro da normalidade"


def avaliar_tendencia_etco2(valores: Iterable[float]) -> str:
    """Analisa tendência de ETCO₂ para RCP ou sedação."""

    valores = list(valores)
    if len(valores) < 3:
        raise ValueError("Forneça pelo menos 3 valores para análise de tendência")
    if any(v < 0 for v in valores):
        raise ValueError("ETCO₂ não pode ser negativo")

    media_inicial = mean(valores[: len(valores) // 2])
    media_final = mean(valores[len(valores) // 2 :])
    if media_final - media_inicial > 5:
        return "ETCO₂ em ascensão — compressões eficazes ou aumento de perfusão"
    if media_inicial - media_final > 5:
        return "Queda progressiva de ETCO₂ — investigar fadiga de compressões ou hipoperfusão"
    return "ETCO₂ estável ao longo da observação"


__all__ = [
    "AlarmePadrao",
    "carregar_alarmes",
    "avaliar_oximetria",
    "calcular_gradiente_co2",
    "interpretar_capnograma",
    "avaliar_tendencia_etco2",
]
