"""Ferramentas para o simulador do módulo 01 (monitorização invasiva)."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESOURCE_PATH = PROJECT_ROOT / "recursos" / "01_monitorizacao_invasiva" / "curvas_referencia.csv"


@dataclass(frozen=True)
class CurvaReferencia:
    """Representa um cenário de curva arterial para apoio à decisão."""

    fase: str
    descricao: str
    pam_alvo_mmHg: float
    observacao: str


def calcular_pam(pas: float, pad: float) -> float:
    """Calcula a pressão arterial média (PAM)."""
    if pas <= 0 or pad <= 0:
        raise ValueError("Pressões devem ser positivas")
    if pas <= pad:
        raise ValueError("PAS deve ser maior que PAD")
    return pad + (pas - pad) / 3


def carregar_curvas() -> list[CurvaReferencia]:
    """Lê as curvas de referência do arquivo de recursos."""
    curvas: list[CurvaReferencia] = []
    with RESOURCE_PATH.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            curvas.append(
                CurvaReferencia(
                    fase=row["fase"],
                    descricao=row["descricao"],
                    pam_alvo_mmHg=float(row["pam_alvo_mmHg"]),
                    observacao=row["observacao"],
                )
            )
    return curvas


def classificar_pam(pam_atual: float) -> CurvaReferencia:
    """Retorna o cenário de curva recomendado com base na PAM atual."""
    curvas = sorted(carregar_curvas(), key=lambda c: c.pam_alvo_mmHg)
    for curva in curvas:
        if pam_atual <= curva.pam_alvo_mmHg:
            return curva
    return curvas[-1]


def avaliar_ppv(ppv: float, ventilacao_controlada: bool = True) -> str:
    """Avalia a responsividade a fluidos a partir da variação de pressão de pulso."""
    if ppv < 0 or ppv > 100:
        raise ValueError("PPV deve estar entre 0 e 100%")
    if not ventilacao_controlada:
        return "PPV pouco confiável — considere outras métricas dinâmicas."
    if ppv >= 13:
        return "Provável responsividade a fluidos (considere teste dinâmico)."
    if ppv >= 9:
        return "Zona cinzenta — avalie ecocardiografia ou variações respiratórias."
    return "Provável não responsivo — ajuste drogas vasoativas."


def estimar_ajuste_vasopressor(pam_atual: float, pam_alvo: float = 65.0, sensibilidade: float = 0.1) -> float:
    """Sugere ajuste proporcional na dose de vasopressor.

    Retorna o fator multiplicador a ser aplicado na dose atual.
    """
    if pam_alvo <= 0 or pam_atual <= 0:
        raise ValueError("PAMs devem ser positivas")
    erro_relativo = (pam_alvo - pam_atual) / pam_alvo
    return 1 + erro_relativo * sensibilidade


__all__ = [
    "CurvaReferencia",
    "calcular_pam",
    "carregar_curvas",
    "classificar_pam",
    "avaliar_ppv",
    "estimar_ajuste_vasopressor",
]
