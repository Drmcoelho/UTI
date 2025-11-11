"""Ferramentas para o simulador do módulo 06 (monitorização da PIC)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class EstadoPIC:
    """Representa parâmetros principais da monitorização da PIC."""

    pam: float
    pic: float
    pbt_o2: float | None = None
    sodio: float | None = None

    @property
    def ppc(self) -> float:
        """Calcula pressão de perfusão cerebral (PPC)."""

        return self.pam - self.pic


def calcular_ppc(pam: float, pic: float) -> float:
    """Calcula PPC garantindo valores válidos."""

    if pam <= 0 or pic < 0:
        raise ValueError("PAM deve ser positiva e PIC não pode ser negativa")
    return pam - pic


def classificar_crise_pic(estado: EstadoPIC) -> str:
    """Classifica gravidade da PIC e sugere condutas."""

    ppc = estado.ppc
    mensagens: list[str] = []
    if estado.pic >= 25:
        mensagens.append("PIC crítica — considerar terapia de resgate")
    elif estado.pic >= 20:
        mensagens.append("PIC limítrofe — reforçar medidas básicas")
    else:
        mensagens.append("PIC controlada")

    if ppc < 60:
        mensagens.append("PPC baixa — elevar PAM alvo")
    else:
        mensagens.append("PPC dentro da meta")

    if estado.pbt_o2 is not None and estado.pbt_o2 < 20:
        mensagens.append("PbtO₂ <20 mmHg — otimizar oxigenação/perfusão")

    if estado.sodio is not None and estado.sodio > 155:
        mensagens.append("Hipernatremia — reavaliar osmoterapia")

    return " | ".join(mensagens)


def volume_drenagem_recomendado(picos_pic: Iterable[float]) -> float:
    """Sugere volume de drenagem de LCR baseado nos últimos picos de PIC."""

    picos = list(picos_pic)
    if not picos:
        raise ValueError("Forneça ao menos um valor de PIC")
    if any(p < 0 for p in picos):
        raise ValueError("Valores de PIC não podem ser negativos")
    media = sum(picos) / len(picos)
    pico_maximo = max(picos)
    if pico_maximo >= 30 or media >= 30:
        return 10.0
    if pico_maximo >= 27 or media >= 25:
        return 7.5
    if pico_maximo >= 22 or media >= 20:
        return 5.0
    return 0.0


def avaliar_bundle_basico(cabeca_30: bool, sedacao_profunda: bool, ventilacao_adequada: bool) -> str:
    """Avalia se o bundle básico está completo antes de escalar terapia."""

    faltantes: list[str] = []
    if not cabeca_30:
        faltantes.append("cabeceira 30°")
    if not sedacao_profunda:
        faltantes.append("sedação/analgesia adequada")
    if not ventilacao_adequada:
        faltantes.append("ventilação alvo PaCO₂ 35-40 mmHg")
    if not faltantes:
        return "Bundle básico completo"
    return "Ajustar " + ", ".join(faltantes)


__all__ = [
    "EstadoPIC",
    "calcular_ppc",
    "classificar_crise_pic",
    "volume_drenagem_recomendado",
    "avaliar_bundle_basico",
]
