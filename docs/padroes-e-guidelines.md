# Padroes e guidelines

Codigo:
- Seguir PEP8 e preferir aspas simples.
- Manter solucoes simples, sem over engineering.
- Usar recursos nativos do Django sempre que possivel (ORM, auth, forms, class based views).
- Separar responsabilidades por app de dominio conforme pasta existente.
- Se signals forem usados, coloca-los em signals.py da respectiva app.
- Textos da interface devem ficar em portugues brasileiro.

Dados e modelos:
- Usar SQLite como banco padrao.
- Incluir campos created_at e updated_at nos models de dominio quando forem implementados.

Frontend:
- Tema escuro e design system descritos no PRD (cores, gradientes, tipografia).
- Reutilizar layout base compartilhado entre telas; usar o design system para formularios e botoes.
- TailwindCSS e o utilitario previsto para estilos conforme PRD.

Fluxo e navegacao:
- URLs devem ser modulares por app e incluidas a partir de core/urls.py.
- Dashboard, landing page e CRUDs descritos no PRD ainda nao existem; implementar conforme especificacao quando for priorizado.

Processo:
- Nao ha testes ou Docker configurados; sao itens planejados para sprints futuras segundo o PRD.
- Revisar PRD antes de adicionar novas features para manter alinhamento de escopo.
