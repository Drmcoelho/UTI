# UTI - Educação Médica Gratuita

## 📚 Sobre o Projeto

Repositório público gratuito dedicado à educação médica em Unidade de Terapia Intensiva (UTI) para estudantes de medicina. O projeto oferece conteúdo de nível avançado com múltiplas ferramentas de aprendizado, reunidas e acompanhadas pelo [`docs/GUIA_INTEGRADO.md`](docs/GUIA_INTEGRADO.md), o ponto único de verdade do programa.

As frentes educacionais previstas contemplam:

- 🎯 **100 Temas Fundamentais** de UTI
- 📝 **Jupyter Notebooks Interativos** para cada tema
- 🧠 **Flashcards** e recursos de memorização
- 📊 **Tabelas, Mindmaps e Flowcharts** (Mermaid)
- 💊 **Casos Clínicos** detalhados
- 🎮 **Simuladores** interativos
- ❓ **Exercícios** em múltiplos formatos
- 📖 **Teoria Robusta** e atualizada
- 📱 **Scripts Scriptable** para apoio beira-leito

## 📈 Estado Atual de Entrega

- ✅ **Notebooks publicados:** 10 de 100 (módulos 01 a 10, 20 e 21).
- ✅ **Casos clínicos:** trilha completa para os módulos 01 a 10.
- ✅ **Flashcards:** conjuntos individuais para módulos 01 a 10 em formato Anki.
- ✅ **Exercícios:** bancos completos com 3 dissertativas, 8 MCQ interativas e 15 V/F para os módulos 01 a 10.
- ✅ **Simuladores:** scripts Python dedicados aos módulos 01 a 10.
- ✅ **Scriptable:** widgets prontos para uso beira-leito nos módulos 01 a 10.
- ✅ **Testes automatizados:** suíte cobre simuladores e integridade das questões dos módulos 01 a 10.
- ⏳ **Demais módulos:** acompanhados pela tabela de progresso central em [`docs/GUIA_INTEGRADO.md`](docs/GUIA_INTEGRADO.md).

## 🗂️ Estrutura do Projeto

```
UTI/
├── notebooks/          # Notebooks de cada tema
├── casos-clinicos/     # Casos clínicos práticos
├── exercicios/         # Exercícios e questões
├── flashcards/         # Flashcards por tema
├── simuladores/        # Ferramentas interativas
├── recursos/           # Imagens, diagramas e tabelas
└── docs/              # Documentação adicional
```

## 📋 100 Temas de UTI

### Monitorização e Suporte Básico (1-15)
1. Monitorização Hemodinâmica Invasiva
2. Monitorização Hemodinâmica Não-Invasiva
3. Cateter de Artéria Pulmonar (Swan-Ganz)
4. Ecocardiografia à Beira do Leito (Point-of-Care)
5. Oximetria e Capnografia
6. Monitorização da Pressão Intracraniana (PIC)
7. Acesso Venoso Central
8. Acesso Arterial
9. Balanço Hídrico e Controle de Volemia
10. Nutrição Enteral em Pacientes Críticos
11. Nutrição Parenteral em UTI
12. Controle Glicêmico em Pacientes Críticos
13. Sedação e Analgesia em UTI
14. Bloqueio Neuromuscular
15. Delirium em UTI: Diagnóstico e Manejo

### Suporte Respiratório (16-30)
16. Ventilação Mecânica Invasiva: Princípios Básicos
17. Modos Ventilatórios: Volume vs Pressão
18. PEEP (Positive End-Expiratory Pressure)
19. Ventilação Protetora (ARDSNet)
20. Síndrome do Desconforto Respiratório Agudo (SDRA)
21. Ventilação Não-Invasiva (VNI)
22. Desmame da Ventilação Mecânica
23. Oxigenoterapia de Alto Fluxo (High Flow)
24. Traqueostomia em UTI
25. Posição Prona em SDRA
26. Manobras de Recrutamento Alveolar
27. ECMO (Oxigenação por Membrana Extracorpórea)
28. Pneumonia Associada à Ventilação (PAV)
29. Asma Grave e Estado de Mal Asmático
30. DPOC Exacerbado em UTI

### Choque e Instabilidade Hemodinâmica (31-45)
31. Choque: Classificação e Abordagem Inicial
32. Choque Séptico: Definição e Manejo
33. Choque Cardiogênico
34. Choque Hipovolêmico
35. Choque Distributivo
36. Choque Obstrutivo
37. Ressuscitação Volêmica: Cristaloides vs Coloides
38. Vasopressores: Noradrenalina, Vasopressina, Dopamina
39. Inotrópicos: Dobutamina, Milrinona
40. Sepse e Sepse Grave: Critérios Diagnósticos
41. Campanha de Sobrevivência à Sepse (Surviving Sepsis)
42. Disfunção Miocárdica Induzida por Sepse
43. Coagulação Intravascular Disseminada (CIVD)
44. Síndrome da Resposta Inflamatória Sistêmica (SIRS)
45. Lactato como Marcador de Perfusão Tecidual

### Emergências Cardiovasculares (46-60)
46. Infarto Agudo do Miocárdio com Supradesnivelamento de ST
47. Síndrome Coronariana Aguda sem Supradesnivelamento de ST
48. Edema Agudo de Pulmão Cardiogênico
49. Insuficiência Cardíaca Aguda
50. Arritmias em Pacientes Críticos
51. Fibrilação Atrial de Alta Resposta
52. Taquicardia Ventricular e Fibrilação Ventricular
53. Bradiarritmias e Bloqueios AV
54. Tamponamento Cardíaco
55. Parada Cardiorrespiratória (PCR) e RCP Avançado
56. Cuidados Pós-PCR
57. Embolia Pulmonar Aguda
58. Trombólise em Emergências
59. Dissecção Aórtica
60. Hipertensão Maligna

### Emergências Neurológicas (61-75)
61. Acidente Vascular Cerebral Isquêmico (AVCi)
62. Acidente Vascular Cerebral Hemorrágico (AVCh)
63. Hemorragia Subaracnóidea (HSA)
64. Traumatismo Cranioencefálico (TCE) Grave
65. Status Epilepticus
66. Síndrome de Guillain-Barré
67. Miastenia Gravis em Crise
68. Meningite Bacteriana em UTI
69. Encefalite Viral
70. Morte Encefálica: Diagnóstico
71. Hipertensão Intracraniana
72. Herniação Cerebral
73. Neuropatia do Paciente Crítico
74. Miopatia do Paciente Crítico
75. Coma: Avaliação e Manejo

### Emergências Renais e Metabólicas (76-90)
76. Injúria Renal Aguda (IRA): Classificação KDIGO
77. Terapia de Substituição Renal (TSR)
78. Hemodiálise em Pacientes Críticos
79. Acidose Metabólica
80. Alcalose Metabólica
81. Acidose Respiratória
82. Alcalose Respiratória
83. Distúrbios de Sódio: Hiponatremia
84. Distúrbios de Sódio: Hipernatremia
85. Distúrbios de Potássio: Hipocalemia
86. Distúrbios de Potássio: Hipercalemia
87. Hipercalcemia em Pacientes Críticos
88. Hipofosfatemia
89. Cetoacidose Diabética (CAD)
90. Estado Hiperglicêmico Hiperosmolar (EHH)

### Tópicos Especiais (91-100)
91. Trauma Grave: Abordagem Inicial (ATLS)
92. Queimaduras Graves
93. Intoxicações Exógenas em UTI
94. Anafilaxia e Reações Alérgicas Graves
95. Síndrome Compartimental Abdominal
96. Pancreatite Aguda Grave
97. Hemorragia Digestiva Alta
98. Insuficiência Hepática Aguda
99. Gestante Crítica em UTI
100. Ética e Cuidados Paliativos em UTI

## 🚀 Como Usar

### Pré-requisitos
```bash
# Instalar Python 3.8+
# Instalar Jupyter
pip install jupyter notebook

# Instalar dependências
pip install -r requirements.txt
```

### Executar Notebooks
```bash
jupyter notebook
# Navegue até notebooks/ e abra o tema desejado
```

## 🔄 Revisão Contínua do Conteúdo

- Revisamos todos os materiais trimestralmente, guiados por indicadores de aprendizagem e novas evidências clínicas.
- A cadência oficial, checklists e responsabilidades estão consolidados em [`docs/GUIA_INTEGRADO.md`](docs/GUIA_INTEGRADO.md).
- Sugestões de atualização podem ser enviadas via issues marcadas com a etiqueta `review-qX` correspondente ao trimestre.

## 📚 Recursos por Tema

Cada módulo deve conter, no mínimo, os componentes abaixo. O status consolidado encontra-se no [`docs/GUIA_INTEGRADO.md`](docs/GUIA_INTEGRADO.md).

1. **Notebook Interativo** (`notebooks/NN_tema.ipynb`)
   - Teoria estruturada
   - Diagramas Mermaid
   - Cálculos automatizados
   - Exemplos práticos

2. **Casos Clínicos Aplicados** (`casos-clinicos/caso_NN_*.md`)
   - Apresentação do cenário
   - Perguntas norteadoras
   - Discussão guiada

3. **Flashcards** (`flashcards/NN_tema.txt`)
   - Revisão espaçada
   - Conceitos-chave
   - Tags para filtragem

4. **Exercícios** (`exercicios/NN_*.md`)
   - Questões objetivas
   - Estudos de caso
   - Gabarito comentado

5. **Simuladores** (`simuladores/NN_*.md` ou apps dedicados)
   - Parâmetros configuráveis
   - Feedback em tempo real

6. **Recursos Visuais** (`recursos/NN/`)
   - Tabelas de referência
   - Flowcharts
   - Mind maps conceituais

7. **Scriptable JS** (`scriptable/NN_tema.js`)
   - Script pronto para uso no iOS
   - Entrada rápida de parâmetros clínicos

## 🌐 Publicação

### GitHub Pages

1. Acesse as configurações do repositório na aba **Pages**.
2. Defina a branch principal e a pasta `/docs` como fonte.
3. Após salvar, o site será disponibilizado no domínio `<usuario>.github.io/<repositorio>`.

### Deploy na Render

Para colocar o site no ar com o conteúdo estático hospedado em `docs/`, utilize o manifesto `render.yaml` incluído neste repositório.

1. Crie um serviço *Web Service* na Render apontando para este repositório.
2. Na etapa de build, confirme que o campo **Build Command** está definido como `pip install -r requirements.txt`.
3. Em **Start Command**, informe `python -m http.server --directory docs $PORT` para servir diretamente a homepage `docs/index.html`.
4. Defina a variável de ambiente `PYTHON_VERSION` (ex.: `3.11.5`) e mantenha o plano *Free* ou equivalente.
5. Após o deploy inicial, valide o healthcheck acessando `https://<seu-servico>.onrender.com/`.

Alternativamente, é possível aplicar o manifesto via CLI com `render.yaml`, garantindo que futuras alterações no repositório atualizem automaticamente o serviço (`autoDeploy: true`).

## 🤝 Como Contribuir

Este é um projeto de código aberto! Contribuições são muito bem-vindas:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovoTema`)
3. Commit suas mudanças (`git commit -m 'Adiciona novo conteúdo'`)
4. Push para a branch (`git push origin feature/NovoTema`)
5. Abra um Pull Request

### Diretrizes de Contribuição

- Mantenha conteúdo baseado em evidências
- Cite referências científicas
- Use linguagem clara e acessível
- Inclua exemplos práticos
- Teste código antes de submeter

## 📖 Referências e Bibliografia

O conteúdo é baseado em:
- Guidelines internacionais (AHA, ESC, ERC, etc.)
- Livros-texto de Medicina Intensiva
- Artigos científicos peer-reviewed
- Protocolos institucionais reconhecidos

## 📝 Licença

Este projeto é distribuído sob licença MIT - veja LICENSE para detalhes.

## ⚠️ Aviso Importante

Este material é para fins educacionais. Não substitui:
- Supervisão clínica adequada
- Julgamento médico individualizado  
- Protocolos institucionais locais
- Atualização profissional contínua

## 📧 Contato

Para dúvidas, sugestões ou colaborações, abra uma issue no repositório.

## 🌟 Apoie o Projeto

Se este projeto ajudou você, considere:
- ⭐ Dar uma estrela no repositório
- 📢 Compartilhar com colegas
- 🤝 Contribuir com conteúdo
- 📝 Reportar erros ou melhorias

---

**Desenvolvido com ❤️ para estudantes de medicina**