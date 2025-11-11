# Simulador — Módulo 04 (Ecocardiografia à Beira do Leito)

Este simulador permite testar cenários de choque utilizando medidas ecocardiográficas essenciais (VTI, TAPSE, IVC, E/e'). Ele consome os dados de referência em [`recursos/04_ecocardiografia_pocus/medidas_referencia.csv`](../recursos/04_ecocardiografia_pocus/medidas_referencia.csv).

## 🚀 Como executar

```bash
python -i simuladores/modulo_04_ecocardiografia_pocus.py
```

Dentro do shell interativo, utilize as funções expostas para analisar diferentes perfis hemodinâmicos.

## 🔧 Funções principais

| Função | Descrição | Exemplo |
| --- | --- | --- |
| `calcular_volume_sistolico_lvot(diametro_cm, vti_cm)` | Calcula volume sistólico (mL) a partir do diâmetro do TSV e VTI. | `calcular_volume_sistolico_lvot(2.1, 18)` |
| `calcular_debito_cardiaco(diametro_cm, vti_cm, fc)` | Retorna débito cardíaco (L/min). | `calcular_debito_cardiaco(2.1, 18, 92)` |
| `classificar_estado_volumico(vti, ivc_diametro, ivc_colapso, ventilacao_controlada=...)` | Integra VTI e IVC para sugerir status volêmico. | `classificar_estado_volumico(17, 2.3, 8, ventilacao_controlada=True)` |
| `avaliar_tapse(tapse_mm)` | Classifica função sistólica do VD. | `avaliar_tapse(16)` |
| `estimar_pressao_capilar_pulmonar(e_e_prime, e_a=None)` | Estima pressão de enchimento do VE via E/e'. | `estimar_pressao_capilar_pulmonar(14)` |
| `carregar_referencias()` | Carrega limites do arquivo CSV de recursos. | `carregar_referencias()["VTI_cm"]` |

## 🧪 Exemplo de fluxo

```python
from simuladores import modulo_04_ecocardiografia_pocus as pocus

refs = pocus.carregar_referencias()
sv = pocus.calcular_volume_sistolico_lvot(2.0, 20)
debito = pocus.calcular_debito_cardiaco(2.0, 20, 90)
print(f"VS: {sv:.1f} mL | DC: {debito:.2f} L/min")
print(pocus.classificar_estado_volumico(20, 1.8, 35, ventilacao_controlada=False))
print(pocus.avaliar_tapse(18))
print(f"Pressão de enchimento estimada: {pocus.estimar_pressao_capilar_pulmonar(12):.1f} mmHg")
```

## ✅ Boas práticas

- Utilize medidas médias de 3-5 ciclos cardíacos para inserir no simulador, replicando a prática clínica.
- Documente os resultados no prontuário e compare com os critérios do caso clínico e exercícios correspondentes.
- Sempre correlacione os cálculos com o contexto clínico (lactato, perfusão periférica, sinais respiratórios).
