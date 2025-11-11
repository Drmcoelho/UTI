# Caso Clínico 03 — Cateter de Artéria Pulmonar em Choque Cardiogênico

> **Integração curricular:**
> - Notebook principal: [`03_cateter_arteria_pulmonar.ipynb`](../notebooks/03_cateter_arteria_pulmonar.ipynb)
> - Exercícios: [Bloco 3](../exercicios/exercicios_blocos_1-3.md#-bloco-3-cateter-de-arteria-pulmonar)
> - Simulador complementar: [`simuladores/modulo_03_cateter_arteria_pulmonar.py`](../simuladores/modulo_03_cateter_arteria_pulmonar.py)

## 📋 Apresentação do caso

- **Paciente:** L.P.A., 59 anos, masculino
- **Diagnóstico de base:** infarto agudo do miocárdio com supra de parede anterior tratado com angioplastia há 24h
- **Motivo da monitorização:** choque cardiogênico com instabilidade refratária apesar de suporte vasoativo

### Dados iniciais

| Variável | Valor |
| --- | --- |
| Pressão arterial invasiva | 86/52 mmHg (PAM 63 mmHg) |
| Frequência cardíaca | 112 bpm |
| Lactato | 3,9 mmol/L |
| Saturação venosa central | 55% |
| Noradrenalina | 0,28 mcg/kg/min |
| Dobutamina | 5 mcg/kg/min |

A equipe decide posicionar cateter de artéria pulmonar (CAP) para guiar suporte avançado.

## ❓ Perguntas para discussão

### 1. Indicação e preparo

Quais são as indicações formais de CAP neste paciente e quais exames devem ser revisados antes do procedimento?

<details>
<summary>Discussão guiada</summary>

- Choque cardiogênico com necessidade de diferenciar componente distributivo ou hipovolêmico.
- Avaliação seriada de pressões de enchimento (PAD, PCP) e débito cardíaco.
- Necessário revisar coagulograma, eletrólitos, função renal e Rx de tórax prévio.
- Planejar sedação leve, analgesia e ultrassom para acesso venoso.
</details>

### 2. Interpretação das pressões

Após inserção, os valores são:

- Pressão de átrio direito (PAD): 18 mmHg
- Pressão arterial pulmonar (PAP): 42/26 mmHg (média 31)
- Pressão capilar pulmonar (PCP): 28 mmHg
- Débito cardíaco (termodiluição): 3,0 L/min

Calcule o índice cardíaco considerando superfície corporal 1,9 m² e interprete o fenótipo hemodinâmico.

<details>
<summary>Discussão guiada</summary>

- Índice cardíaco (IC) = 3,0 / 1,9 ≈ 1,58 L/min/m² (baixo).
- PCP elevada → congestão pulmonar significativa.
- Fenótipo: choque cardiogênico puro, sem evidência de componente distributivo.
</details>

### 3. Resistências vasculares

Utilize os dados para calcular resistência vascular sistêmica (RVS) e resistência vascular pulmonar (RVP). Considere PAM 63 mmHg e PVC aproximada à PAD.

<details>
<summary>Discussão guiada</summary>

- RVS = 80 × (PAM − PVC) / DC = 80 × (63 − 18) / 3 ≈ 1.200 dyn·s·cm⁻⁵ (elevada).
- RVP = 80 × (PAPm − PCP) / DC = 80 × (31 − 28) / 3 ≈ 80 dyn·s·cm⁻⁵ (normal).
- Interpretação: vasoconstrição sistêmica secundária a choque, pulmão sem vasoconstrição importante.
</details>

### 4. Plano terapêutico guiado pelo CAP

Quais ajustes imediatos você sugeriria com base no fenótipo acima?

<details>
<summary>Discussão guiada</summary>

- Otimizar inotrópico: elevar dobutamina (até 10 mcg/kg/min) e considerar milrinona se pressão permitir.
- Avaliar suporte mecânico (balão intra-aórtico) se não houver resposta.
- Ajustar vasopressor visando PAM 65-70 mmHg, evitando excesso que aumente pós-carga.
- Diurese agressiva ou ultrafiltração se congestão refratária.
</details>

### 5. Seguimento

Quais parâmetros devem ser monitorados nas próximas 24 horas e quais critérios determinam retirada do cateter?

<details>
<summary>Discussão guiada</summary>

- Registrar séries de PAP, PCP, IC e saturação venosa mista (SvO₂) a cada 4-6 horas.
- Avaliar tendência de lactato e clearance de creatinina.
- Retirar CAP quando: estabilidade hemodinâmica > 24h, IC > 2,2 L/min/m² e vasopressores mínimos.
</details>

## ✅ Checklist de aprendizado

- [ ] Indicações precisas de CAP em choque cardiogênico.
- [ ] Cálculo de IC, RVS e RVP a partir de dados invasivos.
- [ ] Integração de medidas hemodinâmicas ao plano terapêutico.
- [ ] Critérios objetivos para retirada segura do cateter.

> 📌 **Próximo passo:** consulte os esquemas visuais em [`recursos/03_cateter_arteria_pulmonar/zonas_wedge.md`](../recursos/03_cateter_arteria_pulmonar/zonas_wedge.md) antes de treinar a interpretação de curvas no simulador.
