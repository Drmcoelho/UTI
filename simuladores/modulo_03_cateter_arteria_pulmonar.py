"""Simulador para o módulo 03 (cateter de artéria pulmonar)."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PARAM_PATH = PROJECT_ROOT / "recursos" / "03_cateter_arteria_pulmonar" / "parametros_referencia.json"


@dataclass(frozen=True)
class Hemodinamica:
    pad_mmHg: float
    pap_media_mmHg: float
    pcp_mmHg: float
    debito_cardiaco_l_min: float
    superficie_corporea_m2: float

    @property
    def indice_cardiaco(self) -> float:
        if self.superficie_corporea_m2 <= 0:
            raise ValueError("Superfície corporal inválida")
        return self.debito_cardiaco_l_min / self.superficie_corporea_m2

    def resistencia_vascular_sistemica(self, pam: float) -> float:
        if pam <= 0:
            raise ValueError("PAM deve ser positiva")
        return 80 * (pam - self.pad_mmHg) / self.debito_cardiaco_l_min

    def resistencia_vascular_pulmonar(self) -> float:
        return 80 * (self.pap_media_mmHg - self.pcp_mmHg) / self.debito_cardiaco_l_min


def carregar_parametros_referencia() -> dict:
    with PARAM_PATH.open(encoding="utf-8") as fp:
        return json.load(fp)


def classificar_fenotipo(hemo: Hemodinamica) -> str:
    """Classifica o fenótipo hemodinâmico baseado em pressões e IC."""
    dados = carregar_parametros_referencia()
    metas = dados["metas_hemodinamicas"]
    if hemo.indice_cardiaco < metas["indice_cardiaco_min"] and hemo.pcp_mmHg > dados["intervalos_pressao"]["pcp_mmHg"]["alerta"][0]:
        return "Choque cardiogênico congestivo"
    if hemo.indice_cardiaco < metas["indice_cardiaco_min"]:
        return "Choque cardiogênico com pré-carga adequada"
    if hemo.pcp_mmHg < dados["intervalos_pressao"]["pcp_mmHg"]["otimo"][0]:
        return "Possível hipovolemia"
    return "Perfusão aceitável com monitorização contínua"


def pronta_retirada(hemo: Hemodinamica, pam: float, svo2: float, lactato: float) -> bool:
    dados = carregar_parametros_referencia()
    metas = dados["metas_hemodinamicas"]
    return (
        hemo.indice_cardiaco >= metas["indice_cardiaco_min"]
        and svo2 >= metas["saturacao_venosa_mista"]
        and lactato <= metas["lactato_max"]
        and pam >= 65
    )


__all__ = [
    "Hemodinamica",
    "carregar_parametros_referencia",
    "classificar_fenotipo",
    "pronta_retirada",
]
