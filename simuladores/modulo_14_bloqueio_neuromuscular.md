# Simulador — Módulo 14 — Bloqueio Neuromuscular

Ferramenta rápida para classificar TOF, definir dose alvo e avaliar adesão ao bundle.

```python
from simuladores.modulo_14_bloqueio_neuromuscular import AvaliacaoTOF, resumo_bundle

avaliacao = AvaliacaoTOF(respostas_tof=0, contagem_postetanica=2)
print(avaliacao.classificar())
print(resumo_bundle([True, True, False, True, True, True]))
```

Integre o cálculo de PPC (PAM − PIC) para alinhar metas neurológicas e defina faixas de cisatracúrio conforme estágio (induçãomanutenção-desmame).
