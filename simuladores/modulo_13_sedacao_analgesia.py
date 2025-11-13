"""Ferramentas de apoio para ajustes de sedação e analgesia."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class PlanoSedacao:
    rass_meta_min: int
    rass_meta_max: int
    cpots_maximo: int = 3

    def avaliar_rass(self, rass_atual: int) -> str:
        if rass_atual < -5 or rass_atual > 4:
            raise ValueError("RASS inválido")
        if rass_atual < self.rass_meta_min:
            return "Sedação profunda — considerar redução"
        if rass_atual > self.rass_meta_max:
            return "Sedação insuficiente — ajustar sedativos"
        return "Dentro da meta"

    def avaliar_cpot(self, cpot_atual: int) -> str:
        if cpot_atual < 0:
            raise ValueError("CPOT inválido")
        if cpot_atual > self.cpots_maximo:
            return "Dor mal controlada — intensificar analgesia multimodal"
        return "Analgesia adequada"


def risco_hipertrigliceridemia(triglicerideos: float) -> str:
    """Classifica risco associado ao uso de propofol."""

    if triglicerideos < 0:
        raise ValueError("Triglicerídeos inválidos")
    if triglicerideos >= 1000:
        return "Risco crítico — Suspender propofol imediatamente"
    if triglicerideos >= 400:
        return "Risco elevado — Reduzir taxa e considerar troca por dexmedetomidina/quetamina"
    return "Risco baixo — manter monitorização"


def dose_dexmedetomidina(peso: float, alvo: str = "sedacao_leve") -> tuple[float, float]:
    """Retorna faixa de dose (mcg/kg/h) conforme objetivo."""

    if peso <= 0:
        raise ValueError("Peso deve ser positivo")
    if alvo == "sedacao_leve":
        return (0.2, 0.7)
    if alvo == "delirium":
        return (0.3, 1.0)
    if alvo == "desmame_sedativo":
        return (0.1, 0.4)
    raise ValueError("Alvo desconhecido")


def adesao_bundle(status: Sequence[bool]) -> float:
    """Calcula adesão percentual ao bundle ABCDEF."""

    if not status:
        raise ValueError("É necessário informar itens do bundle")
    return (sum(status) / len(status)) * 100


__all__ = [
    "PlanoSedacao",
    "risco_hipertrigliceridemia",
    "dose_dexmedetomidina",
    "adesao_bundle",
]
