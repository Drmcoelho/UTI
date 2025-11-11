from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
import sys
sys.path.insert(0, str(PROJECT_ROOT))

from simuladores.modulo_01_pressao_invasiva import (
    calcular_pam,
    classificar_pam,
    avaliar_ppv,
    estimar_ajuste_vasopressor,
)
from simuladores.modulo_02_monitorizacao_nao_invasiva import (
    validar_serie_pam,
    estimar_debito_cardiaco,
    needs_escalation,
)
from simuladores.modulo_03_cateter_arteria_pulmonar import (
    Hemodinamica,
    classificar_fenotipo,
    pronta_retirada,
)
from simuladores.modulo_04_ecocardiografia_pocus import (
    calcular_volume_sistolico_lvot,
    calcular_debito_cardiaco as calcular_dc_pocus,
    classificar_estado_volumico,
    avaliar_tapse,
    estimar_pressao_capilar_pulmonar,
)
from simuladores.modulo_05_oximetria_capnografia import (
    carregar_alarmes,
    avaliar_oximetria,
    calcular_gradiente_co2,
    interpretar_capnograma,
    avaliar_tendencia_etco2,
)
from exercicios import (
    modulo_01_monitorizacao_invasiva as quiz01,
    modulo_02_monitorizacao_nao_invasiva as quiz02,
    modulo_03_cateter_arteria_pulmonar as quiz03,
    modulo_04_ecocardiografia_pocus as quiz04,
    modulo_05_oximetria_capnografia as quiz05,
)


def test_calcular_pam_and_classificacao():
    pam = calcular_pam(96, 54)
    assert pytest.approx(pam, 0.1) == 68.0
    curva = classificar_pam(pam)
    assert curva.fase == "pos_ressuscitacao"


def test_avaliar_ppv_thresholds():
    assert "responsividade" in avaliar_ppv(15)
    assert "Zona cinzenta" in avaliar_ppv(10)
    assert "não responsivo" in avaliar_ppv(5)


def test_estimativa_vasopressor_adjustment():
    fator = estimar_ajuste_vasopressor(60, pam_alvo=65)
    assert fator > 1
    with pytest.raises(ValueError):
        estimar_ajuste_vasopressor(-1)


def test_validar_serie_pam():
    assert validar_serie_pam([80, 83, 82])
    assert not validar_serie_pam([80, 90, 82], tolerancia=5)
    with pytest.raises(ValueError):
        validar_serie_pam([])


def test_estimativa_debito_cardiaco():
    debito = estimar_debito_cardiaco(3.1, 14, 96)
    assert pytest.approx(debito, 0.1) == 4.2
    with pytest.raises(ValueError):
        estimar_debito_cardiaco(-1, 14, 90)


def test_needs_escalation_flags_low_values():
    assert needs_escalation(1.0, 70)
    assert needs_escalation(2.0, 60)
    assert not needs_escalation(2.0, 70)


def test_cateter_hemodinamica_metrics():
    hemo = Hemodinamica(18, 31, 28, 3.0, 1.9)
    assert pytest.approx(hemo.indice_cardiaco, 0.01) == 1.58
    assert pytest.approx(hemo.resistencia_vascular_sistemica(63), 0.1) == 1200
    assert "cardiogênico" in classificar_fenotipo(hemo)
    assert not pronta_retirada(hemo, pam=60, svo2=0.6, lactato=2.5)

    hemo_otimizado = Hemodinamica(8, 22, 12, 4.5, 1.8)
    assert pronta_retirada(hemo_otimizado, pam=70, svo2=0.7, lactato=1.5)


def test_pocus_calculations_and_classification():
    volume = calcular_volume_sistolico_lvot(2.0, 18)
    assert pytest.approx(volume, 0.1) == pytest.approx(56.5, 0.1)
    debito = calcular_dc_pocus(2.0, 18, 90)
    assert pytest.approx(debito, 0.1) == pytest.approx(5.1, 0.1)
    status = classificar_estado_volumico(17, 2.4, 8, ventilacao_controlada=True)
    assert "baixo" in status.lower()
    assert "VD" in avaliar_tapse(16)
    assert estimar_pressao_capilar_pulmonar(14) > 15


def test_oximetria_capnografia_tools():
    alarmes = carregar_alarmes()
    assert "SpO2" in alarmes
    resumo = avaliar_oximetria(89, 0.3)
    assert "SpO₂ abaixo" in resumo
    gradiente, status = calcular_gradiente_co2(32, 45)
    assert pytest.approx(gradiente, 0.1) == 13
    assert ">10" in status
    assert "tubar" in interpretar_capnograma(retorno_base=True, formato_plato="dente de tubarão", co2_inspiratorio=1)
    tendencia = avaliar_tendencia_etco2([10, 12, 14, 16, 18, 20])
    assert "ascensão" in tendencia


def test_quiz_counts_are_consistent():
    for module in (quiz01, quiz02, quiz03, quiz04, quiz05):
        counts = module.resumo_banco()
        assert counts["dissertativas"] == 3
        assert counts["mcq"] == 8
        assert counts["vf"] == 15
