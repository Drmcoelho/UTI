# 📘 Guia Integrado do Programa UTI 360

Este documento consolida visão geral, governança e progresso curricular em um único ponto de verdade.

## 🎯 Propósito

- Oferecer uma trilha completa em terapia intensiva com 100 módulos temáticos.
- Garantir consistência entre notebooks, casos clínicos, exercícios, simuladores e materiais de beira-leito.
- Documentar responsabilidades, fluxos de revisão e estado de entrega em um único arquivo.

## 🧱 Entregáveis Obrigatórios por Módulo

Cada módulo deve contemplar os seguintes componentes mínimos:

- 📓 Notebook teórico-prático (`notebooks/NN_tema.ipynb`).
- 🩺 Casos clínicos aplicados (`casos-clinicos/caso_NN_*.md`).
- 🧠 Flashcards em formato Anki (`flashcards/NN_tema.txt`).
- 🎯 Lista de exercícios com gabarito (`exercicios/NN_*.md`) — cada módulo possui 3 questões dissertativas, 8 MCQ interativas (5 alternativas) e 15 V/F com justificativa.
- 🕹️ Simuladores interativos (`simuladores/NN_*.md` ou apps).
- 🧪 Testes automatizados de consistência (`tests/test_modulo_NN.py`).
- 📁 Recursos visuais e tabelas (`recursos/NN/`).
- 📱 Script pronto para uso no Scriptable (`scriptable/NN_tema.js`).

## 🔁 Fluxo de Produção e Revisão

1. **Design curricular:** selecionar objetivos de aprendizagem e referências primárias.
2. **Construção do notebook:** estruturar teoria, algoritmos, simuladores e links para materiais complementares.
3. **Integração clínica:** escrever casos clínicos vinculados ao notebook e às checklists operacionais.
4. **Memorização ativa:** derivar flashcards e exercícios com base nos pontos críticos do módulo.
5. **Validação técnica:** criar testes automatizados que verifiquem cálculos, tabelas de parâmetros e integridade dos dados.
6. **Disponibilização beira-leito:** publicar script Scriptable e material de bolso no diretório `recursos/`.
7. **Revisão editorial:** aplicar checklist trimestral, registrar alterações e atualizar esta tabela de progresso.

## 🗓️ Cadência de Revisão

- **Trimestral (jan/abr/jul/out):** verificação de evidências científicas, atualização de protocolos e testes automatizados.
- **Mensal:** auditoria rápida do site (`docs/index.html`) e dos links internos.
- **A cada novo módulo:** rodar suíte de testes (`pytest`) e atualizar o inventário de progresso abaixo.

## 📊 Progresso dos 100 Módulos

|Módulo|Tema|Notebook|Casos|Flashcards|Exercícios|Simuladores|Testes|Recursos|Scriptable JS|
|---|---|---|---|---|---|---|---|---|---|
|1|Monitorização Hemodinâmica Invasiva|✅|✅|✅|✅|✅|✅|✅|✅|
|2|Monitorização Hemodinâmica Não-Invasiva|✅|✅|✅|✅|✅|✅|✅|✅|
|3|Cateter de Artéria Pulmonar (Swan-Ganz)|✅|✅|✅|✅|✅|✅|✅|✅|
|4|Ecocardiografia à Beira do Leito (Point-of-Care)|✅|✅|✅|✅|✅|✅|✅|✅|
|5|Oximetria e Capnografia|✅|✅|✅|✅|✅|✅|✅|✅|
|6|Monitorização da Pressão Intracraniana (PIC)|✅|✅|✅|✅|✅|✅|✅|✅|
|7|Acesso Venoso Central|✅|✅|✅|✅|✅|✅|✅|✅|
|8|Acesso Arterial|✅|✅|✅|✅|✅|✅|✅|✅|
|9|Balanço Hídrico e Controle de Volemia|✅|✅|✅|✅|✅|✅|✅|✅|
|10|Nutrição Enteral em Pacientes Críticos|✅|✅|✅|✅|✅|✅|✅|✅|
|11|Nutrição Parenteral em UTI|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|12|Controle Glicêmico em Pacientes Críticos|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|13|Sedação e Analgesia em UTI|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|14|Bloqueio Neuromuscular|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|15|Delirium em UTI: Diagnóstico e Manejo|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|16|Ventilação Mecânica Invasiva: Princípios Básicos|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|17|Modos Ventilatórios: Volume vs Pressão|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|18|PEEP (Positive End-Expiratory Pressure)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|19|Ventilação Protetora (ARDSNet)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|20|Síndrome do Desconforto Respiratório Agudo (SDRA)|✅|✅|✅|⬜️|✅|⬜️|✅|⬜️|
|21|Ventilação Não-Invasiva (VNI)|✅|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|22|Desmame da Ventilação Mecânica|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|23|Oxigenoterapia de Alto Fluxo (High Flow)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|24|Traqueostomia em UTI|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|25|Posição Prona em SDRA|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|26|Manobras de Recrutamento Alveolar|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|27|ECMO (Oxigenação por Membrana Extracorpórea)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|28|Pneumonia Associada à Ventilação (PAV)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|29|Asma Grave e Estado de Mal Asmático|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|30|DPOC Exacerbado em UTI|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|31|Choque: Classificação e Abordagem Inicial|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|32|Choque Séptico: Definição e Manejo|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|33|Choque Cardiogênico|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|34|Choque Hipovolêmico|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|35|Choque Distributivo|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|36|Choque Obstrutivo|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|37|Ressuscitação Volêmica: Cristaloides vs Coloides|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|38|Vasopressores: Noradrenalina, Vasopressina, Dopamina|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|39|Inotrópicos: Dobutamina, Milrinona|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|40|Sepse e Sepse Grave: Critérios Diagnósticos|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|41|Campanha de Sobrevivência à Sepse (Surviving Sepsis)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|42|Disfunção Miocárdica Induzida por Sepse|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|43|Coagulação Intravascular Disseminada (CIVD)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|44|Síndrome da Resposta Inflamatória Sistêmica (SIRS)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|45|Lactato como Marcador de Perfusão Tecidual|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|46|Infarto Agudo do Miocárdio com Supradesnivelamento de ST|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|47|Síndrome Coronariana Aguda sem Supradesnivelamento de ST|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|48|Edema Agudo de Pulmão Cardiogênico|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|49|Insuficiência Cardíaca Aguda|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|50|Arritmias em Pacientes Críticos|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|51|Fibrilação Atrial de Alta Resposta|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|52|Taquicardia Ventricular e Fibrilação Ventricular|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|53|Bradiarritmias e Bloqueios AV|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|54|Tamponamento Cardíaco|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|55|Parada Cardiorrespiratória (PCR) e RCP Avançado|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|56|Cuidados Pós-PCR|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|57|Embolia Pulmonar Aguda|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|58|Trombólise em Emergências|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|59|Dissecção Aórtica|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|60|Hipertensão Maligna|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|61|Acidente Vascular Cerebral Isquêmico (AVCi)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|62|Acidente Vascular Cerebral Hemorrágico (AVCh)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|63|Hemorragia Subaracnóidea (HSA)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|64|Traumatismo Cranioencefálico (TCE) Grave|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|65|Status Epilepticus|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|66|Síndrome de Guillain-Barré|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|67|Miastenia Gravis em Crise|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|68|Meningite Bacteriana em UTI|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|69|Encefalite Viral|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|70|Morte Encefálica: Diagnóstico|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|71|Hipertensão Intracraniana|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|72|Herniação Cerebral|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|73|Neuropatia do Paciente Crítico|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|74|Miopatia do Paciente Crítico|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|75|Coma: Avaliação e Manejo|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|76|Injúria Renal Aguda (IRA): Classificação KDIGO|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|77|Terapia de Substituição Renal (TSR)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|78|Hemodiálise em Pacientes Críticos|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|79|Acidose Metabólica|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|80|Alcalose Metabólica|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|81|Acidose Respiratória|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|82|Alcalose Respiratória|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|83|Distúrbios de Sódio: Hiponatremia|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|84|Distúrbios de Sódio: Hipernatremia|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|85|Distúrbios de Potássio: Hipocalemia|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|86|Distúrbios de Potássio: Hipercalemia|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|87|Hipercalcemia em Pacientes Críticos|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|88|Hipofosfatemia|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|89|Cetoacidose Diabética (CAD)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|90|Estado Hiperglicêmico Hiperosmolar (EHH)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|91|Trauma Grave: Abordagem Inicial (ATLS)|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|92|Queimaduras Graves|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|93|Intoxicações Exógenas em UTI|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|94|Anafilaxia e Reações Alérgicas Graves|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|95|Síndrome Compartimental Abdominal|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|96|Pancreatite Aguda Grave|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|97|Hemorragia Digestiva Alta|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|98|Insuficiência Hepática Aguda|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|99|Gestante Crítica em UTI|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|
|100|Ética e Cuidados Paliativos em UTI|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|⬜️|

Legenda: `✅` entregue · `⬜️` pendente.

## 🤝 Governança e Contribuição

- Use issues com etiquetas `modulo-NN` para propor melhorias específicas.
- Pull requests devem atualizar o notebook correspondente **e** os materiais complementares antes de serem aprovados.
- Atualize esta tabela sempre que um deliverable for concluído para evitar divergências.

## 🌐 Publicação

- GitHub Pages: configure a branch principal e a pasta `/docs` para publicação automática.
- Render: utilize `render.yaml` (start command `python -m http.server --directory docs $PORT`).

## 🧭 Navegação Essencial

- [`README.md`](../README.md): visão geral e lista dos 100 temas.
- [`docs/index.html`](index.html): site estático para consulta rápida.
- [`notebooks/`](../notebooks/): notebooks por tema.
- [`casos-clinicos/`](../casos-clinicos/): casos clínicos integrados.
- [`flashcards/`](../flashcards/): arquivos para Anki.
- [`simuladores/`](../simuladores/): guias de simuladores.
- [`scriptable/`](../scriptable/): scripts prontos para o app Scriptable.

---

Este guia substitui os antigos arquivos `RESUMO_PROJETO.md`, `GUIA_DE_USO.md` e `REVIEW_CADENCE.md`, consolidando as informações em um único documento de referência.
