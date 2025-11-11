"""Ferramentas para o simulador do módulo 10 (nutrição enteral)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlanoNutricional:
    peso: float
    kcal_kg: float
    proteina_kg: float
    densidade_formula: float

    @property
    def calorias_totais(self) -> float:
        return self.peso * self.kcal_kg

    @property
    def proteina_total(self) -> float:
        return self.peso * self.proteina_kg

    @property
    def volume_alvo(self) -> float:
        return self.calorias_totais / self.densidade_formula


def cobertura_calorica(plano: PlanoNutricional, volume_infudido: float) -> float:
    """Calcula porcentagem de cobertura calórica alcançada."""

    if volume_infudido < 0:
        raise ValueError("Volume infundido não pode ser negativo")
    if plano.volume_alvo == 0:
        return 0.0
    return (volume_infudido / plano.volume_alvo) * 100


def avaliar_tolerancia(residuo: float, distensao: bool, diarreia: bool) -> str:
    """Classifica tolerância gastrointestinal conforme achados."""

    if residuo > 500 or distensao:
        return "Intolerância grave — considerar pós-pilórica"
    if diarreia:
        return "Intolerância moderada — ajustar fórmula/fibra"
    return "Tolerância adequada"


def ajustar_taxa_atual(volume_alvo: float, volume_infudido: float, horas_restantes: float) -> float:
    """Sugere nova taxa de infusão para atingir meta nas horas restantes."""

    if horas_restantes <= 0:
        raise ValueError("Horas restantes deve ser positivo")
    deficit = max(volume_alvo - volume_infudido, 0)
    return deficit / horas_restantes


def necessidade_suplemento_zinco(queimados: bool, zinco_serico: float) -> bool:
    """Determina necessidade de suplementação de zinco."""

    return queimados or zinco_serico < 70


__all__ = [
    "PlanoNutricional",
    "cobertura_calorica",
    "avaliar_tolerancia",
    "ajustar_taxa_atual",
    "necessidade_suplemento_zinco",
]
