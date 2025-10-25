# GitHub Pages com JupyterLite - Documentação de Implementação

## 📋 Resumo

Este documento descreve a implementação do suporte ao GitHub Pages com JupyterLite para o repositório UTI, permitindo a execução interativa de notebooks diretamente no navegador.

## 🎯 Requisitos Atendidos

- ✅ README.md principal permanece intacto
- ✅ index.html criado como página inicial descrevendo o projeto
- ✅ JupyterLite configurado para execução interativa no navegador
- ✅ _config.yml criado para ativação do GitHub Pages
- ✅ Navegação para notebooks disponíveis (01 e 20)
- ✅ Instruções claras de uso na página inicial
- ✅ Todo o restante do conteúdo do repositório permanece intacto
- ✅ Uso de dependências mínimas necessárias

## 📁 Arquivos Criados

### 1. `index.html` (Raiz)
Página inicial completa e profissional com:
- Descrição detalhada do projeto
- Links diretos para JupyterLite
- Lista de notebooks disponíveis com links diretos
- Instruções passo a passo de uso
- Duas opções de uso: online (JupyterLite) e local (instalação tradicional)
- FAQ e recursos adicionais
- Design responsivo e moderno

### 2. `_config.yml`
Configuração mínima do Jekyll para GitHub Pages:
```yaml
theme: jekyll-theme-minimal
title: UTI - Educação Médica Gratuita
description: Repositório de aprendizado interativo para estudantes de medicina
```

### 3. `jupyter-lite.json`
Configuração do JupyterLite:
- Nome da aplicação: "UTI - Notebooks Interativos"
- Tema padrão: JupyterLab Light
- Configurações básicas de ambiente

### 4. `.github/workflows/deploy.yml`
Workflow do GitHub Actions que:
- Instala JupyterLite e dependências
- Faz build do JupyterLite com os notebooks da pasta `notebooks/`
- Copia arquivos necessários para deploy
- Publica no GitHub Pages automaticamente

### 5. `requirements-lite.txt`
Dependências mínimas para build do JupyterLite:
- jupyterlite-core
- jupyterlite-pyodide-kernel  
- jupyter-server

### 6. `.nojekyll`
Arquivo vazio que instrui o GitHub Pages a não processar arquivos com Jekyll, essencial para o funcionamento correto do JupyterLite.

### 7. Atualização do `.gitignore`
Adicionadas entradas para:
- `lite/` (diretório de build do JupyterLite)
- `_site/` (diretório temporário de deploy)
- `.jupyterlite.doit.db` (arquivo de cache do build)

## 🚀 Como Funciona

### Processo de Deploy Automático

1. **Trigger**: Push para a branch `main`
2. **Build**: GitHub Actions executa o workflow
3. **Geração**: JupyterLite cria versão web dos notebooks
4. **Deploy**: Publicação automática no GitHub Pages

### Estrutura Resultante no GitHub Pages

```
https://drmcoelho.github.io/UTI/
├── index.html                    # Página inicial
├── lite/                         # JupyterLite (gerado automaticamente)
│   ├── lab/                      # Interface JupyterLab
│   │   └── index.html           # Ambiente interativo
│   ├── files/                    # Notebooks copiados
│   │   ├── 01_monitorizacao_hemodinamica_invasiva.ipynb
│   │   ├── 20_sdra.ipynb
│   │   └── README.md
│   └── [outros arquivos do JupyterLite]
└── _config.yml                   # Configuração Jekyll
```

## 💡 Uso pelo Usuário

### Opção 1: Navegador (Recomendado)
1. Acessar https://drmcoelho.github.io/UTI/
2. Clicar em "Abrir JupyterLite"
3. Navegar até a pasta notebooks
4. Abrir e executar notebooks interativamente

### Opção 2: Links Diretos
- Acesso direto ao notebook 01: https://drmcoelho.github.io/UTI/lite/lab/index.html?path=notebooks/01_monitorizacao_hemodinamica_invasiva.ipynb
- Acesso direto ao notebook 20: https://drmcoelho.github.io/UTI/lite/lab/index.html?path=notebooks/20_sdra.ipynb

## 🔧 Características Técnicas

### JupyterLite
- Execução 100% no navegador via WebAssembly
- Kernel Python (Pyodide) embutido
- Não requer servidor backend
- Armazenamento local via IndexedDB
- Suporte a widgets interativos básicos

### Limitações Conhecidas
- Algumas bibliotecas Python podem não estar disponíveis no Pyodide
- Performance pode ser menor que execução local
- Salvamentos são locais ao navegador (usuário deve fazer download)
- Bibliotecas que requerem C extensions podem não funcionar

### Vantagens
- Zero instalação necessária
- Funciona em qualquer navegador moderno
- Ideal para demonstrações e aprendizado
- Acesso rápido e imediato
- Seguro (execução sandboxed)

## 📊 Validação

### Build Local Testado
```bash
pip install -r requirements-lite.txt
jupyter lite build --contents notebooks --output-dir lite
```
Resultado: ✅ Build bem-sucedido com ambos notebooks incluídos

### Arquivos Verificados
- ✅ README.md não modificado
- ✅ Estrutura de pastas intacta
- ✅ Notebooks originais preservados
- ✅ Apenas arquivos novos adicionados

## 🎓 Instruções de Ativação

Após o merge desta PR:

1. Vá para Settings > Pages no repositório
2. Em "Build and deployment", selecione:
   - Source: "GitHub Actions"
3. O workflow será executado automaticamente
4. Aguarde ~2-5 minutos para o build completar
5. Acesse: https://drmcoelho.github.io/UTI/

## 📝 Notas Adicionais

- O build do JupyterLite é executado apenas no GitHub Actions
- O diretório `lite/` é gerado automaticamente e não deve ser commitado
- Novos notebooks adicionados à pasta `notebooks/` serão incluídos automaticamente no próximo deploy
- A página inicial pode ser customizada editando `index.html`
- Para testar localmente: `jupyter lite build --contents notebooks --output-dir lite && python -m http.server --directory lite 8000`

## 🔄 Manutenção Futura

### Para Adicionar Novos Notebooks
1. Adicione o arquivo `.ipynb` em `notebooks/`
2. Commit e push para main
3. GitHub Actions reconstruirá automaticamente
4. Opcional: adicione link direto no `index.html`

### Para Atualizar JupyterLite
1. Edite `requirements-lite.txt` com novas versões
2. Commit e push
3. Próximo build usará versões atualizadas

## 📚 Referências

- [JupyterLite Documentation](https://jupyterlite.readthedocs.io/)
- [GitHub Pages Documentation](https://docs.github.com/pages)
- [Pyodide Documentation](https://pyodide.org/)
