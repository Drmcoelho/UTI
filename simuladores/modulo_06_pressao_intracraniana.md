# Simulador — Módulo 06 — Monitorização da PIC

Ferramentas em Python para calcular PPC, classificar crises hipertensivas intracranianas e decidir intervenções escalonadas.

## Como usar

```bash
python -i simuladores/modulo_06_pressao_intracraniana.py
```

### Exemplo

```python
from simuladores.modulo_06_pressao_intracraniana import EstadoPIC, classificar_crise_pic, volume_drenagem_recomendado
estado = EstadoPIC(pam=85, pic=26, pbt_o2=18, sodio=156)
print(classificar_crise_pic(estado))
print(volume_drenagem_recomendado([26, 28, 30]))
```

## Funções principais

- `calcular_ppc(pam, pic)`: retorna PPC validada.
- `classificar_crise_pic(EstadoPIC)`: produz síntese textual de gravidade e recomendações.
- `volume_drenagem_recomendado(picos)`: sugere volume de drenagem de líquor.
- `avaliar_bundle_basico(...)`: confirma pré-requisitos antes de terapia de resgate.
