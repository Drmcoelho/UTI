"""Simulador para ajuste de bloqueio neuromuscular."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class AvaliacaoTOF:
    respostas_tof: int
    contagem_postetanica: int | None

    def classificar(self) -> str:
        if not 0 <= self.respostas_tof <= 4:
            raise ValueError("TOF deve estar entre 0 e 4")
        if self.respostas_tof == 0:
            if self.contagem_postetanica is None:
                return "Bloqueio profundo — medir contagem postetânica"
            if self.contagem_postetanica <= 1:
                return "Bloqueio muito profundo — reduzir infusão"
            if self.contagem_postetanica <= 3:
                return "Bloqueio adequado"
            return "Recuperação em curso — considerar redução adicional"
        if 1 <= self.respostas_tof <= 2:
            return "Bloqueio dentro da meta"
        if self.respostas_tof == 3:
            return "Bloqueio superficial — avaliar aumento"
        return "Sem bloqueio — considerar suspensão do fármaco"


def dose_cisatracurio(peso_kg: float, alvo: str = "manutencao") -> float:
    """Estima dose em mcg/kg/min de cisatracúrio."""

    if peso_kg <= 0:
        raise ValueError("Peso inválido")
    if alvo == "inducao":
        return 0.2
    if alvo == "manutencao":
        return 3.0
    if alvo == "desmame":
        return 1.0
    raise ValueError("Alvo desconhecido")


def resumo_bundle(status: Sequence[bool]) -> str:
    """Gera resumo textual da adesão ao bundle de bloqueio."""

    if not status:
        raise ValueError("Forneça dados de bundle")
    adesao = (sum(status) / len(status)) * 100
    if adesao >= 80:
        return f"Adesão alta ({adesao:.0f}%) — manter estratégia"
    if adesao >= 60:
        return f"Adesão moderada ({adesao:.0f}%) — reforçar educação"
    return f"Adesão baixa ({adesao:.0f}%) — revisar processos"


def calcular_ppc(pam: float, pic: float) -> float:
    """Calcula pressão de perfusão cerebral para integrar a avaliação."""

    if pam <= 0 or pic < 0:
        raise ValueError("Valores inválidos")
    return pam - pic


__all__ = [
    "AvaliacaoTOF",
    "dose_cisatracurio",
    "resumo_bundle",
    "calcular_ppc",
]
