# Caso Clínico 05 — Integração de Oximetria e Capnografia na Sedação Profunda

> **Integração curricular:**
> - Notebook: `05_oximetria_capnografia.ipynb`
> - Exercícios: [`exercicios/modulo_05_oximetria_capnografia.md`](../exercicios/modulo_05_oximetria_capnografia.md)
> - Simulador: [`simuladores/modulo_05_oximetria_capnografia.py`](../simuladores/modulo_05_oximetria_capnografia.py)

## 📋 Apresentação do caso

- **Paciente:** G.B.S., 72 anos, masculino
- **Diagnóstico de base:** DPOC GOLD IV, hipertensão arterial sistêmica
- **Motivo da sedação:** broncoscopia terapêutica para retirada de tampão mucoso

Procedimento ocorre em sala de endoscopia com sedação profunda (propofol + remifentanil) e VNI transoperatória.

### Monitorização inicial

| Parâmetro | Valor |
| --- | --- |
| SpO₂ | 95% com O₂ suplementar 4 L/min |
| Índice de perfusão | 1,2% |
| ETCO₂ (capnografia nasal adaptada à VNI) | 34 mmHg |
| Frequência respiratória | 18 irpm |

Após 8 minutos, a SpO₂ cai para 89%, ETCO₂ sobe para 48 mmHg e curva capnográfica apresenta retorno incompleto à linha de base.

## ❓ Perguntas para discussão

### 1. Análise imediata

- Quais hipóteses explicam a queda de SpO₂ e o aumento de ETCO₂?
- Como diferenciar hipoventilação de reinalação de CO₂?

<details>
<summary>Discussão guiada</summary>

- Hipoventilação (sedação profunda, obstrução parcial), reinalação (filtros saturados), retenção de CO₂ por espaço morto da VNI, deslocamento da cânula.
- Reinalação gera curva com fase inspiratória acima de zero; hipoventilação mantém retorno a zero porém com platô elevado. Avaliar CO₂ inspiratório e inspeção do circuito.
</details>

### 2. Intervenção baseada em monitorização integrada

A equipe ajusta VNI (aumenta EPAP de 6 → 8 cmH₂O, IPAP de 16 → 20 cmH₂O) e aplica ventilação assistida manual. ETCO₂ reduz para 40 mmHg e SpO₂ sobe a 94%.

- Quais indicadores confirmam resolução adequada?
- O que deve permanecer em vigilância para evitar nova deterioração?

<details>
<summary>Discussão guiada</summary>

- Normalização de ETCO₂, retomada da SpO₂ ≥ 94% e curva com retorno à linha de base confirmam sucesso. Manter índice de perfusão > 1% e observar padrão respiratório.
- Vigiar sedação (nível Ramsay), posicionamento da cânula nasal, filtros da VNI e balanço de fluidos.
</details>

### 3. Pós-procedimento

Durante a recuperação, SpO₂ mantém 93-94%, ETCO₂ 36 mmHg, PI 1,5%.

- Quais registros são obrigatórios na evolução?
- Como instruir a equipe para monitorização contínua nas primeiras horas?

<details>
<summary>Discussão guiada</summary>

- Registrar parâmetros (SpO₂, ETCO₂, PI), intervenções realizadas, ajustes ventilatórios e resposta clínica. Destacar alarmes configurados e plano de vigilância.
- Orientar enfermagem a manter capnografia nasal, conferir linha de amostragem, checar PI e reavaliar a cada 15 minutos na primeira hora.
</details>

## ✅ Checklist de aprendizado

- [ ] Configurar alarmes e limites de SpO₂/ETCO₂ antes da sedação profunda.
- [ ] Interpretar curvas capnográficas e índice de perfusão para guiar intervenção rápida.
- [ ] Documentar respostas terapêuticas e planejar vigilância pós-procedimento.

> 📌 **Próximo passo:** utilize [`recursos/05_oximetria_capnografia/`](../recursos/05_oximetria_capnografia/) para revisar alarmes padronizados e padrões de curva.
