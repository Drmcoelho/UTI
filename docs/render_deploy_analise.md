# Diagnóstico de falhas na implantação Render MCP

## Contexto
Os registros apresentados no painel da Render evidenciam tentativas de executar o comando `npm run build` durante o deploy do serviço **UTI**. O processo retorna `Exited with status 254 while running your code` imediatamente após a execução do comando de build, interrompendo a publicação do serviço.

## Principais mensagens de erro

- `npm ERR! Missing script: "build"`
- Sugestão automática do npm: `npm run build <script>`
- Após a falha, o deploy é abortado e a instância é reiniciada.

Essas mensagens indicam que a Render está tratando o projeto como uma aplicação Node.js, mas o repositório não contém um `package.json` nem scripts NPM configurados para build.

## Causa raiz

1. **Comando de build incorreto**  
   O deploy foi configurado para executar `npm run build`, porém o projeto é composto por notebooks, utilitários Python e materiais educacionais. Não há dependências Node nem scripts NPM definidos.

2. **Tipo de serviço inadequado**  
   Pela captura de tela "New Web Service" é possível que o serviço tenha sido cadastrado como aplicação web genérica com comandos padrão para Node. Para projetos Python/Jupyter recomenda-se configurar o serviço como web service Python ou worker, ajustando o comando inicial para `gunicorn`, `uvicorn` ou outro servidor compatível.

## Como corrigir

1. **Rever comando de build**  
   - Se o objetivo é servir notebooks via [Voilá](https://voila.readthedocs.io), defina o build command como `pip install -r requirements.txt` (caso necessário) e ajuste o start command para `voila caminho/do_notebook.ipynb --port $PORT --no-browser`.
   - Para uma API Flask/FastAPI utilize `pip install -r requirements.txt` e inicie com `gunicorn pacote.app:app --bind 0.0.0.0:$PORT` ou `uvicorn pacote.app:app --host 0.0.0.0 --port $PORT`.

2. **Selecionar o tipo de serviço correto**  
   - Ao criar o serviço na Render, escolha "Python" quando disponível ou mantenha "Web Service" porém informe explicitamente os comandos de build e start adequados para Python.
   - Certifique-se de apontar o diretório raiz correto (por exemplo `/workspace/UTI`), garantindo que o `requirements.txt` seja encontrado.

3. **Variáveis de ambiente**  
   - Configure `PYTHON_VERSION` conforme a versão desejada (ex.: `3.11.5`) para evitar imagens base desatualizadas.

4. **Validação local**  
   - Antes de tentar novo deploy, execute localmente `pip install -r requirements.txt` e o comando de inicialização escolhido para confirmar que a aplicação sobe corretamente.

## Referências úteis

- [Documentação Render MCP Server](https://render.com/docs/render-mcp) — descreve como integrar agentes MCP e comandos personalizados.
- Guias da Render para [deploy de aplicações Python](https://render.com/docs/deploy-flask) e [configuração de serviços web](https://render.com/docs/web-services).

Seguindo os ajustes acima, o processo de deploy deve deixar de executar scripts NPM inexistentes e passar a instalar as dependências Python corretas, permitindo que o serviço seja iniciado com sucesso.
