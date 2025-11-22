# Setup e uso

Prerequisitos:
- Python 3.11+ e pip.
- Opcional: ambiente virtual.

Passo a passo sugerido:
1. python -m venv .venv
2. .\.venv\Scripts\Activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

Observacoes:
- O banco padrao e db.sqlite3 na raiz. Remova e rode migrate se quiser partir limpo.
- Neste estado do projeto ha apenas o admin do Django acessivel.
- DEBUG esta ativado em core/settings.py, nao use em producao.
