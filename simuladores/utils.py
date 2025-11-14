"""Módulo de utilidades compartilhadas entre simuladores."""
from __future__ import annotations


def calcular_ppc(pam: float, pic: float) -> float:
    """Calcula pressão de perfusão cerebral (PPC).
    
    PPC = PAM - PIC
    
    Args:
        pam: Pressão arterial média (mmHg)
        pic: Pressão intracraniana (mmHg)
        
    Returns:
        Pressão de perfusão cerebral em mmHg
        
    Raises:
        ValueError: Se PAM for não-positiva ou PIC for negativa
    """
    if pam <= 0 or pic < 0:
        raise ValueError("PAM deve ser positiva e PIC não pode ser negativa")
    return pam - pic


__all__ = ["calcular_ppc"]
