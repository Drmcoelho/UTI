# Simulador — Módulo 05 (Oximetria e Capnografia)

Este simulador integra interpretação de SpO₂, índice de perfusão e capnografia, utilizando limites padronizados em [`recursos/05_oximetria_capnografia/alarmes_padrao.csv`](../recursos/05_oximetria_capnografia/alarmes_padrao.csv).

## 🚀 Como executar

```bash
python -i simuladores/modulo_05_oximetria_capnografia.py
```

## 🔧 Funções principais

| Função | Descrição | Exemplo |
| --- | --- | --- |
| `avaliar_oximetria(spo2, indice_perfusao)` | Analisa qualidade da oximetria e confiabilidade do PI. | `avaliar_oximetria(89, 0.4)` |
| `calcular_gradiente_co2(etco2, paco2)` | Calcula gradiente ETCO₂-PaCO₂ e fornece alerta. | `calcular_gradiente_co2(32, 44)` |
| `interpretar_capnograma(retorno_base, formato_plato, co2_inspiratorio)` | Sugere diagnósticos conforme morfologia da curva. | `interpretar_capnograma(False, "platô plano", 4)` |
| `avaliar_tendencia_etco2([valores])` | Detecta tendência crescente ou decrescente de ETCO₂. | `avaliar_tendencia_etco2([12, 14, 18, 22])` |
| `carregar_alarmes()` | Retorna limites recomendados para alarmes. | `carregar_alarmes()["SpO2"]` |

## 🧪 Exemplo de fluxo

```python
from simuladores import modulo_05_oximetria_capnografia as oxicap

alarmes = oxicap.carregar_alarmes()
print(alarmes["ETCO2"].recomendacao)
print(oxicap.avaliar_oximetria(93, 1.2))
print(oxicap.calcular_gradiente_co2(38, 45))
print(oxicap.interpretar_capnograma(retorno_base=False, formato_plato="dente de tubarão", co2_inspiratorio=2))
print(oxicap.avaliar_tendencia_etco2([18, 20, 24, 28]))
```

## ✅ Boas práticas

- Combine a leitura de SpO₂ com PI para assegurar confiabilidade, especialmente em pacientes com vasoconstrição periférica.
- Utilize a análise de tendência de ETCO₂ durante RCP ou sedação prolongada para ajustar compressões e ventilação.
- Registre gradiente ETCO₂-PaCO₂ sempre que gasometrias forem coletadas para monitorar evolução do espaço morto.
