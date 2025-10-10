# Recursos - Materiais de Apoio

## 📁 Sobre Esta Pasta

Esta pasta contém recursos visuais e materiais de apoio para os notebooks, incluindo:

- 🖼️ Imagens médicas
- 📊 Diagramas e ilustrações
- 📋 Tabelas de referência rápida
- 🔄 Algoritmos de manejo
- 📝 Protocolos em formato visual
- 🎨 Infográficos educacionais

## 🗂️ Estrutura de Organização

```
recursos/
├── imagens/              # Imagens médicas e ilustrações
│   ├── radiologia/       # RX, TC, RM
│   ├── anatomia/         # Diagramas anatômicos
│   └── procedimentos/    # Fotos de procedimentos
├── tabelas/              # Tabelas de referência
│   ├── farmacos/         # Doses, diluições
│   ├── valores/          # Valores normais
│   └── scores/           # Escores e escalas
├── algoritmos/           # Fluxogramas de decisão
├── protocolos/           # Protocolos institucionais
└── infograficos/         # Infográficos educacionais
```

## 📋 Tabelas de Referência Rápida

### Tabela 1: Vasopressores e Inotrópicos

| Droga | Classe | Dose | Efeito Principal | Indicação |
|-------|--------|------|------------------|-----------|
| Noradrenalina | Vasopr. | 0.05-3.0 mcg/kg/min | ↑ RVS (α1) | Choque séptico, 1ª escolha |
| Vasopressina | Vasopr. | 0.03-0.04 U/min | ↑ RVS (V1) | 2ª droga no choque |
| Dopamina | Vasopr. | 5-20 mcg/kg/min | ↑ RVS e DC | Alternativa (bradicardia) |
| Dobutamina | Inotr. | 2.5-20 mcg/kg/min | ↑ DC (β1) | Disfunção miocárdica |
| Adrenalina | Ambos | 0.05-0.5 mcg/kg/min | ↑ RVS e DC | Choque refratário |
| Milrinona | Inotr. | 0.375-0.75 mcg/kg/min | ↑ DC, ↓ RVS | IC descompensada |

### Tabela 2: Parâmetros Ventilatórios Normais

| Parâmetro | Valor Normal | Unidade |
|-----------|--------------|---------|
| Volume Corrente (VC) | 6-8 | mL/kg PBW |
| Frequência Respiratória (FR) | 12-20 | irpm |
| PEEP | 5-10 | cmH2O |
| FiO2 | 0.21-1.0 | fração |
| Pressão de Platô | < 30 | cmH2O |
| Driving Pressure | < 15 | cmH2O |
| Complacência | 50-100 | mL/cmH2O |
| Resistência | 5-15 | cmH2O/L/s |

### Tabela 3: Gasometria Arterial - Valores Normais

| Parâmetro | Valor Normal | Unidade |
|-----------|--------------|---------|
| pH | 7.35-7.45 | - |
| PaCO2 | 35-45 | mmHg |
| PaO2 | 80-100 | mmHg |
| HCO3 | 22-26 | mEq/L |
| BE | -2 a +2 | mEq/L |
| SatO2 | > 95 | % |
| Lactato | < 2 | mmol/L |

### Tabela 4: Escores Prognósticos

| Escore | Uso | Variáveis | Interpretação |
|--------|-----|-----------|---------------|
| SOFA | Disfunção orgânica | 6 sistemas | 0-24, >2 = sepse |
| APACHE II | Mortalidade UTI | Idade + 12 var. | 0-71, ↑ = ↑ mortalidade |
| SAPS III | Mortalidade hospitalar | 20 variáveis | 0-217, calcula % mort |
| Glasgow | Consciência | 3 domínios | 3-15, <8 = grave |
| RASS | Sedação | Escala -5 a +4 | 0 = alerta e calmo |
| CAM-ICU | Delirium | 4 passos | Positivo = delirium |

### Tabela 5: Antibióticos em UTI - Doses Renais

| Antibiótico | Dose Normal | ClCr 30-50 | ClCr 10-29 | ClCr < 10 |
|-------------|-------------|------------|------------|-----------|
| Meropenem | 1g 8/8h | 1g 12/12h | 500mg 12/12h | 500mg 24/24h |
| Piperacilina-Tazo | 4.5g 6/6h | 4.5g 8/8h | 2.25g 8/8h | 2.25g 12/12h |
| Vancomicina | 15-20mg/kg | Ajustar por nível | Ajustar | Dose de ataque + nível |
| Ceftriaxone | 1-2g 24/24h | Sem ajuste | Sem ajuste | Max 2g/dia |
| Linezolida | 600mg 12/12h | Sem ajuste | Sem ajuste | Sem ajuste |

## 🔄 Algoritmos Disponíveis

### Algoritmo 1: Abordagem do Choque

```
CHOQUE (Hipotensão + Hipoperfusão)
    ↓
Ressuscitação Inicial (30 mL/kg cristaloide)
    ↓
Avaliar Tipo de Choque
    ↓
├─ Distributivo (Séptico) → Noradrenalina
├─ Cardiogênico → Inotrópico + considerar MCS
├─ Hipovolêmico → Fluidos + corrigir sangramento
└─ Obstrutivo → Tratar causa (TEP, tamponamento)
    ↓
Meta PAM ≥ 65 mmHg + Lactato clearance
    ↓
Monitorização Contínua
```

### Algoritmo 2: Abordagem da Hipoxemia

```
Hipoxemia (PaO2 < 60 mmHg ou SpO2 < 90%)
    ↓
Oxigenoterapia
    ↓
Avaliar Resposta
    ↓
├─ Melhora → Manter O2, investigar causa
└─ Sem melhora
    ↓
    Considerar:
    ├─ VNI (se alerta, cooperativo)
    ├─ Alto fluxo
    └─ IOT + VM (se refratário ou critérios)
        ↓
        VM Protetora (6 mL/kg PBW)
        ↓
        Se SDRA grave (PaO2/FiO2 < 150)
        ↓
        Considerar:
        ├─ Posição Prona
        ├─ Bloqueio Neuromuscular
        └─ ECMO (se refratário)
```

### Algoritmo 3: Manejo de SDRA

```
Diagnóstico de SDRA (Critérios de Berlim)
    ↓
Classificar Gravidade (PaO2/FiO2)
    ↓
Ventilação Protetora
├─ VC: 6 mL/kg PBW
├─ Pplat < 30 cmH2O
├─ PEEP conforme FiO2 (tabela ARDSNet)
└─ Hipercapnia permissiva (pH > 7.20)
    ↓
Avaliar Resposta (4-6h)
    ↓
├─ PaO2/FiO2 > 150 → Manter estratégia
└─ PaO2/FiO2 < 150 → Terapias Adjuvantes
    ↓
    Sequência:
    1. Posição Prona (16-18h/dia)
    2. Bloqueio Neuromuscular (48h)
    3. Recrutamento Alveolar (cauteloso)
    4. ECMO (se refratário)
```

## 📖 Protocolos de Referência

### Protocolo 1: Pacote de Sepse (1 hora)

**Objetivos:**
- Implementar medidas salvadoras em sepse/choque séptico
- Reduzir mortalidade com intervenções precoces

**Ações (dentro de 1 hora):**

1. ✅ **Coleta de Culturas**
   - Hemocultura (2 amostras, sítios diferentes)
   - Urocultura
   - Outras conforme foco suspeito
   - ⚠️ ANTES de antibiótico

2. 💊 **Antibiótico Empírico**
   - Amplo espectro
   - Dose plena
   - Via endovenosa
   - Dentro de 1 hora do reconhecimento

3. 💧 **Ressuscitação Volêmica**
   - 30 mL/kg de cristaloide
   - Se hipotensão OU lactato ≥ 4 mmol/L
   - Reavaliar após cada bolus

4. 💉 **Vasopressor**
   - Se hipotensão refratária a fluidos
   - Noradrenalina (1ª escolha)
   - Meta: PAM ≥ 65 mmHg

5. 🔬 **Lactato**
   - Mensurar no início
   - Repetir em 2-4h
   - Meta: redução ≥ 10%

### Protocolo 2: Desmame da Ventilação Mecânica

**Critérios para Teste de Respiração Espontânea (TRE):**

✅ Pré-requisitos:
- [ ] Melhora da causa da IRA
- [ ] PaO2 ≥ 60 mmHg com FiO2 ≤ 40% e PEEP ≤ 8
- [ ] Hemodinamicamente estável (sem/com doses baixas de vasoativo)
- [ ] Capaz de iniciar esforço respiratório
- [ ] Sem sedação contínua (RASS -1 a +1)
- [ ] Sem bloqueio neuromuscular

**Execução do TRE:**
1. Explicar ao paciente
2. Modo PSV 5-7 cmH2O ou Tubo-T
3. Duração: 30-120 minutos
4. Monitorização contínua

**Critérios de Falha (suspender TRE):**
- FR > 35 irpm ou < 8 irpm
- SpO2 < 90%
- FC > 140 bpm ou ↑ > 20%
- PAS > 180 ou < 90 mmHg
- Ansiedade, sudorese, rebaixamento
- Arritmias

**Se sucesso:** Extubar
**Se falha:** Retornar VM, investigar causa, novo TRE em 24h

## 🎨 Infográficos

### Infográfico 1: "Choque em 5 Minutos"
- Definição visual
- 4 tipos de choque
- Tratamento específico de cada

### Infográfico 2: "SDRA - Do Diagnóstico ao Tratamento"
- Critérios de Berlim ilustrados
- Ventilação protetora em passos
- Quando usar prona

### Infográfico 3: "Vasopressores - Guia Visual"
- Mecanismo de ação
- Doses práticas
- Quando usar cada um

## 📥 Como Usar os Recursos

### Em Notebooks
```python
from IPython.display import Image, display

# Exibir imagem
display(Image('recursos/imagens/algoritmo_choque.png'))
```

### Em Markdown
```markdown
![Descrição da imagem](recursos/imagens/nome_arquivo.png)
```

### Tabelas em DataFrames
```python
import pandas as pd

# Carregar tabela
df = pd.read_csv('recursos/tabelas/vasopressores.csv')
display(df)
```

## 🤝 Contribuindo com Recursos

### Adicionando Imagens
1. Certifique-se de ter direitos de uso
2. Use formatos: PNG, JPG, SVG
3. Otimize tamanho (< 1MB quando possível)
4. Nomeie descritivamente: `tema_descricao.png`

### Adicionando Tabelas
1. Formato CSV ou Excel
2. UTF-8 encoding
3. Cabeçalhos claros
4. Dados validados

### Adicionando Algoritmos
1. Formato Mermaid (preferencial) ou PNG
2. Legível e claro
3. Baseado em guidelines
4. Referências citadas

## 📚 Fontes e Referências

Todos os recursos devem ter:
- **Fonte clara**
- **Licença apropriada**
- **Referência bibliográfica**
- **Data de atualização**

## ⚖️ Licenciamento

Recursos devem ter licenças compatíveis com uso educacional:
- Creative Commons (CC-BY, CC-BY-SA)
- Domínio público
- Uso autorizado por autor/instituição

⚠️ **Nunca use materiais sem permissão ou com copyright restritivo**

## 📞 Suporte

Dúvidas sobre recursos?
- Abra uma Issue
- Marque com tag `recursos`

---

**Atualizado em: 2025-10-10**
