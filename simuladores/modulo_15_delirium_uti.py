"""Utilidades para manejo de delirium em UTI."""
from __future__ import annotations

from typing import Sequence


def cam_icu_result(inicio_agudo: bool, inatencao: bool, pensamento_desorganizado: bool, nivel_consciencia_alterado: bool) -> bool:
    """Determina se CAM-ICU é positivo."""

    return inicio_agudo and inatencao and (pensamento_desorganizado or nivel_consciencia_alterado)


def escore_risco(pre_deliric_base: float, fatores: Sequence[float]) -> float:
    """Calcula PRE-DELIRIC ajustado somando fatores de risco ponderados."""

    if pre_deliric_base < 0:
        raise ValueError("Base inválida")
    total = pre_deliric_base + sum(fatores)
    return min(max(total, 0.0), 100.0)


def classificar_risco(escore: float) -> str:
    """Classifica risco em faixas padronizadas."""

    if escore >= 70:
        return "Muito alto"
    if escore >= 50:
        return "Alto"
    if escore >= 30:
        return "Moderado"
    return "Baixo"


def adesao_bundle_delirium(status: Sequence[bool]) -> float:
    """Calcula adesão percentual às medidas do bundle ABCDEF."""

    if not status:
        raise ValueError("Informe itens do bundle")
    return (sum(status) / len(status)) * 100


def alerta_qtc(qtc_ms: float) -> str:
    """Gera alerta para uso seguro de antipsicóticos."""

    if qtc_ms <= 0:
        raise ValueError("QTc inválido")
    if qtc_ms >= 500:
        return "QTc prolongado — evitar haloperidol, considerar alternativas"
    if qtc_ms >= 470:
        return "QTc limítrofe — Monitorizar diariamente com ECG seriado"
    return "QTc dentro da faixa segura"


__all__ = [
    "cam_icu_result",
    "escore_risco",
    "classificar_risco",
    "adesao_bundle_delirium",
    "alerta_qtc",
]
