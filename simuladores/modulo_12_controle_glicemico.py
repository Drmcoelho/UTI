"""Ferramentas para simular protocolos de controle glicêmico em UTI."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class MedicaoGlicemica:
    glicemia_atual: float
    glicemia_anterior: float
    intervalo_horas: float

    @property
    def variacao_por_hora(self) -> float:
        if self.intervalo_horas <= 0:
            raise ValueError("Intervalo deve ser positivo")
        return (self.glicemia_atual - self.glicemia_anterior) / self.intervalo_horas


def sugerir_ajuste_taxa(variacao_hora: float, taxa_atual: float) -> float:
    """Sugere nova taxa de insulina conforme taxa de variação."""

    if taxa_atual < 0:
        raise ValueError("Taxa atual deve ser não negativa")
    if variacao_hora > 60:
        return taxa_atual + 2
    if variacao_hora > 30:
        return taxa_atual + 1
    if variacao_hora < -40:
        return max(taxa_atual - 2, 0)
    if variacao_hora < -20:
        return max(taxa_atual - 1, 0)
    return taxa_atual


def avaliar_pausa_dieta(minutos_pausa: float, taxa_atual: float) -> float:
    """Calcula taxa ajustada diante de pausa de dieta enteral."""

    if minutos_pausa < 0:
        raise ValueError("Minutos não pode ser negativo")
    if taxa_atual < 0:
        raise ValueError("Taxa atual deve ser não negativa")
    if minutos_pausa == 0:
        return taxa_atual
    if minutos_pausa <= 120:
        return taxa_atual * 0.5
    return 0.0


def tempo_na_meta(medicoes: Sequence[float], limite_inferior: float, limite_superior: float) -> float:
    """Calcula percentual de medições dentro da meta."""

    if limite_inferior >= limite_superior:
        raise ValueError("Limites inválidos")
    if not medicoes:
        raise ValueError("Necessário fornecer ao menos uma medição")
    dentro = sum(limite_inferior <= valor <= limite_superior for valor in medicoes)
    return (dentro / len(medicoes)) * 100


def risco_hipoglicemia(glicemia: float, sintomas: bool, insuficiencia_renal: bool) -> str:
    """Classifica risco de hipoglicemia grave."""

    if glicemia < 40:
        return "Alto risco — iniciar protocolo de resgate imediato"
    if glicemia < 70 or sintomas:
        return "Moderado — reduzir infusão e administrar carboidrato"
    if insuficiencia_renal:
        return "Baixo, porém requer monitorização intensificada"
    return "Baixo risco"


__all__ = [
    "MedicaoGlicemica",
    "sugerir_ajuste_taxa",
    "avaliar_pausa_dieta",
    "tempo_na_meta",
    "risco_hipoglicemia",
]
