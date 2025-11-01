"""Funções de visualização para parâmetros clínicos."""
from __future__ import annotations

from typing import Iterable, Optional, Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np

_DEFAULT_VOLUME_RANGE_ML_PER_KG: Tuple[float, float] = (4.0, 8.0)
_DEFAULT_PRESSURE_LIMITS = {
    "PEEP": 5.0,
    "Pplat": 30.0,
    "ΔP": 15.0,
}


def _coerce_float(name: str, value: Optional[float], *, allow_zero: bool = True) -> float:
    """Convert *value* to ``float`` ensuring it is non-negative (or positive)."""
    if value is None:
        raise ValueError(f"O parâmetro '{name}' não pode ser None.")

    try:
        converted = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"O parâmetro '{name}' deve ser numérico.") from exc

    if allow_zero:
        if converted < 0:
            raise ValueError(f"O parâmetro '{name}' deve ser maior ou igual a zero.")
    else:
        if converted <= 0:
            raise ValueError(f"O parâmetro '{name}' deve ser maior que zero.")

    return converted


def _format_bar_labels(bars: Iterable, units: str = "") -> None:
    """Annotate bars with their height formatted in whole numbers."""

    for bar in bars:
        height = bar.get_height()
        suffix = f" {units}" if units else ""
        bar.axes.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{height:.0f}{suffix}",
            ha="center",
            va="bottom",
            fontweight="bold",
            fontsize=11,
        )


def visualizar_parametros_ventilatorios(
    pbw: float,
    vc_alvo: Optional[float],
    pplat: Optional[float],
    peep: Optional[float],
    driving_pressure: Optional[float],
    *,
    volume_range_ml_per_kg: Tuple[float, float] = _DEFAULT_VOLUME_RANGE_ML_PER_KG,
    pressure_limits: Optional[Sequence[float]] = None,
    show: bool = True,
):
    """
    Criar visualização gráfica dos parâmetros ventilatórios.

    Gera dois gráficos lado a lado, destacando limites recomendados para
    ventilação protetora em pacientes com SDRA.

    Parâmetros
    ----------
    pbw:
        Peso Predito (PBW) em kg. Deve ser maior que zero.
    vc_alvo:
        Volume corrente alvo em mL. Caso ``None``, é calculado automaticamente
        como ``pbw * 6`` (6 mL/kg).
    pplat:
        Pressão de platô em cmH2O. Necessária para os gráficos de pressão.
    peep:
        PEEP em cmH2O.
    driving_pressure:
        Driving pressure (ΔP) em cmH2O. Quando ``None``, é deduzido de
        ``pplat - peep``.
    volume_range_ml_per_kg:
        Faixa (mínimo, máximo) em mL/kg exibida no gráfico de volumes.
    pressure_limits:
        Limites de segurança para ``PEEP``, ``Pplat`` e ``ΔP``. Caso não seja
        informado, utiliza ``(5, 30, 15)``.
    show:
        Exibe a figura imediatamente quando ``True`` (padrão).

    Returns
    -------
    (fig, (ax_volume, ax_pressao)):
        Figura e eixos gerados, permitindo reutilização em outros contextos
        (por exemplo, testes automatizados ou dashboards).
    """

    pbw = _coerce_float("pbw", pbw, allow_zero=False)

    volume_min_ml_per_kg, volume_max_ml_per_kg = volume_range_ml_per_kg
    vc_min = pbw * volume_min_ml_per_kg
    vc_max = pbw * volume_max_ml_per_kg

    if vc_alvo is None:
        vc_alvo = pbw * 6
    vc_alvo = _coerce_float("vc_alvo", vc_alvo, allow_zero=False)

    pplat = _coerce_float("pplat", pplat)
    peep = _coerce_float("peep", peep)

    if driving_pressure is None:
        driving_pressure = pplat - peep
    driving_pressure = _coerce_float("driving_pressure", driving_pressure)

    pressure_limits = (
        pressure_limits
        if pressure_limits is not None
        else tuple(_DEFAULT_PRESSURE_LIMITS[label] for label in ("PEEP", "Pplat", "ΔP"))
    )

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    categories = [
        f"Mínimo\n({volume_min_ml_per_kg:.0f} mL/kg)",
        "ALVO\n(6 mL/kg)",
        f"Máximo\n({volume_max_ml_per_kg:.0f} mL/kg)",
    ]
    values = [vc_min, vc_alvo, vc_max]
    colors = ["#ffd93d", "#6bcf7f", "#ffd93d"]

    bars1 = ax1.bar(categories, values, color=colors, edgecolor="black", linewidth=2)
    ax1.set_ylabel("Volume (mL)", fontsize=12, fontweight="bold")
    ax1.set_title("Volume Corrente - Ventilação Protetora", fontsize=13, fontweight="bold")
    ax1.axhline(y=vc_alvo, color="red", linestyle="--", linewidth=2, alpha=0.7)
    _format_bar_labels(bars1, "mL")

    pressure_labels = ["PEEP", "Pplat", "ΔP"]
    pressure_values = [peep, pplat, driving_pressure]

    x_pos = np.arange(len(pressure_labels))
    bars2 = ax2.bar(
        x_pos,
        pressure_values,
        color=["#4ecdc4", "#ff6b6b", "#ffd93d"],
        edgecolor="black",
        linewidth=2,
        label="Valor Atual",
    )

    for i, lim in enumerate(pressure_limits):
        color = "green" if i == 0 else "red"
        ax2.axhline(y=lim, color=color, linestyle="--", linewidth=1.5, alpha=0.5)

    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(pressure_labels)
    ax2.set_ylabel("Pressão (cmH2O)", fontsize=12, fontweight="bold")
    ax2.set_title("Pressões Ventilatórias", fontsize=13, fontweight="bold")
    _format_bar_labels(bars2, "cmH2O")

    plt.tight_layout()

    if show:
        plt.show()

    return fig, (ax1, ax2)
