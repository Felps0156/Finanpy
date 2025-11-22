# Arquitetura e estrutura

Modelo: Django MVT com apps por dominio.

Estrutura atual:
- core: configuracoes globais; settings.py mantem INSTALLED_APPS com accounts, categories, profiles, transactions, users; urls.py expoe apenas admin/.
- accounts: placeholder para contas bancarias.
- categories: placeholder para categorias de lancamentos.
- profiles: placeholder para dados adicionais do usuario.
- transactions: placeholder para registros financeiros.
- users: placeholder para customizacoes futuras do usuario.

Configuracoes relevantes (estado atual):
- Templates: somente APP_DIRS=True; nenhuma pasta templates global definida.
- Static: STATIC_URL = "static/"; sem pasta static criada ainda.
- Idioma/fuso: en-us e UTC.
- Banco: SQLite apontando para db.sqlite3 na raiz.
- Dependencias: requirements.txt contem apenas django.

Design e frontend:
- Ainda nao ha templates ou assets. Quando forem criados, seguir o design system descrito no PRD (tema escuro, gradientes, TailwindCSS).
