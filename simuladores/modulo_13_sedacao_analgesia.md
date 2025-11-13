# Simulador — Módulo 13 — Sedação e Analgesia

Ferramentas para avaliar metas de RASS/CPOT, risco de hipertrigliceridemia e adesão ao bundle.

```python
from simuladores.modulo_13_sedacao_analgesia import PlanoSedacao, risco_hipertrigliceridemia, adesao_bundle

plano = PlanoSedacao(rass_meta_min=-2, rass_meta_max=0)
print(plano.avaliar_rass(-4))
print(plano.avaliar_cpot(5))
print(risco_hipertrigliceridemia(450))
print(adesao_bundle([True, True, False, True, True, False]))
```

Explore diferentes metas para sedação cooperativa, cálculos de dose de dexmedetomidina e relatórios de adesão ABCDEF.
