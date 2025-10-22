# Deploy e Publicação

Esta seção descreve como gerar o portal estático e publicá-lo automaticamente no GitHub Pages.

## Requisitos Locais

1. Instale as dependências do projeto: `pip install -r requirements.txt`.
2. Garanta que o `nbconvert` consiga executar todos os notebooks: `jupyter nbconvert --to notebook --execute notebooks/*.ipynb`.

## Build Manual

```bash
cd docs/site
sphinx-build -b html . _build/html
```

O resultado estará em `_build/html`. Basta publicar o conteúdo em qualquer provedor de hospedagem estática.

## Publicação Automatizada

O workflow `docs.yml` gera o portal e publica no branch `gh-pages` quando houver push na branch `main`. Após ativar o GitHub Pages para servir esse branch, as atualizações passam a ser automáticas.

## Pré-Requisitos do Repositório

- Ative o GitHub Pages em **Settings → Pages** selecionando o branch `gh-pages` e a pasta raiz (`/`).
- Forneça permissões de escrita para GitHub Actions (`Settings → Actions → General`).
- Garanta que os notebooks já tenham sido executados localmente para que as saídas estejam presentes nas páginas renderizadas.
