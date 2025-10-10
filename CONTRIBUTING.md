# Guia de Contribuição

## 🤝 Bem-vindo, Colaborador!

Obrigado por considerar contribuir com o projeto UTI! Este é um projeto comunitário de educação médica gratuita, e sua contribuição pode ajudar milhares de estudantes.

## 📋 Formas de Contribuir

### 1. 🐛 Reportar Erros

Encontrou um erro no conteúdo, código ou documentação?

**Como reportar:**
1. Abra uma [Issue](https://github.com/Drmcoelho/UTI/issues/new)
2. Use o template de bug report
3. Inclua:
   - Descrição clara do erro
   - Passos para reproduzir
   - Comportamento esperado vs observado
   - Screenshots (se aplicável)
   - Versão do Python/Jupyter

**Exemplo:**
```
Título: Erro de cálculo na PAM no notebook 01

Descrição: 
A fórmula da PAM no notebook 01 está retornando valores incorretos
quando PAD > PAS (caso de entrada inválida).

Passos:
1. Abrir notebook 01
2. Executar célula com calcular_pam(80, 120)
3. Resultado esperado: erro ou validação
4. Resultado obtido: valor negativo

Ambiente: Python 3.10, Jupyter 1.0
```

### 2. 💡 Sugerir Melhorias

Tem ideias para melhorar o projeto?

**O que sugerir:**
- Novos recursos para notebooks
- Melhorias em simuladores
- Novos tipos de exercícios
- Otimizações de código
- Melhorias na documentação

**Como sugerir:**
1. Abra uma Issue com label `enhancement`
2. Descreva a melhoria detalhadamente
3. Explique o benefício para os usuários
4. Se possível, sugira implementação

### 3. 📝 Adicionar Conteúdo

#### 3.1 Novos Notebooks

**Requisitos:**
- Seguir estrutura padrão (veja notebooks 01 e 20)
- Conteúdo baseado em evidências
- Código funcional e testado
- Referências bibliográficas

**Estrutura obrigatória:**
```markdown
# Título do Tema

## 📚 Objetivos de Aprendizado
## 🎯 Conceitos Fundamentais
## 📊 Diagramas/Tabelas
## 🧮 Código Interativo
## 🔬 Casos Clínicos
## 💡 Flashcards
## ❓ Exercícios
## 📚 Referências
## 📝 Checklist de Competências
```

#### 3.2 Casos Clínicos

**Formato:**
- Apresentação completa do caso
- Dados clínicos relevantes
- Exames complementares
- Questões para reflexão
- Respostas com justificativas
- Referências

**Template:** Use `casos-clinicos/caso_01_choque_septico.md` como modelo

#### 3.3 Flashcards

**Formato:**
```
Frente da pergunta | Verso com resposta | tags;relevantes
```

**Diretrizes:**
- Uma informação por card
- Frente: pergunta clara e direta
- Verso: resposta concisa mas completa
- Tags: para organização e busca

#### 3.4 Exercícios

**Tipos aceitos:**
- Múltipla escolha com gabarito
- Casos clínicos curtos
- Cálculos práticos
- Verdadeiro ou falso
- Questões dissertativas

**Requisitos:**
- Gabarito com justificativa
- Nível de dificuldade indicado
- Referências quando aplicável

### 4. 🔧 Melhorar Código

**Áreas para contribuir:**
- Otimização de simuladores
- Novos recursos interativos
- Melhorias em visualizações
- Correção de bugs
- Testes unitários

**Diretrizes de código:**
- Python PEP 8
- Docstrings em todas as funções
- Comentários em português
- Código limpo e legível

### 5. 📖 Melhorar Documentação

**Sempre bem-vindo:**
- Correções ortográficas
- Clarificação de instruções
- Exemplos adicionais
- Traduções (futuramente)

## 🔄 Processo de Contribuição

### Passo a Passo

#### 1. Fork o Repositório
```bash
# No GitHub, clique em "Fork" no canto superior direito
```

#### 2. Clone seu Fork
```bash
git clone https://github.com/SEU-USUARIO/UTI.git
cd UTI
```

#### 3. Crie uma Branch
```bash
# Use nome descritivo
git checkout -b adiciona-notebook-32-choque-septico
# ou
git checkout -b corrige-calculo-pam
# ou
git checkout -b melhora-simulador-ventilacao
```

#### 4. Faça suas Mudanças

**Boas práticas:**
- Commits pequenos e frequentes
- Mensagens de commit claras
- Teste suas mudanças
- Atualize documentação se necessário

#### 5. Commit suas Mudanças
```bash
git add .
git commit -m "Adiciona notebook sobre choque cardiogênico

- Adiciona teoria completa
- Inclui simulador de Swan-Ganz
- Adiciona 10 flashcards
- Inclui 2 casos clínicos
- Referências atualizadas"
```

**Formato de mensagens:**
- Linha 1: Resumo (50 caracteres)
- Linha 2: Vazia
- Linha 3+: Detalhes (se necessário)

#### 6. Push para seu Fork
```bash
git push origin sua-branch
```

#### 7. Abra um Pull Request

1. Vá para o repositório original no GitHub
2. Clique em "Pull Requests" > "New Pull Request"
3. Selecione sua branch
4. Preencha o template do PR
5. Aguarde revisão

### Template de Pull Request

```markdown
## Descrição
Breve descrição das mudanças

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova feature
- [ ] Melhoria de conteúdo
- [ ] Melhoria de documentação
- [ ] Refatoração de código

## Checklist
- [ ] Código testado e funcional
- [ ] Documentação atualizada
- [ ] Segue padrões do projeto
- [ ] Referências incluídas (se aplicável)
- [ ] Sem erros de lint
- [ ] Notebooks executam sem erros

## Screenshots (se aplicável)
Cole imagens aqui

## Testes Realizados
Descreva os testes que você fez

## Referências
Liste artigos/guidelines utilizados
```

## ✅ Checklist de Qualidade

### Para Notebooks
- [ ] Executa sem erros do início ao fim
- [ ] Todos os imports no topo
- [ ] Código comentado adequadamente
- [ ] Visualizações renderizam corretamente
- [ ] Flashcards incluídos
- [ ] Exercícios com gabaritos
- [ ] Referências bibliográficas
- [ ] Segue estrutura padrão

### Para Código Python
- [ ] Segue PEP 8
- [ ] Docstrings em funções
- [ ] Type hints quando aplicável
- [ ] Tratamento de erros
- [ ] Testes (quando aplicável)

### Para Conteúdo Médico
- [ ] Baseado em evidências
- [ ] Referências de qualidade
- [ ] Linguagem clara e objetiva
- [ ] Revisado por par (se possível)
- [ ] Atualizado conforme guidelines

## 🎨 Padrões de Estilo

### Markdown
- Títulos: `#`, `##`, `###` (hierárquico)
- Ênfase: `**negrito**`, `*itálico*`
- Código inline: \`código\`
- Blocos de código: \`\`\`python
- Listas: `-` ou `1.`
- Emojis para seções: 📚 🎯 💡 etc.

### Python
```python
def calcular_pam(pas: float, pad: float) -> float:
    """
    Calcula a Pressão Arterial Média.
    
    Args:
        pas: Pressão Arterial Sistólica em mmHg
        pad: Pressão Arterial Diastólica em mmHg
        
    Returns:
        float: Pressão Arterial Média em mmHg
        
    Raises:
        ValueError: Se PAS < PAD ou valores negativos
        
    Example:
        >>> calcular_pam(120, 80)
        93.3
    """
    if pas < pad or pas < 0 or pad < 0:
        raise ValueError("Valores de pressão inválidos")
    
    pam = pad + (pas - pad) / 3
    return round(pam, 1)
```

### Jupyter Notebooks
- Cell 1: Título e objetivos
- Cell 2+: Conteúdo organizado em seções
- Intercalar Markdown e Code cells
- Outputs salvos para visualização rápida
- Clear output antes de commit (se muito grande)

## 🚫 O Que NÃO Fazer

### ❌ Não Aceito

1. **Plágio**
   - Copiar conteúdo sem atribuição
   - Usar código de terceiros sem licença

2. **Conteúdo Não-Científico**
   - "Medicina alternativa" sem evidência
   - Opiniões pessoais como fatos
   - Informações desatualizadas

3. **Código Problemático**
   - Código que não executa
   - Sem documentação
   - Práticas inseguras

4. **Mudanças Destrutivas**
   - Deletar conteúdo sem motivo
   - Reformatar todo o projeto
   - Mudar estrutura sem discussão

## 🏆 Reconhecimento

Contribuidores terão:
- Nome no CONTRIBUTORS.md
- Crédito nos commits
- Reconhecimento na comunidade
- Possibilidade de co-autoria em publicações futuras

## 📞 Dúvidas?

- **Issues**: Para perguntas específicas
- **Discussions**: Para discussões gerais
- **Email**: [será adicionado]

## 📚 Recursos para Contribuidores

### Aprendendo Git/GitHub
- [Git Book](https://git-scm.com/book/pt-br/v2)
- [GitHub Docs](https://docs.github.com/pt)
- [First Contributions](https://github.com/firstcontributions/first-contributions)

### Jupyter
- [Jupyter Documentation](https://jupyter.org/documentation)
- [nbviewer](https://nbviewer.org/)

### Python
- [PEP 8](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

### Medicina Baseada em Evidências
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
- [Cochrane Library](https://www.cochranelibrary.com/)
- [UpToDate](https://www.uptodate.com/)

## 📜 Código de Conduta

### Nossos Valores

- **Respeito**: Trate todos com respeito
- **Inclusão**: Ambiente acolhedor para todos
- **Colaboração**: Trabalhe em equipe
- **Qualidade**: Compromisso com excelência
- **Ética**: Integridade acadêmica

### Comportamento Esperado

✅ **Faça:**
- Seja respeitoso e construtivo
- Aceite críticas com elegância
- Foque no que é melhor para a comunidade
- Mostre empatia com outros membros

❌ **Não faça:**
- Linguagem ou imagens ofensivas
- Ataques pessoais
- Assédio público ou privado
- Publicar informações privadas
- Conduta antiética

### Aplicação

Violações serão avaliadas e podem resultar em:
1. Aviso
2. Banimento temporário
3. Banimento permanente

## 🎉 Agradecimentos

Obrigado por contribuir para a educação médica gratuita e de qualidade!

Sua contribuição pode impactar a formação de milhares de profissionais de saúde e, indiretamente, a vida de inúmeros pacientes.

---

**Desenvolvido com ❤️ pela comunidade médica**
