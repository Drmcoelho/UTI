# Simulador — Módulo 08 — Acesso Arterial Avançado

Ferramentas para análise de perfusão distal, planejamento do sítio e avaliação da curva arterial.

## Uso

```bash
python -i simuladores/modulo_08_acesso_arterial.py
```

### Exemplo

```python
from simuladores.modulo_08_acesso_arterial import AvaliacaoAcessoArterial, analisar_curva_pressao
estado = AvaliacaoAcessoArterial(pam=70, pic=20, spo2_distal=90, delta_temp=3.5)
print(estado.alerta())
print(analisar_curva_pressao([12, 11, 8]))
```

## Funções

- `AvaliacaoAcessoArterial.alerta()`: sintetiza alertas hemodinâmicos e de perfusão.
- `recomendar_sitio(...)`: orienta seleção do vaso.
- `estimar_volume_hemostatico(...)`: planeja curativo compressivo.
- `analisar_curva_pressao(...)`: detecta tendência de obstrução ou overshoot.
