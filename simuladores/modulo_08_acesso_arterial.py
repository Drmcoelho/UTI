"""Ferramentas para o simulador do módulo 08 (acesso arterial avançado)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AvaliacaoAcessoArterial:
    pam: float
    pic: float
    spo2_distal: float
    delta_temp: float

    @property
    def ppc(self) -> float:
        return self.pam - self.pic

    def alerta(self) -> str:
        mensagens: list[str] = []
        if self.ppc < 60:
            mensagens.append("PPC <60 mmHg")
        if self.spo2_distal < 92:
            mensagens.append("SpO₂ distal baixa")
        if self.delta_temp > 3:
            mensagens.append("ΔT >3°C")
        return " | ".join(mensagens) if mensagens else "Sem alertas"


def recomendar_sitio(suporte_mecanico: bool, trombose_radial: bool, fistula_av: bool) -> str:
    """Sugere melhor sítio arterial conforme restrições."""

    if fistula_av:
        return "Evitar membro com fístula AV — considerar axilar contralateral"
    if suporte_mecanico:
        return "Preferir artéria axilar contralateral com tunelização"
    if trombose_radial:
        return "Avaliar artéria braquial com ultrassom"
    return "Radial preferencial se anatomia favorável"


def estimar_volume_hemostatico(calibre_cateter: float, vasopressor: bool) -> float:
    """Estima volume do curativo hemostático baseado no calibre do cateter."""

    if calibre_cateter <= 0:
        raise ValueError("Calibre deve ser positivo")
    base = 30 + calibre_cateter * 5
    if vasopressor:
        base += 10
    return base


def analisar_curva_pressao(amplitudes: Iterable[float]) -> str:
    """Analisa tendência da curva arterial a partir das amplitudes registradas."""

    valores = list(amplitudes)
    if len(valores) < 3:
        raise ValueError("Forneça pelo menos 3 amplitudes")
    if any(v <= 0 for v in valores):
        raise ValueError("Amplitude deve ser positiva")
    if valores[-1] < valores[0] * 0.7:
        return "Suspeita de obstrução parcial da linha"
    if valores[-1] > valores[0] * 1.3:
        return "Possível overshoot/under-damping"
    return "Amplitude estável"


__all__ = [
    "AvaliacaoAcessoArterial",
    "recomendar_sitio",
    "estimar_volume_hemostatico",
    "analisar_curva_pressao",
]
