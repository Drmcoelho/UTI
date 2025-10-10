# Guia de Uso do Repositório UTI

## 📖 Bem-vindo!

Este guia irá ajudá-lo a navegar e aproveitar ao máximo os recursos disponíveis neste repositório de educação médica em UTI.

## 🎯 Para Quem é Este Repositório?

- **Estudantes de Medicina** (todos os anos)
- **Residentes de Medicina Intensiva**
- **Médicos em formação**
- **Profissionais que desejam revisar conceitos de UTI**

## 📚 Estrutura do Conteúdo

### 1. Notebooks (`/notebooks/`)

Os notebooks são o **coração** deste projeto. Cada um dos 100 temas tem seu próprio notebook interativo com:

**Componentes de cada notebook:**
- 📝 Teoria completa e atualizada
- 📊 Diagramas e flowcharts (Mermaid)
- 🧮 Código executável para cálculos
- 🎮 Simuladores interativos
- 💡 Flashcards integrados
- ❓ Exercícios práticos
- 📖 Referências bibliográficas

**Como usar:**
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar Jupyter
jupyter notebook

# 3. Navegar até /notebooks/ e abrir o tema desejado
# Exemplo: 01_monitorizacao_hemodinamica_invasiva.ipynb
```

**Dicas para notebooks:**
- Execute as células sequencialmente (Shift + Enter)
- Interaja com os widgets e simuladores
- Modifique parâmetros para aprender
- Salve suas anotações (File > Save)

### 2. Casos Clínicos (`/casos-clinicos/`)

**Descrição:** Casos reais (anonimizados) ou baseados em situações típicas de UTI.

**Estrutura de cada caso:**
- Apresentação do paciente
- História clínica detalhada
- Exames complementares
- Questões para reflexão
- Respostas com justificativas
- Discussão baseada em evidências

**Como estudar:**
1. Leia o caso completo
2. Tente responder as questões antes de ver as respostas
3. Compare seu raciocínio com as respostas fornecidas
4. Consulte as referências para aprofundamento

### 3. Flashcards (`/flashcards/`)

**Formato:** Compatível com Anki (software de repetição espaçada)

**Como usar:**
1. **Opção 1 - Anki (recomendado):**
   - Baixe Anki: https://apps.ankiweb.net/
   - Importe o arquivo: File > Import > selecione o arquivo .txt
   - Configure revisão diária (20-30 cards/dia)

2. **Opção 2 - Leitura direta:**
   - Abra o arquivo .txt
   - Use para revisão rápida
   - Cubra a resposta e teste seu conhecimento

**Dicas:**
- Revise diariamente (consistência > quantidade)
- Use o sistema de repetição espaçada
- Adicione seus próprios flashcards
- Revise antes de provas/plantões

### 4. Exercícios (`/exercicios/`)

**Tipos de exercícios:**
- Múltipla escolha
- Casos clínicos curtos
- Cálculos práticos
- Interpretação de exames
- Questões dissertativas

**Como usar:**
- Resolva sem consultar material
- Anote dúvidas
- Revise conceitos que errou
- Refaça periodicamente

### 5. Simuladores (`/simuladores/`)

**Descrição:** Ferramentas interativas para praticar:
- Ajuste de ventilação mecânica
- Titulação de drogas vasoativas
- Interpretação de curvas
- Tomada de decisões

**Como usar:**
- Execute via Jupyter Notebook
- Experimente diferentes cenários
- Observe consequências das decisões
- Aprenda de forma ativa

### 6. Recursos (`/recursos/`)

**Conteúdo:**
- Imagens médicas
- Diagramas anatômicos
- Tabelas de referência rápida
- Algoritmos de manejo
- Protocolos

**Como usar:**
- Consulta rápida durante estudos
- Material de apoio para apresentações
- Revisão visual de conceitos

## 🚀 Começando do Zero

### Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/Drmcoelho/UTI.git
cd UTI

# 2. Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Inicie o Jupyter
jupyter notebook
```

### Primeiros Passos

**Semana 1-2: Fundamentos**
- [ ] Comece pelo tema 01 (Monitorização Hemodinâmica)
- [ ] Execute todos os códigos do notebook
- [ ] Faça os flashcards diários
- [ ] Resolva 1 caso clínico

**Semana 3-4: Respiratório**
- [ ] Temas 16-30 (Suporte Respiratório)
- [ ] Foque em ventilação mecânica (16-19)
- [ ] Estude SDRA em detalhes (tema 20)
- [ ] Pratique com simuladores

**Mês 2: Choque e Hemodinâmica**
- [ ] Temas 31-45 (Choque e Instabilidade)
- [ ] Revise choque séptico (32)
- [ ] Pratique cálculos hemodinâmicos
- [ ] Casos clínicos complexos

**Continue:** Siga a ordem dos temas ou personalize conforme suas necessidades.

## 💡 Dicas de Estudo

### Técnica Pomodoro + Revisão Ativa

```
25 min: Estudo do notebook (leitura + código)
5 min: Pausa
25 min: Exercícios/casos clínicos
5 min: Pausa
25 min: Flashcards + revisão
15 min: Pausa longa
```

### Curva de Esquecimento

Revise o material nos seguintes intervalos:
- 1 dia depois
- 3 dias depois
- 7 dias depois
- 21 dias depois
- 60 dias depois

### Estudo Ativo vs Passivo

✅ **FAÇA (Ativo):**
- Execute os códigos
- Modifique parâmetros
- Resolva exercícios
- Explique para alguém
- Crie resumos próprios

❌ **EVITE (Passivo):**
- Apenas ler
- Copiar e colar
- Não testar conhecimento
- Postergar exercícios

## 🎓 Níveis de Aprendizado

### Nível 1: Iniciante
**Objetivo:** Compreender conceitos básicos

- Leia notebooks completamente
- Execute códigos sem modificar
- Flashcards básicos
- Casos clínicos simples

### Nível 2: Intermediário
**Objetivo:** Aplicar conhecimento

- Modifique parâmetros nos simuladores
- Resolva casos complexos
- Crie seus próprios flashcards
- Correlacione temas diferentes

### Nível 3: Avançado
**Objetivo:** Sintetizar e criar

- Resolva casos sem consultar material
- Contribua com novos casos
- Crie novos simuladores
- Ensine outros colegas

## 🤝 Como Contribuir

### Formas de Contribuir

1. **Reporte Erros**
   - Abra uma Issue no GitHub
   - Descreva o erro detalhadamente
   - Sugira correção se possível

2. **Adicione Conteúdo**
   - Novos casos clínicos
   - Flashcards adicionais
   - Exercícios
   - Melhorias em notebooks

3. **Compartilhe Conhecimento**
   - Sugira referências
   - Adicione protocolos locais
   - Compartilhe experiências

### Processo de Contribuição

```bash
# 1. Fork o repositório
# 2. Clone seu fork
git clone https://github.com/SEU-USUARIO/UTI.git

# 3. Crie uma branch
git checkout -b minha-contribuicao

# 4. Faça suas mudanças
# 5. Commit
git commit -m "Adiciona caso clínico de TEP"

# 6. Push
git push origin minha-contribuicao

# 7. Abra um Pull Request no GitHub
```

## 📱 Acesso Mobile

### Jupyter no Celular

**Android:**
- Termux + Jupyter
- Carnets (app dedicado)

**iOS:**
- Carnets
- Juno

### Flashcards no Celular

- **AnkiDroid** (Android)
- **AnkiMobile** (iOS)
- Sincronize com AnkiWeb

## ❓ FAQ

### Como estudar se tenho pouco tempo?

**Plano Mínimo (30 min/dia):**
- 15 min: Flashcards (revisão espaçada)
- 15 min: 1 seção de um notebook

### Preciso saber programação?

**Não!** O código está pronto para executar. Você só precisa:
- Clicar em "Run" (Shift + Enter)
- Modificar valores nos sliders
- Observar resultados

### Os notebooks funcionam offline?

**Sim!** Após instalar as dependências, tudo funciona offline.

### Como tirar dúvidas?

1. Consulte as referências no notebook
2. Abra uma Issue no GitHub
3. Discussão na comunidade (Discussions)

### Posso usar em provas/concursos?

**Sim!** Todo conteúdo é baseado em:
- Evidências científicas
- Guidelines internacionais
- Livros-texto reconhecidos

### Como acompanhar atualizações?

```bash
# No seu repositório local
git pull origin main

# Ou "Watch" o repositório no GitHub
```

## 🎯 Checklist de Progresso

Use este checklist para acompanhar seu progresso:

### Monitorização (1-15)
- [ ] Tema 01 - Monitorização Hemodinâmica Invasiva
- [ ] Tema 02 - Monitorização Hemodinâmica Não-Invasiva
- [ ] ... (complete conforme avança)

### Respiratório (16-30)
- [ ] Tema 16 - VM Invasiva: Princípios
- [ ] Tema 20 - SDRA
- [ ] ... (continue)

*(Complete para todos os 100 temas)*

## 📞 Suporte

- **Issues:** https://github.com/Drmcoelho/UTI/issues
- **Discussions:** https://github.com/Drmcoelho/UTI/discussions

## 📄 Licença

MIT License - Use livremente para fins educacionais.

## ⚠️ Disclaimer

Este material é para fins educacionais. Sempre:
- Consulte supervisores
- Siga protocolos institucionais
- Atualize-se continuamente
- Use julgamento clínico individual

---

**Bons estudos! 📚💪**

*Última atualização: 2025-10-10*
