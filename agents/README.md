# Agentes Finanpy

Time virtual especializado na stack Finanpy (Django 4+, Templates, TailwindCSS, SQLite). Sempre consulte `docs/README.md` e `PRD.md` e compartilhe requisitos claros antes de chamar um agente.

## Indice rapido
- [Backend Django](./backend-django.md) - Modelos, views, sinais, auth, regras de saldo e integracoes server-side.
- [Frontend Templates](./frontend-templates.md) - HTML Django Template Language, componentes Tailwind e telas responsivas escuras.
- [QA Playwright](./qa-playwright.md) - Testes E2E/UI no navegador avaliando fluxos e design system.

## Como escolher
- Backend Django: use para implementar ou refatorar logicas no core/users/profiles/accounts/categories/transactions, configurar settings, URLs e signals. Esse agente sempre consulta o MCP server `context7` para fundamentar o codigo nas referencias oficiais mais recentes.
- Frontend Templates: use para criar ou ajustar `templates/` seguindo o design system dark, textos em PT-BR e grids responsivos. Ele tambem depende do MCP `context7` para revisar documentacao de Django Templates e Tailwind antes de gerar HTML/CSS.
- QA Playwright: use apos entregas para validar fluxos completos (cadastro, login, dashboard, CRUDs, perfil) e o layout. Ele opera via MCP server `playwright` para executar scripts e registrar evidencias.

Todos os agentes entendem o roadmap das sprints do PRD, mantem o isolamento de dados por usuario e exigem instrucoes claras sobre arquivos, requisitos e criterios de aceite.
