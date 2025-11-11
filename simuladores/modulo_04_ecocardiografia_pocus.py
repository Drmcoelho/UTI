"""Ferramentas para o simulador do módulo 04 (ecocardiografia à beira do leito)."""
from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESOURCE_PATH = PROJECT_ROOT / "recursos" / "04_ecocardiografia_pocus" / "medidas_referencia.csv"


@dataclass(frozen=True)
class ReferenciaMedida:
    variavel: str
    faixa_normal: tuple[float | None, float | None]
    alerta_baixo: float | None
    alerta_alto: float | None
    observacao: str


def carregar_referencias() -> dict[str, ReferenciaMedida]:
    """Lê faixas de referência utilizadas no simulador."""

    referencias: dict[str, ReferenciaMedida] = {}
    with RESOURCE_PATH.open(encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            minimo, maximo = row["faixa_normal"].split("-")
            referencias[row["variavel"]] = ReferenciaMedida(
                variavel=row["variavel"],
                faixa_normal=(float(minimo) if minimo else None, float(maximo) if maximo else None),
                alerta_baixo=float(row["alerta_baixo"]) if row["alerta_baixo"] else None,
                alerta_alto=float(row["alerta_alto"]) if row["alerta_alto"] else None,
                observacao=row["observacao"],
            )
    return referencias


def calcular_volume_sistolico_lvot(diametro_cm: float, vti_cm: float) -> float:
    """Calcula volume sistólico (mL) a partir do diâmetro do TSV e VTI."""

    if diametro_cm <= 0 or vti_cm <= 0:
        raise ValueError("Diâmetro e VTI devem ser positivos")
    raio = diametro_cm / 2
    area_cm2 = math.pi * raio**2
    volume_ml = area_cm2 * vti_cm
    return volume_ml


def calcular_debito_cardiaco(diametro_cm: float, vti_cm: float, frequencia_cardiaca: float) -> float:
    """Retorna débito cardíaco em L/min com base na fórmula padrão."""

    if frequencia_cardiaca <= 0:
        raise ValueError("Frequência cardíaca deve ser positiva")
    volume_sistolico = calcular_volume_sistolico_lvot(diametro_cm, vti_cm)
    debito_ml_min = volume_sistolico * frequencia_cardiaca
    return debito_ml_min / 1000


def classificar_estado_volumico(
    vti_cm: float,
    ivc_diametro_cm: float,
    ivc_colapso_pct: float,
    *,
    ventilacao_controlada: bool,
) -> str:
    """Classifica estado volêmico combinando VTI e métricas da IVC."""

    if vti_cm <= 0 or ivc_diametro_cm <= 0:
        raise ValueError("Valores de VTI e diâmetro da IVC devem ser positivos")
    if not 0 <= ivc_colapso_pct <= 100:
        raise ValueError("Colapso da IVC deve estar entre 0 e 100%")

    mensagens: list[str] = []
    if vti_cm < 18:
        mensagens.append("VTI baixo sugere baixo volume sistólico")
    elif vti_cm > 22:
        mensagens.append("VTI alto sugere hiperdinamismo ou pós-carga baixa")
    else:
        mensagens.append("VTI dentro da faixa esperada")

    if ventilacao_controlada:
        if ivc_colapso_pct < 12 and ivc_diametro_cm > 2.1:
            mensagens.append("IVC tensa com colapso < 12% — provável sobrecarga")
        elif ivc_colapso_pct > 18:
            mensagens.append("Colapso aumentado em ventilação controlada — investigar hipovolemia")
        else:
            mensagens.append("IVC compatível com enchimento adequado")
    else:
        if ivc_colapso_pct > 50:
            mensagens.append("Colapso > 50% em ventilação espontânea — hipovolemia provável")
        elif ivc_diametro_cm > 2.1 and ivc_colapso_pct < 30:
            mensagens.append("IVC dilatada sem colapso — sugerindo alta pressão de enchimento")
        else:
            mensagens.append("IVC sem achados críticos em ventilação espontânea")

    return " | ".join(mensagens)


def avaliar_tapse(tapse_mm: float) -> str:
    """Retorna classificação qualitativa do TAPSE."""

    if tapse_mm <= 0:
        raise ValueError("TAPSE deve ser positivo")
    if tapse_mm < 17:
        return "Disfunção sistólica de VD"
    if tapse_mm > 24:
        return "Hiperdinamismo de VD (investigar etiologias)"
    return "Função de VD preservada"


def estimar_pressao_capilar_pulmonar(e_e_prime: float, e_a: float | None = None) -> float:
    """Estima pressão de enchimento do VE usando relação E/e'."""

    if e_e_prime <= 0:
        raise ValueError("E/e' deve ser positivo")
    pressao = 1.24 * e_e_prime + 1.9
    if e_a:
        pressao += 0.5 * max(0, e_a - 1.0)
    return pressao


__all__ = [
    "ReferenciaMedida",
    "carregar_referencias",
    "calcular_volume_sistolico_lvot",
    "calcular_debito_cardiaco",
    "classificar_estado_volumico",
    "avaliar_tapse",
    "estimar_pressao_capilar_pulmonar",
]
