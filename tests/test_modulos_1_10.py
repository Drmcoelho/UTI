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
from simuladores.modulo_06_pressao_intracraniana import (
    EstadoPIC,
    classificar_crise_pic,
    volume_drenagem_recomendado,
    avaliar_bundle_basico,
)
from simuladores.utils import calcular_ppc
from simuladores.modulo_07_acesso_venoso_central import (
    AvaliacaoCVC,
    dias_para_troca_curativo,
    avaliar_bundle,
    necessidade_cultura,
    sugestao_via_acesso,
)
from simuladores.modulo_08_acesso_arterial import (
    AvaliacaoAcessoArterial,
    recomendar_sitio,
    estimar_volume_hemostatico,
    analisar_curva_pressao,
)
from simuladores.modulo_09_balanco_hidrico import (
    BalançoHidrico,
    calcular_meta_remocao,
    avaliar_diuretico_sequencial,
    planejar_ultrafiltracao,
)
from simuladores.modulo_10_nutricao_enteral import (
    PlanoNutricional,
    cobertura_calorica,
    avaliar_tolerancia,
    ajustar_taxa_atual,
    necessidade_suplemento_zinco,
)
from exercicios import (
    modulo_01_monitorizacao_invasiva as quiz01,
    modulo_02_monitorizacao_nao_invasiva as quiz02,
    modulo_03_cateter_arteria_pulmonar as quiz03,
    modulo_04_ecocardiografia_pocus as quiz04,
    modulo_05_oximetria_capnografia as quiz05,
    modulo_06_pressao_intracraniana as quiz06,
    modulo_07_acesso_venoso_central as quiz07,
    modulo_08_acesso_arterial as quiz08,
    modulo_09_balanco_hidrico as quiz09,
    modulo_10_nutricao_enteral as quiz10,
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


def test_pic_tools_and_bundle():
    estado = EstadoPIC(pam=85, pic=26, pbt_o2=18, sodio=156)
    assert calcular_ppc(estado.pam, estado.pic) == estado.ppc
    resumo = classificar_crise_pic(estado)
    assert "PPC" in resumo and "Hipernatremia" in resumo
    assert pytest.approx(volume_drenagem_recomendado([26, 28, 30]), 0.1) == 10.0
    assert "Bundle" in avaliar_bundle_basico(True, True, True)
    assert "Ajustar" in avaliar_bundle_basico(False, True, False)


def test_cvc_risk_and_bundle_metrics():
    avaliacao = AvaliacaoCVC(dias_curativo=8, temperatura=38.2, sinais_locais=True, bundle_insercao=False)
    assert "Risco elevado" in avaliacao.risco_infeccao()
    assert dias_para_troca_curativo(3) == 4
    assert pytest.approx(avaliar_bundle([True, False, True, True]), 0.1) == 75.0
    assert necessidade_cultura(True, False, False)
    assert "Jugular" in sugestao_via_acesso("vasopressor", False, False)


def test_acesso_arterial_analysis():
    acesso = AvaliacaoAcessoArterial(pam=72, pic=20, spo2_distal=90, delta_temp=3.4)
    alerta = acesso.alerta()
    assert "PPC" in alerta and "SpO₂" in alerta
    assert "axilar" in recomendar_sitio(True, False, False).lower()
    assert estimar_volume_hemostatico(4.0, vasopressor=True) > estimar_volume_hemostatico(4.0, vasopressor=False)
    assert "obstrução" in analisar_curva_pressao([12, 11, 8])


def test_balanco_hidrico_simulation():
    estado = BalançoHidrico(peso_ideal=68, balanco_acumulado_ml=8000)
    assert estado.classificar() == "Sobrecarga crítica"
    assert calcular_meta_remocao(estado.balanco_acumulado_ml, 2000) > 0
    assert avaliar_diuretico_sequencial([15, 25, 35]) == "Resposta adequada"
    assert "contínua" in planejar_ultrafiltracao(False, True, True).lower()


def test_nutricao_enteral_plan():
    plano = PlanoNutricional(peso=76, kcal_kg=30, proteina_kg=1.8, densidade_formula=1.5)
    assert plano.calorias_totais == 2280
    assert pytest.approx(plano.volume_alvo, 0.1) == pytest.approx(1520.0, 0.1)
    assert cobertura_calorica(plano, 1200) < 100
    assert "Intolerância" in avaliar_tolerancia(600, False, False)
    assert pytest.approx(ajustar_taxa_atual(plano.volume_alvo, 800, 8), 0.1) == pytest.approx(90.0, 0.1)
    assert necessidade_suplemento_zinco(True, 85)


def test_quiz_counts_are_consistent():
    for module in (quiz01, quiz02, quiz03, quiz04, quiz05, quiz06, quiz07, quiz08, quiz09, quiz10):
        counts = module.resumo_banco()
        assert counts["dissertativas"] == 3
        assert counts["mcq"] == 8
        assert counts["vf"] == 15
