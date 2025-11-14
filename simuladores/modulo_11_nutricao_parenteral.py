"""Ferramentas de simulação para prescrição de nutrição parenteral total."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ComposicaoNPT:
    peso_atual: float
    altura_m: float
    imc_atual: float
    imc_alvo: float
    kcal_por_kg: float
    proteina_por_kg: float
    fracao_carbo: float = 0.6
    fracao_lipidios: float = 0.2

    @property
    def peso_ajustado(self) -> float:
        """Calcula peso ajustado considerando IMC alvo."""

        if self.altura_m <= 0:
            raise ValueError("Altura deve ser positiva")
        return self.peso_atual + (self.imc_alvo - self.imc_atual) * (self.altura_m ** 2)

    @property
    def calorias_totais(self) -> float:
        return self.peso_ajustado * self.kcal_por_kg

    @property
    def proteina_total(self) -> float:
        return self.peso_ajustado * self.proteina_por_kg

    @property
    def carboidratos_totais(self) -> float:
        return self.calorias_totais * self.fracao_carbo

    @property
    def lipidios_totais(self) -> float:
        return self.calorias_totais * self.fracao_lipidios


def calcular_osmolaridade(mOsm_amino: float, mOsm_dextrose: float, mOsm_lipidios: float, outros: float = 0) -> float:
    """Soma osmolaridade prevista da mistura."""

    for valor in (mOsm_amino, mOsm_dextrose, mOsm_lipidios, outros):
        if valor < 0:
            raise ValueError("Componentes não podem ser negativos")
    return mOsm_amino + mOsm_dextrose + mOsm_lipidios + outros


def avaliar_refeeding(fosforo: float, magnesio: float, potassio: float) -> str:
    """Classifica risco de síndrome de realimentação."""

    if fosforo < 2 or magnesio < 1.6 or potassio < 3.2:
        return "Alto risco — repletar eletrólitos e iniciar com 60% da meta"
    if fosforo < 2.5 or magnesio < 1.8 or potassio < 3.4:
        return "Risco moderado — monitorar 2/2h e suplementar conforme necessário"
    return "Baixo risco — prosseguir com escalonamento planejado"


def ajustar_lipidio(triglicerideos: float) -> str:
    """Sugere ajuste da infusão lipídica conforme triglicerídeos séricos."""

    if triglicerideos < 0:
        raise ValueError("Triglicerídeos não podem ser negativos")
    if triglicerideos >= 500:
        return "Suspender lipídio por 24-48h e reintroduzir em 50% da dose"
    if triglicerideos >= 400:
        return "Reduzir lipídio em 50% e reavaliar em 24h"
    return "Manter dose atual com monitorização semanal"


def ritmo_infusao(volume_total_ml: float, horas: float) -> float:
    """Calcula ritmo necessário da bomba em mL/h."""

    if horas <= 0:
        raise ValueError("Horas deve ser positiva")
    if volume_total_ml < 0:
        raise ValueError("Volume não pode ser negativo")
    return volume_total_ml / horas


__all__ = [
    "ComposicaoNPT",
    "calcular_osmolaridade",
    "avaliar_refeeding",
    "ajustar_lipidio",
    "ritmo_infusao",
]
