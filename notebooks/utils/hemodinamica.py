"""Rotinas reutilizáveis para cálculos hemodinâmicos e ventilatórios."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, NamedTuple, Tuple

import numpy as np
import pandas as pd


SexoBiologico = Literal["M", "F"]


class VolumeCorrenteResult(NamedTuple):
    """Resultado do cálculo de volume corrente ARDSNet.
    
    Attributes:
        vc: Volume corrente alvo em mL (6 mL/kg do peso predito)
        pbw: Peso corporal predito em kg
    """
    vc: float
    pbw: float


class TabelaPeepFio2(NamedTuple):
    """Tabelas ARDSNet de combinações PEEP/FiO2.
    
    Attributes:
        baixa: Tabela de estratégia PEEP baixa
        alta: Tabela de estratégia PEEP alta
    """
    baixa: pd.DataFrame
    alta: pd.DataFrame


class CurvaPressaoResult(NamedTuple):
    """Resultado da geração de curva de pressão arterial.
    
    Attributes:
        tempo: Array de tempos em segundos
        pressao: Array de pressões em mmHg
        pam: Pressão arterial média em mmHg
    """
    tempo: np.ndarray
    pressao: np.ndarray
    pam: float


@dataclass(frozen=True)
class RespostaVasopressor:
    """Resultado consolidado de uma simulação hemodinâmica."""

    pas: float
    pad: float
    pam: float
    lactato: float


def calcular_pam(pas: float, pad: float) -> float:
    """Calcula a Pressão Arterial Média (PAM)."""

    pam = pad + (pas - pad) / 3
    return round(float(pam), 1)


def simular_parametros_vasopressor(
    dose_noradrenalina: float,
    *,
    volemia: Literal["Hipovolemia", "Adequada", "Hipervolemia"],
    resistencia: Literal["Muito Baixa", "Baixa", "Normal", "Alta"],
) -> RespostaVasopressor:
    """Simula a resposta hemodinâmica esperada ao ajuste de vasopressor."""

    pas_basal = 75.0
    pad_basal = 45.0

    incremento_pas = dose_noradrenalina * 150
    incremento_pad = dose_noradrenalina * 100

    if volemia == "Hipovolemia":
        incremento_pas *= 0.6
        incremento_pad *= 0.6
    elif volemia == "Hipervolemia":
        incremento_pas *= 1.2
        incremento_pad *= 1.2

    if resistencia == "Muito Baixa":
        incremento_pas *= 1.3
        incremento_pad *= 1.3
    elif resistencia == "Alta":
        incremento_pas *= 0.7
        incremento_pad *= 0.7

    pas_final = min(pas_basal + incremento_pas, 180)
    pad_final = min(pad_basal + incremento_pad, 110)
    pam_final = calcular_pam(pas_final, pad_final)

    lactato_basal = 4.2
    if pam_final >= 65:
        reducao_lactato = (pam_final - 65) * 0.03
        lactato_final = max(lactato_basal - reducao_lactato, 0.5)
    else:
        lactato_final = lactato_basal + (65 - pam_final) * 0.02

    return RespostaVasopressor(
        pas=round(pas_final, 1),
        pad=round(pad_final, 1),
        pam=pam_final,
        lactato=round(lactato_final, 1),
    )


def calcular_peso_predito(altura_cm: float, sexo: SexoBiologico) -> float:
    """Calcula o Peso Predito (PBW) de acordo com sexo biológico."""

    if sexo.upper() == "M":
        pbw = 50 + 0.91 * (altura_cm - 152.4)
    else:
        pbw = 45.5 + 0.91 * (altura_cm - 152.4)
    return round(float(pbw), 1)


def calcular_volume_corrente_ardsnet(altura_cm: float, sexo: SexoBiologico) -> VolumeCorrenteResult:
    """Retorna o volume corrente alvo (6 mL/kg) e o peso predito."""

    pbw = calcular_peso_predito(altura_cm, sexo)
    vc = pbw * 6
    return VolumeCorrenteResult(vc=round(vc, 0), pbw=pbw)


def calcular_driving_pressure(pplat: float, peep: float) -> float:
    """Calcula a Driving Pressure (ΔP = Pplat - PEEP)."""

    return float(pplat - peep)


def criar_tabela_peep_fio2() -> TabelaPeepFio2:
    """Gera as tabelas ARDSNet de PEEP/FiO2."""

    tabela_baixa = pd.DataFrame(
        {
            "FiO2": [0.3, 0.4, 0.4, 0.5, 0.5, 0.6, 0.7, 0.7, 0.7, 0.8, 0.9, 0.9, 0.9, 1.0],
            "PEEP": [5, 5, 8, 8, 10, 10, 10, 12, 14, 14, 14, 16, 18, 18],
        }
    )

    tabela_alta = pd.DataFrame(
        {
            "FiO2": [0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
            "PEEP": [5, 8, 10, 12, 14, 14, 16, 16, 18, 20, 20, 20, 22, 22, 24],
        }
    )

    return TabelaPeepFio2(baixa=tabela_baixa, alta=tabela_alta)


def gerar_curva_pressao(
    pas: float,
    pad: float,
    fc: float,
    *,
    pontos: int = 1000,
) -> CurvaPressaoResult:
    """Calcula a série temporal de pressão arterial para um ciclo cardíaco."""

    periodo = 60 / fc
    duracao_sistole = periodo * 0.35
    t = np.linspace(0, periodo, pontos)
    pressao = np.zeros_like(t)

    for i, tempo in enumerate(t):
        if tempo < duracao_sistole:
            fator = tempo / duracao_sistole
            pressao[i] = pad + (pas - pad) * (1 - np.cos(np.pi * fator)) / 2
        else:
            tempo_diastole = tempo - duracao_sistole
            duracao_diastole = periodo - duracao_sistole
            fator = tempo_diastole / duracao_diastole
            pressao[i] = pad + (pas - pad) * 0.5 * np.exp(-3 * fator) * (1 + np.cos(np.pi * fator))

    pam = calcular_pam(pas, pad)
    return CurvaPressaoResult(tempo=t, pressao=pressao, pam=pam)


__all__ = [
    "VolumeCorrenteResult",
    "TabelaPeepFio2",
    "CurvaPressaoResult",
    "RespostaVasopressor",
    "calcular_pam",
    "simular_parametros_vasopressor",
    "calcular_peso_predito",
    "calcular_volume_corrente_ardsnet",
    "calcular_driving_pressure",
    "criar_tabela_peep_fio2",
    "gerar_curva_pressao",
]
