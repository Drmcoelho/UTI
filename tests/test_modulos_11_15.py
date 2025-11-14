from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
import sys
sys.path.insert(0, str(PROJECT_ROOT))

from simuladores.modulo_11_nutricao_parenteral import (
    ComposicaoNPT,
    ajustar_lipidio,
    avaliar_refeeding,
    calcular_osmolaridade,
    ritmo_infusao,
)
from simuladores.modulo_12_controle_glicemico import (
    MedicaoGlicemica,
    avaliar_pausa_dieta,
    risco_hipoglicemia,
    sugerir_ajuste_taxa,
    tempo_na_meta,
)
from simuladores.modulo_13_sedacao_analgesia import (
    PlanoSedacao,
    adesao_bundle,
    dose_dexmedetomidina,
    risco_hipertrigliceridemia,
)
from simuladores.modulo_14_bloqueio_neuromuscular import (
    AvaliacaoTOF,
    dose_cisatracurio,
    resumo_bundle,
)
from simuladores.utils import calcular_ppc
from simuladores.modulo_15_delirium_uti import (
    adesao_bundle_delirium,
    alerta_qtc,
    cam_icu_result,
    classificar_risco,
    escore_risco,
)

from exercicios import (
    modulo_11_nutricao_parenteral as quiz11,
    modulo_12_controle_glicemico as quiz12,
    modulo_13_sedacao_analgesia as quiz13,
    modulo_14_bloqueio_neuromuscular as quiz14,
    modulo_15_delirium_uti as quiz15,
)


def test_composicao_npt_calculations():
    plano = ComposicaoNPT(peso_atual=64, altura_m=1.72, imc_atual=21.6, imc_alvo=22.0, kcal_por_kg=30, proteina_por_kg=1.8)
    assert pytest.approx(plano.peso_ajustado, 0.01) == 65.18
    assert pytest.approx(plano.calorias_totais, 0.1) == 1955.4
    assert pytest.approx(plano.proteina_total, 0.1) == 117.32
    osm = calcular_osmolaridade(600, 900, 200, outros=100)
    assert osm == 1800
    assert "Alto risco" in avaliar_refeeding(1.8, 1.5, 3.1)
    assert "Reduzir" in ajustar_lipidio(420)
    assert "Suspender" in ajustar_lipidio(520)
    assert pytest.approx(ritmo_infusao(1800, 18), 0.1) == 100.0


def test_controle_glicemico_tools():
    med = MedicaoGlicemica(glicemia_atual=230, glicemia_anterior=180, intervalo_horas=1)
    assert med.variacao_por_hora == 50
    assert pytest.approx(sugerir_ajuste_taxa(med.variacao_por_hora, 2.0), 0.1) == 3.0
    assert pytest.approx(avaliar_pausa_dieta(90, 4.0), 0.1) == 2.0
    assert avaliar_pausa_dieta(150, 4.0) == 0.0
    tempo = tempo_na_meta([150, 165, 142, 130, 200], 110, 180)
    assert pytest.approx(tempo, 0.1) == 80.0
    assert "Moderado" in risco_hipoglicemia(68, False, False)
    assert "Alto risco" in risco_hipoglicemia(35, True, True)


def test_plano_sedacao_bundle_metrics():
    plano = PlanoSedacao(rass_meta_min=-2, rass_meta_max=0)
    assert "profunda" in plano.avaliar_rass(-4)
    assert "insuficiente" in plano.avaliar_rass(1)
    assert plano.avaliar_cpot(2) == "Analgesia adequada"
    assert "Dor" in plano.avaliar_cpot(5)
    assert "Reduzir" in risco_hipertrigliceridemia(450)
    assert "Suspender" in risco_hipertrigliceridemia(1100)
    assert dose_dexmedetomidina(70, "delirium") == (0.3, 1.0)
    assert pytest.approx(adesao_bundle([True, True, False, True, True, False]), 0.1) == 66.7


def test_bloqueio_neuromuscular_supports():
    avaliacao = AvaliacaoTOF(respostas_tof=0, contagem_postetanica=2)
    assert "adequado" in avaliacao.classificar()
    avaliacao_superficial = AvaliacaoTOF(respostas_tof=3, contagem_postetanica=None)
    assert "superficial" in avaliacao_superficial.classificar()
    assert dose_cisatracurio(70, "desmame") == 1.0
    assert "alta" in resumo_bundle([True, True, True, False, True])
    assert calcular_ppc(75, 18) == 57


def test_delirium_tools_and_risk():
    assert cam_icu_result(True, True, False, True)
    assert not cam_icu_result(True, False, True, True)
    score = escore_risco(35, [5, 10])
    assert pytest.approx(score, 0.1) == 50.0
    assert classificar_risco(score) == "Alto"
    assert "Monitorizar" in alerta_qtc(480)
    assert "evitar".lower() in alerta_qtc(510).lower()
    assert pytest.approx(adesao_bundle_delirium([True, False, True, True, True]), 0.1) == 80.0


def test_quiz_counts_consistent_modulos_11_15():
    for module in (quiz11, quiz12, quiz13, quiz14, quiz15):
        counts = module.resumo_banco()
        assert counts["dissertativas"] == 3
        assert counts["mcq"] == 8
        assert counts["vf"] == 15
