import os
import sys

import numpy as np

sys.path.insert(0, os.path.abspath("."))

from notebooks.utils.hemodinamica import (
    CurvaPressaoResult,
    RespostaVasopressor,
    TabelaPeepFio2,
    VolumeCorrenteResult,
    calcular_driving_pressure,
    calcular_pam,
    calcular_peso_predito,
    calcular_volume_corrente_ardsnet,
    criar_tabela_peep_fio2,
    gerar_curva_pressao,
    simular_parametros_vasopressor,
)


def test_calcular_pam():
    assert calcular_pam(120, 80) == 93.3


def test_calcular_peso_predito_masculino():
    assert calcular_peso_predito(180, "M") == 75.1


def test_calcular_peso_predito_feminino():
    assert calcular_peso_predito(165, "F") == 57.0


def test_calcular_volume_corrente_ardsnet():
    resultado = calcular_volume_corrente_ardsnet(170, "M")
    assert isinstance(resultado, VolumeCorrenteResult)
    assert resultado.vc == 396
    assert resultado.pbw == 66.0
    # Test that tuple unpacking still works
    vc, pbw = resultado
    assert vc == 396
    assert pbw == 66.0


def test_calcular_driving_pressure():
    assert calcular_driving_pressure(28, 10) == 18


def test_criar_tabela_peep_fio2():
    resultado = criar_tabela_peep_fio2()
    assert isinstance(resultado, TabelaPeepFio2)
    assert resultado.baixa.shape == (14, 2)
    assert resultado.alta.iloc[-1].to_dict() == {"FiO2": 1.0, "PEEP": 24}
    # Test that tuple unpacking still works
    baixa, alta = resultado
    assert baixa.shape == (14, 2)
    assert alta.iloc[-1].to_dict() == {"FiO2": 1.0, "PEEP": 24}


def test_gerar_curva_pressao_dimensions():
    resultado = gerar_curva_pressao(120, 80, 80)
    assert isinstance(resultado, CurvaPressaoResult)
    assert resultado.tempo.shape == resultado.pressao.shape
    assert isinstance(resultado.pam, float)
    assert np.isclose(resultado.pam, 93.3)
    # Test that tuple unpacking still works
    t, pressao, pam = resultado
    assert t.shape == pressao.shape
    assert isinstance(pam, float)
    assert np.isclose(pam, 93.3)


def test_simular_parametros_vasopressor_typing():
    resposta = simular_parametros_vasopressor(
        0.3,
        volemia="Adequada",
        resistencia="Normal",
    )
    assert isinstance(resposta, RespostaVasopressor)
    assert resposta.pam >= 65
