"""Ferramentas para o simulador do módulo 07 (acesso venoso central)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AvaliacaoCVC:
    dias_curativo: int
    temperatura: float
    sinais_locais: bool
    bundle_insercao: bool

    def risco_infeccao(self) -> str:
        """Resume o risco infeccioso com base nos parâmetros atuais."""

        alertas: list[str] = []
        if not self.bundle_insercao:
            alertas.append("bundle incompleto na inserção")
        if self.dias_curativo > 7:
            alertas.append("curativo >7 dias")
        if self.sinais_locais:
            alertas.append("sinais locais")
        if self.temperatura >= 38:
            alertas.append("febre")
        if not alertas:
            return "Risco baixo"
        return "Risco elevado: " + ", ".join(alertas)


def dias_para_troca_curativo(dias_atual: int) -> int:
    """Calcula em quantos dias o curativo deve ser trocado novamente."""

    if dias_atual < 0:
        raise ValueError("Dias não pode ser negativo")
    restante = 7 - dias_atual
    return 0 if restante <= 0 else restante


def avaliar_bundle(bundle_itens: Iterable[bool]) -> float:
    """Retorna porcentagem de itens cumpridos no bundle de inserção."""

    itens = list(bundle_itens)
    if not itens:
        raise ValueError("Forneça itens do bundle")
    corretos = sum(1 for item in itens if item)
    return corretos / len(itens) * 100


def necessidade_cultura(sinais_locais: bool, febre: bool, hemodinamica_instavel: bool) -> bool:
    """Determina se culturas devem ser coletadas imediatamente."""

    return sinais_locais or (febre and hemodinamica_instavel)


def sugestao_via_acesso(indicacao: str, trombose_previa: bool, infec_site: bool) -> str:
    """Sugere via de acesso preferencial considerando contexto clínico."""

    indic = indicacao.lower()
    if infec_site:
        return "Trocar para sítio alternativo contralateral"
    if "hemodialise" in indic:
        return "Preferir veia jugular interna direita"
    if "vasopressor" in indic and not trombose_previa:
        return "Jugular interna com US"
    if trombose_previa:
        return "Avaliar veia subclávia guiada por US"
    return "Escolher sítio com melhor anatomia ultrassonográfica"


__all__ = [
    "AvaliacaoCVC",
    "dias_para_troca_curativo",
    "avaliar_bundle",
    "necessidade_cultura",
    "sugestao_via_acesso",
]
