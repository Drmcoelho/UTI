# Contribuição

Este guia resume o fluxo de contribuição recomendado. Consulte `CONTRIBUTING.md` para detalhes completos.

## Checklist Essencial

1. Use o template `docs/TEMPLATE_NOTEBOOK.md` ao iniciar um novo tema.
2. Execute `pytest` e `jupyter nbconvert --execute` antes de abrir um Pull Request.
3. Atualize `docs/RESUMO_PROJETO.md` com o status do tema entregue.

## Convenções

- Funções reutilizáveis devem ser adicionadas em `notebooks/utils/`.
- Simuladores interativos precisam de documentação curta descrevendo objetivos e limitações.
- Cada notebook deve conter referências bibliográficas ao final.

## Revisão

Os PRs passam por revisão de pares clínicos e técnicos. Utilize os checks automatizados (CI) para validar notebooks e documentação antes de solicitar revisão.
