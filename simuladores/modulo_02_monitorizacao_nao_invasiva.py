"""Simulador de apoio ao módulo 02 (monitorização não invasiva)."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TRENDING_PATH = PROJECT_ROOT / "recursos" / "02_monitorizacao_nao_invasiva" / "tabela_trending.csv"


@dataclass(frozen=True)
class TrendingEntry:
    hora: int
    pam_mmHg: float
    fc_bpm: float
    indice_perfusao_percent: float
    vti_cm: float
    comentarios: str


def carregar_trending() -> list[TrendingEntry]:
    """Carrega os dados de trending não invasivo."""
    entries: list[TrendingEntry] = []
    with TRENDING_PATH.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            entries.append(
                TrendingEntry(
                    hora=int(row["hora"]),
                    pam_mmHg=float(row["pam_mmHg"]),
                    fc_bpm=float(row["fc_bpm"]),
                    indice_perfusao_percent=float(row["indice_perfusao_percent"]),
                    vti_cm=float(row["vti_cm"]),
                    comentarios=row["comentarios"],
                )
            )
    return entries


def validar_serie_pam(valores: list[float], tolerancia: float = 5.0) -> bool:
    """Retorna True se a diferença máxima entre leituras estiver dentro da tolerância."""
    if not valores:
        raise ValueError("Informe ao menos um valor de PAM")
    if any(v <= 0 for v in valores):
        raise ValueError("Todos os valores devem ser positivos")
    return max(valores) - min(valores) <= tolerancia


def estimar_debito_cardiaco(area_tsv_cm2: float, vti_cm: float, fc_bpm: float) -> float:
    """Estima débito cardíaco não invasivo a partir do TSV.

    Retorna o débito em L/min.
    """
    if area_tsv_cm2 <= 0 or vti_cm <= 0 or fc_bpm <= 0:
        raise ValueError("Parâmetros devem ser positivos")
    volume_sistolico_ml = area_tsv_cm2 * vti_cm
    debito_l_min = volume_sistolico_ml * fc_bpm / 1000
    return debito_l_min


def needs_escalation(indice_perfusao: float, pam: float) -> bool:
    """Define se há necessidade de escalonar monitorização ou terapia."""
    if indice_perfusao < 0 or pam <= 0:
        raise ValueError("Valores inválidos para análise")
    return indice_perfusao < 1.4 or pam < 65


__all__ = [
    "TrendingEntry",
    "carregar_trending",
    "validar_serie_pam",
    "estimar_debito_cardiaco",
    "needs_escalation",
]
