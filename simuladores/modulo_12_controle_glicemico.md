# Simulador — Módulo 12 — Controle Glicêmico

Scripts permitem estimar taxa de variação, ajuste da bomba de insulina e impacto de pausas de dieta.

## Exemplo

```python
from simuladores.modulo_12_controle_glicemico import MedicaoGlicemica, sugerir_ajuste_taxa, avaliar_pausa_dieta

med = MedicaoGlicemica(glicemia_atual=220, glicemia_anterior=180, intervalo_horas=1)
print(med.variacao_por_hora)
print(sugerir_ajuste_taxa(med.variacao_por_hora, taxa_atual=2.0))
print(avaliar_pausa_dieta(90, 3.0))
```

## Cenários
- Calcular time-in-range a partir de medições seriadas.
- Classificar risco de hipoglicemia em pacientes com insuficiência renal.
- Ajustar taxa de insulina após interrupção de dieta enteral ou início de NPT.
