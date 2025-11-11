# 🚀 Guia de Início Rápido - UTI

## 👋 Bem-vindo ao Repositório UTI!

Este guia vai te ajudar a começar em **5 minutos**.

## 📋 Pré-requisitos

Você precisa ter instalado:
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Verificar Instalações

```bash
# Verificar Python
python --version
# ou
python3 --version

# Verificar pip
pip --version
# ou
pip3 --version
```

Se não tiver Python instalado:
- **Windows**: https://www.python.org/downloads/
- **Mac**: `brew install python3`
- **Linux**: `sudo apt-get install python3 python3-pip`

## ⚡ Início Rápido (5 minutos)

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/Drmcoelho/UTI.git
cd UTI
```

**Sem Git?** Baixe o ZIP:
1. Clique em "Code" > "Download ZIP" no GitHub
2. Extraia para uma pasta
3. Abra o terminal nessa pasta

### Passo 2: Crie um Ambiente Virtual (Recomendado)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate

# Você verá (venv) no prompt
```

**Por que usar ambiente virtual?**
- Isola dependências do projeto
- Evita conflitos com outros projetos
- Facilita gerenciamento

### Passo 3: Instale as Dependências

```bash
pip install -r requirements.txt
```

Isso irá instalar:
- Jupyter Notebook
- NumPy, Pandas, Matplotlib
- ipywidgets (para interatividade)
- E outras bibliotecas necessárias

⏱️ **Tempo:** 2-5 minutos (depende da conexão)

### Passo 4: Inicie o Jupyter Notebook

```bash
jupyter notebook
```

Seu navegador abrirá automaticamente em `http://localhost:8888`

### Passo 5: Abra um Notebook

1. No navegador, clique em `notebooks/`
2. Escolha um notebook:
   - `01_monitorizacao_hemodinamica_invasiva.ipynb` (ponto de partida obrigatório)
   - `02_monitorizacao_hemodinamica_nao_invasiva.ipynb` (consolida trending não invasivo)
   - `03_cateter_arteria_pulmonar.ipynb` (interpretação avançada de Swan-Ganz)
3. Execute as células com `Shift + Enter`

## 🎯 Primeiros Passos no Aprendizado

### Dia 1: Familiarização
- [ ] Leia o README.md principal
- [ ] Abra o notebook 01
- [ ] Execute todas as células
- [ ] Teste os simuladores interativos

### Semana 1: Fundamentos
- [ ] Complete notebook 01 (Monitorização Hemodinâmica)
- [ ] Resolva os exercícios do notebook
- [ ] Crie flashcards no Anki
- [ ] Leia 1 caso clínico

### Semana 2: Aprofundamento
- [ ] Complete notebook 02 (Monitorização não invasiva)
- [ ] Pratique com simuladores
- [ ] Resolva exercícios em `exercicios/`
- [ ] Revise flashcards diariamente

### Mês 1: Consolidação
- [ ] Complete os módulos 01-03 e avance para os próximos temas
- [ ] Revise conceitos com flashcards
- [ ] Resolva todos os exercícios disponíveis
- [ ] Contribua com o projeto (opcional)

## 📖 Estrutura do Projeto

```
UTI/
├── README.md                    # Visão geral + 100 temas
├── notebooks/                   # ⭐ Notebooks interativos
│   ├── 01_monitorizacao...ipynb
│   └── 20_sdra.ipynb
├── casos-clinicos/              # Casos práticos
├── exercicios/                  # Questões e exercícios
├── flashcards/                  # Para Anki
├── simuladores/                 # Ferramentas interativas
├── recursos/                    # Tabelas, imagens
└── docs/                        # Documentação adicional
```

## 💡 Como Estudar Efetivamente

### Método Recomendado: "3-2-1"

**3 Recursos por Tema:**
1. Leia o notebook completo
2. Execute os simuladores
3. Resolva os exercícios

**2 Repetições:**
1. Primeira leitura: Entender
2. Segunda leitura: Praticar

**1 Semana Depois:**
- Revise flashcards
- Refaça exercícios
- Teste conhecimento

### Técnica Pomodoro Adaptada

```
📚 25 min: Leitura ativa (notebook)
☕ 5 min: Pausa
🧮 25 min: Prática (simuladores/exercícios)
☕ 5 min: Pausa
💭 25 min: Revisão (flashcards)
☕ 15 min: Pausa longa
```

### Revisão Espaçada

Revise o conteúdo em:
- 1 dia depois (rápida)
- 3 dias depois (média)
- 7 dias depois (completa)
- 21 dias depois (teste)
- 60 dias depois (consolidação)

## 🎮 Recursos Interativos

### Simuladores Disponíveis

1. **Calculadora de PAM**
   - Notebook 01
   - Calcula pressão arterial média
   - Visualiza curva de pressão

2. **Simulador de Noradrenalina**
   - Notebook sobre choque
   - Ajusta dose de vasopressor
   - Observa resposta hemodinâmica

3. **Calculadora de Ventilação Protetora**
   - Notebook 20
   - Calcula volume corrente
   - Avalia pressões ventilatórias

### Como Usar Simuladores

```python
# Exemplo de código interativo
interact(funcao_simulador,
         parametro1=IntSlider(min=0, max=100, value=50),
         parametro2=Dropdown(options=['A', 'B', 'C']))
```

**Dica:** Modifique os valores e observe mudanças em tempo real!

## 📱 Acesso Mobile

### Jupyter no Celular

**Android:**
1. Instale **Termux** (Google Play)
2. Execute:
   ```bash
   pkg install python
   pip install jupyter
   cd /caminho/para/UTI
   jupyter notebook
   ```

Ou use **Carnets** (app dedicado)

**iOS:**
- **Carnets** (App Store)
- **Juno** (para iPad)

### Flashcards no Celular

1. Instale **Anki**:
   - Android: AnkiDroid (Google Play)
   - iOS: AnkiMobile (App Store)

2. Importe flashcards:
   - Copie arquivo `.txt` de `flashcards/`
   - Import no Anki

3. Sincronize com AnkiWeb (opcional)

## 🐛 Troubleshooting

### Problema 1: "ModuleNotFoundError"

```bash
# Reinstale dependências
pip install -r requirements.txt --upgrade
```

### Problema 2: Jupyter não abre

```bash
# Tente especificar o browser
jupyter notebook --browser=firefox
# ou
jupyter notebook --browser=chrome
```

### Problema 3: Widgets não aparecem

```bash
# Instale extensões
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension
```

### Problema 4: Kernel desconectou

No Jupyter:
1. `Kernel` > `Restart`
2. Execute células novamente do início

### Problema 5: Erro de encoding (Windows)

```bash
# Configure UTF-8
set PYTHONIOENCODING=utf-8
jupyter notebook
```

### Problema 6: Erro 400 ao fazer login com Google

Este repositório funciona localmente e **não exige autenticação** para abrir notebooks ou simuladores. Portanto, um erro HTTP 400 ao tentar usar "Login com Google" indica um problema de configuração em um serviço externo (por exemplo, um site complementar ou ambiente compartilhado mantido por outra equipe).

Verifique no [Google Cloud Console](https://console.cloud.google.com/) se:

- O **URI de redirecionamento** está exatamente igual ao endereço usado pelo serviço (incluindo protocolo `https://` ou `http://` e eventuais caminhos).
- O **domínio** do serviço aparece na lista de **origens JavaScript autorizadas** e de **URIs de redirecionamento**.
- O **tipo de conta autorizado** (usuários internos vs. externos) corresponde ao público que tentará acessar.
- A tela de consentimento **OAuth consent screen** está publicada e com status **Approved**.

Links úteis da documentação oficial do Google OAuth:

- [Configurar tela de consentimento OAuth](https://developers.google.com/identity/protocols/oauth2/web-server#consentpage)
- [Registrar URIs de redirecionamento autorizados](https://developers.google.com/identity/protocols/oauth2/web-server#redirect-uri)
- [Erros comuns de OAuth 2.0](https://developers.google.com/identity/protocols/oauth2/web-server#handlingerrors)

Se o login estiver sendo usado em um site externo associado ao projeto (por exemplo, uma plataforma de estudos hospedada pela sua instituição), entre em contato com o responsável por esse ambiente — geralmente o organizador do curso, administrador da plataforma ou a pessoa que forneceu o link. Caso não saiba quem é o responsável, registre a situação nas [Issues do repositório](https://github.com/Drmcoelho/UTI/issues) com o máximo de informações possível para que possamos direcionar o suporte.

### Ainda com problemas?

- Abra uma Issue: https://github.com/Drmcoelho/UTI/issues
- Inclua: erro completo, sistema operacional, versão Python

## 📚 Recursos Adicionais

### Documentação Completa
- `docs/GUIA_INTEGRADO.md` - Guia detalhado
- `docs/TEMPLATE_NOTEBOOK.md` - Para contribuidores
- `CONTRIBUTING.md` - Como contribuir

### Material Externo Recomendado
- **UpToDate**: Referência clínica
- **PubMed**: Artigos científicos
- **Surviving Sepsis Campaign**: Guidelines
- **ARDSNet**: Protocolos de ventilação

### Comunidades
- GitHub Discussions deste repo
- Grupos de estudo locais
- Redes sociais médicas

## 🎓 Certificação (Futuro)

Planejamos oferecer:
- [ ] Certificado de conclusão
- [ ] Badges por módulo
- [ ] Ranking de contribuidores
- [ ] Mentorias online

## 🤝 Como Contribuir

Quer ajudar o projeto?

1. **Reportar erros**: Abra uma Issue
2. **Sugerir melhorias**: Discussions
3. **Adicionar conteúdo**: Pull Request
4. **Compartilhar**: Divulgue para colegas

Veja `CONTRIBUTING.md` para detalhes.

## ⭐ Apoie o Projeto

- Dê uma ⭐ no GitHub
- Compartilhe nas redes sociais
- Recomende para professores
- Contribua com conteúdo

## 📞 Contato e Suporte

- **Issues**: Bugs e problemas técnicos
- **Discussions**: Dúvidas e discussões gerais
- **Pull Requests**: Contribuições de código/conteúdo

## 📈 Roadmap

### 2025 Q4
- [x] Estrutura inicial
- [x] 2 notebooks completos
- [ ] 10 notebooks adicionais
- [ ] Sistema de badges

### 2026 Q1
- [ ] 50 notebooks completos
- [ ] Aplicativo mobile
- [ ] Vídeos explicativos

### 2026 Q2-Q4
- [ ] 100 notebooks completos
- [ ] Tradução para inglês
- [ ] Plataforma web interativa

## 🎉 Pronto para Começar!

Agora você está pronto para:

```bash
# 1. Clone (se ainda não fez)
git clone https://github.com/Drmcoelho/UTI.git
cd UTI

# 2. Instale
pip install -r requirements.txt

# 3. Execute
jupyter notebook

# 4. Aprenda! 🚀
```

## 💪 Mensagem Final

> *"A educação é a arma mais poderosa que você pode usar para mudar o mundo."* - Nelson Mandela

Este repositório existe para democratizar o acesso à educação médica de qualidade. Seja estudante ou profissional, você é bem-vindo aqui.

Seu sucesso nos estudos é nosso sucesso. Conte conosco!

**Bons estudos! 📚🩺**

---

**Desenvolvido com ❤️ pela comunidade médica brasileira**

**Última atualização**: 2025-10-10
