"""Ferramentas para o simulador do módulo 09 (balanço hídrico e volemia)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class BalançoHidrico:
    peso_ideal: float
    balanco_acumulado_ml: float

    @property
    def fracao_sobrecarga(self) -> float:
        return (self.balanco_acumulado_ml / (self.peso_ideal * 1000)) * 100

    def classificar(self) -> str:
        fo = self.fracao_sobrecarga
        if fo >= 10:
            return "Sobrecarga crítica"
        if fo >= 5:
            return "Sobrecarga moderada"
        if fo <= -2:
            return "Déficit relevante"
        return "Controle adequado"


def calcular_meta_remocao(balanco_atual: float, objetivo_ml: float) -> float:
    """Calcula taxa de remoção (mL/h) para atingir objetivo em 24h."""

    restante = balanco_atual - objetivo_ml
    return max(restante / 24, 0)


def avaliar_diuretico_sequencial(resposta_diurese: Iterable[float]) -> str:
    """Analisa curva de diurese ao longo das horas após terapia sequencial."""

    dados = list(resposta_diurese)
    if len(dados) < 3:
        raise ValueError("Forneça pelo menos 3 medições")
    if any(d < 0 for d in dados):
        raise ValueError("Valores de diurese devem ser não negativos")
    if dados[-1] >= 2 * dados[0]:
        return "Resposta adequada"
    if dados[-1] >= dados[0]:
        return "Resposta parcial — manter vigilância"
    return "Sem resposta — considerar ultrafiltração"


def planejar_ultrafiltracao(hemodinamica_estavel: bool, vasopressor: bool, sobrecarga_critica: bool) -> str:
    """Sugere modalidade de ultrafiltração conforme perfil hemodinâmico."""

    if not hemodinamica_estavel or vasopressor:
        return "Ultrafiltração contínua lenta"
    if sobrecarga_critica:
        return "Pode considerar ultrafiltração intermitente controlada"
    return "Manter terapia farmacológica, reavaliar em 12h"


__all__ = [
    "BalançoHidrico",
    "calcular_meta_remocao",
    "avaliar_diuretico_sequencial",
    "planejar_ultrafiltracao",
]
