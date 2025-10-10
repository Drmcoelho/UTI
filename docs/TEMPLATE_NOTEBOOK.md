# Template para Novos Notebooks

Este arquivo serve como template para criação de novos notebooks. Copie e adapte conforme o tema.

## 📋 Checklist Antes de Começar

- [ ] Pesquisar referências atualizadas (guidelines, artigos, livros)
- [ ] Identificar conceitos-chave do tema
- [ ] Planejar simuladores/calculadoras necessários
- [ ] Preparar casos clínicos relevantes
- [ ] Listar flashcards importantes

## 🎯 Estrutura Padrão

### 1. Cabeçalho (Markdown Cell)

```markdown
# [Número] - [Nome do Tema]

## 📚 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Objetivo 1
- Objetivo 2
- Objetivo 3
- Objetivo 4

---
```

### 2. Conceitos Fundamentais (Markdown Cell)

```markdown
## 🎯 Conceitos Fundamentais

### Definição

[Definição clara e concisa do tema]

### Epidemiologia/Relevância

[Por que este tema é importante?]

### Fisiopatologia

[Como funciona? O que acontece?]
```

### 3. Diagramas Mermaid (Markdown Cell)

```markdown
## 🔄 Fluxograma de Decisão

\`\`\`mermaid
graph TD
    A[Situação Inicial] --> B{Pergunta Decisória?}
    B -->|Sim| C[Ação 1]
    B -->|Não| D[Ação 2]
    C --> E[Resultado]
    D --> E
\`\`\`
```

**Tipos de diagramas úteis:**
- `graph TD`: Fluxograma vertical
- `graph LR`: Fluxograma horizontal
- `mindmap`: Mapa mental
- `timeline`: Linha do tempo
- `pie`: Gráfico de pizza

### 4. Tabelas Comparativas (Markdown Cell)

```markdown
## 📊 Tabela Comparativa

| Característica | Opção A | Opção B | Opção C |
|----------------|---------|---------|---------|
| Vantagem 1 | ✓ | ✗ | ✓ |
| Vantagem 2 | ✗ | ✓ | ✓ |
| Eficácia | Alta | Média | Baixa |
```

### 5. Imports e Configuração (Code Cell)

```python
# Importar bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact, IntSlider, FloatSlider, Dropdown

# Configurar visualização
plt.style.use('seaborn-v0_8-darkgrid')
%matplotlib inline

# Configurações de display
pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)
```

### 6. Funções de Cálculo (Code Cell)

```python
def calcular_parametro_exemplo(valor1: float, valor2: float) -> float:
    """
    Descrição breve da função.
    
    Parâmetros:
    valor1 (float): Descrição do parâmetro 1
    valor2 (float): Descrição do parâmetro 2
    
    Retorna:
    float: Descrição do resultado
    
    Exemplo:
    >>> calcular_parametro_exemplo(10, 20)
    30.0
    """
    # Validação de entrada
    if valor1 < 0 or valor2 < 0:
        raise ValueError("Valores devem ser positivos")
    
    # Cálculo
    resultado = (valor1 + valor2) / 2
    
    return round(resultado, 2)

# Teste da função
print("Exemplo de cálculo:")
resultado = calcular_parametro_exemplo(100, 80)
print(f"Resultado: {resultado}")
```

### 7. Simulador Interativo (Code Cell)

```python
def simulador_interativo(parametro1=100, parametro2=80, opcao='Normal'):
    """
    Simulador interativo do tema.
    """
    # Cálculos baseados nos parâmetros
    resultado = calcular_parametro_exemplo(parametro1, parametro2)
    
    # Ajustes baseados na opção
    if opcao == 'Alterado':
        resultado *= 1.2
    
    # Apresentação dos resultados
    print("="*60)
    print("SIMULADOR - [NOME DO TEMA]")
    print("="*60)
    print(f"\nParâmetro 1: {parametro1}")
    print(f"Parâmetro 2: {parametro2}")
    print(f"Opção: {opcao}")
    print(f"\nResultado: {resultado}")
    
    # Interpretação
    print("\n" + "-"*60)
    print("INTERPRETAÇÃO:")
    print("-"*60)
    if resultado > 90:
        print("✓ Valor ADEQUADO")
    else:
        print("✗ Valor ALTERADO - Considerar intervenção")
    print("="*60)
    
    # Visualização
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Exemplo de gráfico de barras
    categorias = ['Parâmetro 1', 'Parâmetro 2', 'Resultado']
    valores = [parametro1, parametro2, resultado]
    colors = ['#4ecdc4', '#ff6b6b', '#ffd93d']
    
    bars = ax.bar(categorias, valores, color=colors, edgecolor='black', linewidth=2)
    ax.set_ylabel('Valor', fontsize=12, fontweight='bold')
    ax.set_title('Visualização dos Parâmetros', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Adicionar valores nas barras
    for bar, valor in zip(bars, valores):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{valor:.1f}',
                ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    plt.tight_layout()
    plt.show()

# Widget interativo
interact(simulador_interativo,
         parametro1=IntSlider(min=50, max=150, step=5, value=100, description='Param 1'),
         parametro2=IntSlider(min=50, max=150, step=5, value=80, description='Param 2'),
         opcao=Dropdown(options=['Normal', 'Alterado'], value='Normal', description='Status'));
```

### 8. Casos Clínicos (Markdown Cell)

```markdown
## 🔬 Caso Clínico Interativo

### Caso 1: [Título do Caso]

**Cenário:** [Descrição breve do cenário clínico]

**Dados do Paciente:**
- Identificação: [idade, sexo]
- História: [resumo relevante]
- Exame físico: [achados principais]
- Exames: [resultados importantes]

**Questões:**

1. Qual o diagnóstico mais provável?
2. Qual a conduta inicial?
3. Quais as metas terapêuticas?

**Discussão:**
[Análise detalhada do caso com justificativas]
```

### 9. Flashcards (Markdown Cell)

```markdown
## 💡 Flashcards para Memorização

### Card 1
**Frente:** Pergunta objetiva sobre conceito importante?

**Verso:** Resposta clara e concisa com informação essencial.

---

### Card 2
**Frente:** Segunda pergunta?

**Verso:** Segunda resposta.

---

[Mínimo 10 cards por tema]
```

### 10. Exercícios (Markdown Cell)

```markdown
## ❓ Exercícios - Múltipla Escolha

### Questão 1
[Enunciado da questão]

A) Opção A  
B) Opção B  
C) Opção C  
D) Opção D  
E) Opção E  

**Resposta:** [Letra correta]

**Explicação:** [Justificativa detalhada]

---

[Mínimo 5 questões por tema]
```

### 11. Referências (Markdown Cell)

```markdown
## 📚 Referências Bibliográficas

1. **Autor et al.** Título do artigo. Revista. Ano;Volume(Número):Páginas.

2. **Guideline/Protocolo.** Título completo. Sociedade/Organização. Ano.

3. **Livro.** Autor. Título do Livro. Edição. Editora; Ano.

[Mínimo 5 referências de qualidade]
```

### 12. Checklist Final (Markdown Cell)

```markdown
## 📝 Checklist de Competências

Após estudar este módulo, você deve ser capaz de:

- [ ] Competência 1
- [ ] Competência 2
- [ ] Competência 3
- [ ] Competência 4
- [ ] Competência 5

---

## 🎓 Próximos Passos

- Revise os flashcards diariamente
- Pratique com os simuladores interativos
- Resolva os exercícios propostos
- Consulte as referências para aprofundamento
- Avance para o próximo tema: **[Número] - [Nome do Próximo Tema]**
```

## 💡 Dicas para Criação de Conteúdo

### Conteúdo Teórico
- **Seja conciso mas completo**
- Use listas e bullet points
- Destaque conceitos-chave em **negrito**
- Use emojis para organização visual

### Código
- **Documente tudo**: docstrings, comentários
- **Valide entradas**: evite erros de execução
- **Teste antes**: execute célula por célula
- **Seja didático**: explique o que o código faz

### Visualizações
- **Use cores consistentes**
- **Adicione labels claros**
- **Inclua títulos descritivos**
- **Ajuste tamanho (figsize)**

### Simuladores
- **Parâmetros realistas**
- **Feedback claro**
- **Interpretação automática**
- **Gráficos ilustrativos**

### Casos Clínicos
- **Baseie em situações reais**
- **Inclua dados completos**
- **Questões progressivas**
- **Discussão baseada em evidências**

### Flashcards
- **Uma informação por card**
- **Perguntas diretas**
- **Respostas completas mas concisas**
- **Conceitos-chave do tema**

### Exercícios
- **Varie dificuldade**
- **Gabarito sempre justificado**
- **Cubra todos os objetivos**
- **Questões práticas e aplicadas**

## ✅ Checklist Pré-Publicação

Antes de submeter seu notebook:

- [ ] Executou todas as células do início ao fim sem erros
- [ ] Todos os imports estão no topo
- [ ] Código está documentado (docstrings e comentários)
- [ ] Visualizações renderizam corretamente
- [ ] Simuladores funcionam conforme esperado
- [ ] Flashcards incluídos (mínimo 10)
- [ ] Exercícios com gabaritos (mínimo 5)
- [ ] Referências bibliográficas atualizadas (mínimo 5)
- [ ] Checklist de competências completo
- [ ] Revisão ortográfica e gramatical
- [ ] Conteúdo baseado em evidências
- [ ] Segue estrutura padrão do template

## 📞 Ajuda

Dúvidas sobre como criar notebooks?
- Consulte os exemplos: notebooks 01 e 20
- Abra uma Issue no GitHub
- Participe das Discussions

## 🎉 Obrigado por Contribuir!

Sua contribuição ajuda a democratizar o acesso à educação médica de qualidade.

---

**Template versão 1.0 - Atualizado em 2025-10-10**
