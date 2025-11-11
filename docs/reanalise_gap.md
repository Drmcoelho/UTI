# Reanálise de Cobertura Curricular UTI

## 1. Objetivos e competências declarados
- **Meta geral do programa:** democratizar educação médica em UTI com 100 temas cobrindo teoria, simuladores, casos e exercícios, oferecendo materiais avançados gratuitos para estudantes e profissionais de saúde.【F:README.md†L5-L34】
- **Competências e pré-requisitos para o estudante:** domínio de instalação de Python 3.8+, pip, criação de ambiente virtual e operação do Jupyter Notebook; capacidade de clonar o repositório ou baixar o ZIP para execução local.【F:INICIO_RAPIDO.md†L7-L71】【F:README.md†L90-L115】
- **Habilidades de estudo autônomo esperadas:** seguir plano de estudo sequencial com checkpoints diários, semanais e mensais, combinar notebooks, simuladores, exercícios e flashcards utilizando técnicas como Pomodoro e revisão espaçada.【F:INICIO_RAPIDO.md†L73-L205】

## 2. Catálogo de materiais disponíveis por diretório

### docs/
| Recurso | Conteúdo | Objetivos cobertos |
| --- | --- | --- |
| `GUIA_INTEGRADO.md` | Guia consolidado com entregáveis obrigatórios, fluxo de produção, cadência de revisão e status de cada módulo. | Referência central para acompanhar evolução dos 100 objetivos curriculares.【F:docs/GUIA_INTEGRADO.md†L1-L169】 |
| `TEMPLATE_NOTEBOOK.md` | Estrutura padrão para novos notebooks com checklist, seções obrigatórias e exemplos de código. | Ferramenta para expandir qualquer objetivo da lista principal com consistência pedagógica.【F:docs/TEMPLATE_NOTEBOOK.md†L1-L69】 |
| `mapa_curricular_modulos.md` | Matriz que relaciona módulos 01–03 com teoria, exercícios, casos, notebooks e flashcards correspondentes. | Objetivos 1 (Monitorização invasiva), 20 (SDRA) e 32/40/41 (Choque Séptico) através dos módulos integrados.【F:docs/mapa_curricular_modulos.md†L1-L19】 |
| `modulo_01_monitorizacao_hemodinamica.md` | Plano instrucional para monitorização invasiva com competências, carga horária e critérios de conclusão. | Objetivo 1 – Monitorização Hemodinâmica Invasiva.【F:docs/modulo_01_monitorizacao_hemodinamica.md†L1-L46】 |
| `modulo_02_ventilacao_sdra.md` | Guia completo para ventilação protetora e adjuvantes na SDRA. | Objetivo 20 – SDRA e ventilação mecânica.【F:docs/modulo_02_ventilacao_sdra.md†L1-L44】 |
| `modulo_03_choque_septico.md` | Roteiro para manejo do choque séptico com pacotes terapêuticos e monitorização. | Objetivos 32, 40 e 41 – Choque séptico, sepse grave e campanha de sobrevivência.【F:docs/modulo_03_choque_septico.md†L1-L44】 |
| `index.html` | Site estático com overview do programa, links para módulos ativos e chamada direta para o guia integrado. | Facilita navegação rápida pelos módulos completos e materiais complementares.【F:docs/index.html†L300-L428】 |
| `files/UTI_Mega_Notebook_FINAL.ipynb` | Placeholder legado sem conteúdo publicado. | Reservado para consolidação futura; não cobre objetivos no estado atual.【F:docs/files/UTI_Mega_Notebook_FINAL.ipynb†L1-L1】 |

### notebooks/
| Recurso | Conteúdo | Objetivos cobertos |
| --- | --- | --- |
| `01_monitorizacao_hemodinamica_invasiva.ipynb` | Notebook com teoria, calculadoras de PAM, simulador de curva arterial, exercícios e caso integrado. | Objetivo 1 – Monitorização Hemodinâmica Invasiva.【F:notebooks/README.md†L9-L23】 |
| `20_sdra.ipynb` | Notebook com critérios de Berlim, calculadoras de PBW/VC, simulador de driving pressure e casos. | Objetivo 20 – SDRA.【F:notebooks/README.md†L9-L23】 |
| `21_casos_integrados_choque_sdra.ipynb` | Casos interativos cobrindo checkpoints de monitorização, SDRA e choque séptico. | Integra objetivos 1, 20, 32, 40 e 41 conforme matriz curricular.【F:docs/mapa_curricular_modulos.md†L6-L19】 |
| `README.md` | Guia geral sobre uso dos notebooks e status de desenvolvimento. | Suporte metodológico geral, enfatizando que apenas 3 notebooks estão completos.【F:notebooks/README.md†L1-L29】 |

### flashcards/
| Recurso | Conteúdo | Objetivos cobertos |
| --- | --- | --- |
| `flashcards_temas_01_20_sepse.txt` | Baralho compatível com Anki abordando monitorização, SDRA e sepse/choque. | Objetivos 1, 20, 32, 40 e 41.【F:flashcards/flashcards_temas_01_20_sepse.txt†L1-L40】 |
| `flashcards_modulos_integrados.md` | Tabelas de Q&A para módulos 01–03 alinhados aos objetivos clínicos. | Objetivos 1, 20, 32, 40 e 41 via revisão ativa modular.【F:flashcards/flashcards_modulos_integrados.md†L1-L40】 |

### casos-clinicos/
| Recurso | Conteúdo | Objetivos cobertos |
| --- | --- | --- |
| `caso_01_choque_septico.md` | Caso extenso de choque séptico com pacote de 1h, monitorização e ventilação protetora. | Objetivos 32, 40, 41 com reforço de monitorização (Objetivo 1) e SDRA (Objetivo 20).【F:casos-clinicos/caso_01_choque_septico.md†L1-L104】 |
| `caso_02_monitorizacao_invasiva.md` | Caso focado em indicação, configuração e interpretação de PAI em choque refratário. | Objetivo 1 – Monitorização invasiva.【F:casos-clinicos/caso_02_monitorizacao_invasiva.md†L1-L74】 |
| `caso_03_sdra_refrataria.md` | Caso de SDRA grave com decisões sobre pronação, ΔP e escalonamento. | Objetivo 20 – SDRA (compondo módulo 02).【F:casos-clinicos/caso_03_sdra_refrataria.md†L1-L74】 |

### exercicios/
| Recurso | Conteúdo | Objetivos cobertos |
| --- | --- | --- |
| `exercicios_blocos_1-3.md` | Blocos de múltipla escolha alinhados aos módulos 01–03 com gabaritos comentados. | Objetivos 1, 20, 32/40/41.【F:exercicios/exercicios_blocos_1-3.md†L1-L62】 |

### simuladores/
| Recurso | Conteúdo | Objetivos cobertos |
| --- | --- | --- |
| `README_simulador_noradrenalina.md` | Guia de simuladores de titulação vasoativa (Noradrenalina). | Objetivos 32, 40, 41 (manejo de choque séptico).【F:simuladores/README_simulador_noradrenalina.md†L1-L48】 |
| `quiz_objetivos_modulos.md` | Simulador textual de autoavaliação com cenários para módulos 01–03. | Objetivos 1, 20, 32, 40 e 41.【F:simuladores/quiz_objetivos_modulos.md†L1-L96】 |

### recursos/
| Recurso | Conteúdo | Objetivos cobertos |
| --- | --- | --- |
| `README.md` | Tabelas de drogas vasoativas, parâmetros ventilatórios, gasometria e algoritmos de choque/hipoxemia. | Suporte transversal aos módulos 01–03 (monitorização, SDRA, sepse) e futura expansão. 【F:recursos/README.md†L1-L76】 |

## 3. Análise de lacunas
- **Cobertura principal ainda limitada:** dos 100 temas planejados, apenas os objetivos de monitorização invasiva (1), SDRA (20) e sepse/choque séptico (32, 40, 41) possuem trilha completa com teoria, notebook, caso, exercícios e flashcards; o README reforça que a maioria dos temas segue pendente.【F:README.md†L25-L87】【F:notebooks/README.md†L9-L18】
- **Módulos integrados sem material completo:** embora o `mapa_curricular_modulos.md` liste módulos 01–03 com elementos combinados, não há conteúdos similares para os demais 97 módulos, deixando grande parte da matriz curricular vazia.【F:docs/mapa_curricular_modulos.md†L1-L19】
- **Documentos e arquivos placeholder sem utilização:** `docs/files/UTI_Mega_Notebook_FINAL.ipynb` permanece reservado sem conteúdo, enquanto o site `docs/index.html` já apresenta overview atualizado com links diretos.【F:docs/files/UTI_Mega_Notebook_FINAL.ipynb†L1-L1】【F:docs/index.html†L300-L428】
- **Falta de recursos práticos para outros eixos:** não existem casos clínicos, simuladores ou flashcards cobrindo temas além de monitorização, SDRA e choque séptico, deixando lacunas em emergências neurológicas, distúrbios metabólicos, suporte renal, entre outros listados no README.【F:README.md†L27-L87】【F:flashcards/flashcards_modulos_integrados.md†L1-L40】
- **Escalonamento dependente de novos notebooks:** o template e o novo notebook 21 oferecem estrutura para expansão, mas não há produção iniciada para os demais temas; é necessário priorizar cronograma de criação para atingir metas 2026.【F:docs/TEMPLATE_NOTEBOOK.md†L1-L69】【F:notebooks/README.md†L9-L23】
