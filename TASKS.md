## Lista de tarefas (em sprints, checklist granular)

> Formato: `[ ]` para abrir, `[x]` para concluído.  
> Sprints focam em pequenas implementações específicas.

### Sprint 1 – Setup do projeto e estrutura [x]

#### 1.1 Projeto Django e core [x]

- [x] Criar ambiente virtual Python (ex.: `python -m venv .venv`).
- [x] Ativar ambiente virtual.
- [x] Instalar Django (`pip install django`).
- [x] Criar projeto Django `finanpy` (`django-admin startproject finanpy .`).
- [x] Validar que `python manage.py runserver` funciona.

- [x] Configurar `core/settings.py`:
  - [x] Adicionar `INSTALLED_APPS` básicos (django.contrib.*).
  - [x] Configurar `LANGUAGE_CODE = 'pt-br'`.
  - [x] Configurar `TIME_ZONE = 'America/Sao_Paulo'` (ou outro fuso desejado).
  - [x] Definir `USE_TZ = True`.
  - [x] Configurar `TEMPLATES` com diretório `templates/` na raiz do projeto.
  - [x] Configurar `STATIC_URL` e, se necessário, `STATICFILES_DIRS`.

#### 1.2 Criação das apps

- [x] Criar app `users` (`python manage.py startapp users`).
- [x] Criar app `profiles` (`python manage.py startapp profiles`).
- [x] Criar app `accounts` (`python manage.py startapp accounts`).
- [x] Criar app `categories` (`python manage.py startapp categories`).
- [x] Criar app `transactions` (`python manage.py startapp transactions`).
- [x] Adicionar todas as apps em `INSTALLED_APPS` no `settings.py`.

#### 1.3 Estrutura de templates e static [x]

- [x] Criar pasta `templates/` na raiz do projeto.
- [x] Criar subpasta `templates/core/` para páginas globais (ex.: home, dashboard).
- [x] Criar subpastas por app (ex.: `templates/users/`, `templates/accounts/`).
- [x] Criar pasta `static/` na raiz para arquivos estáticos.
- [x] Configurar `STATICFILES_DIRS` se for necessário (`[BASE_DIR / "static"]`).
- [x] Testar renderização de um template simples usando `render()` em uma view.

#### 1.4 Integração inicial do TailwindCSS [x]

- [x] Instalar TailwindCSS (via npm ou binário local).
- [x] Criar arquivo `tailwind.config.js`.
- [x] Configurar `content` do Tailwind para incluir templates Django (`"templates/**/*.html"`).
- [x] Criar arquivo `assets/css/input.css` com:
  - [x] `@tailwind base;`
  - [x] `@tailwind components;`
  - [x] `@tailwind utilities;`
- [x] Configurar script de build (ex.: `npx tailwindcss -i ./assets/css/input.css -o ./static/css/styles.css --watch`).
- [x] Rodar build inicial e garantir que `styles.css` é gerado.
- [x] Referenciar `styles.css` em `base.html` usando `{% load static %}`.

---

### Sprint 2 – Autenticação, custom User e landing page

#### 2.1 Custom User (login por email) [x]

- [x] No app `users`, criar model custom `User` herdando de `AbstractUser`.
- [x] Remover dependência de `username` como identificador principal.
- [x] Definir `email` como `USERNAME_FIELD`.
- [x] Definir `REQUIRED_FIELDS = []` (ou conforme necessário).
- [x] Adicionar campos `created_at` e `updated_at` no modelo `User`.
- [x] Criar `UserManager` customizado se necessário para criação por email.
- [x] Atualizar `AUTH_USER_MODEL = 'users.User'` em `settings.py`.
- [x] Rodar `python manage.py makemigrations users`.
- [x] Rodar `python manage.py migrate`.

#### 2.2 Views e URLs de autenticação [x]

- [x] Criar view de cadastro (`SignupView`) em `users/views.py` usando `FormView` ou `CreateView`.
- [x] Implementar formulário de cadastro com email, senha e confirmação de senha.
- [x] Utilizar `LoginView` do Django para login baseado em email.
- [x] Configurar `AuthenticationForm` customizado, se necessário, para usar email.
- [x] Configurar `LogoutView` para encerrar sessão.

- [x] Criar arquivo `users/urls.py` com rotas:
  - [x] `/login/` → `LoginView`.
  - [x] `/logout/` → `LogoutView`.
  - [x] `/cadastro/` → `SignupView`.
- [x] Incluir `users/urls.py` em `core/urls.py` com namespace `users`.

#### 2.3 Templates de autenticação

- [ ] Criar `templates/base.html` com:
  - [ ] Estrutura básica HTML5.
  - [ ] Inclusão de `{% load static %}`.
  - [ ] Link para `/static/css/styles.css`.
  - [ ] Navbar simples com logo "Finanpy" e links "Entrar" e "Cadastre-se" (quando usuário anônimo).
  - [ ] Blocos `{% block content %}` para conteúdo principal.

- [ ] Criar `templates/users/login.html`:
  - [ ] Estender `base.html`.
  - [ ] Formulário estilizado com Design System (inputs, labels, botão primário).
  - [ ] Placeholders e labels em português brasileiro.
  - [ ] Exibição de mensagens de erro de validação.

- [ ] Criar `templates/users/signup.html`:
  - [ ] Estender `base.html`.
  - [ ] Formulário com campos email, senha, confirmação de senha.
  - [ ] Exibir erros campo a campo, seguindo estilo do design system.

#### 2.4 Landing page pública

- [ ] Criar view `home` em `core/views.py`.
- [ ] Criar template `templates/core/home.html`:
  - [ ] Seção hero com título principal (ex.: "Organize suas finanças com o Finanpy").
  - [ ] Subtítulo explicativo.
  - [ ] Botão "Cadastre-se" (link para rota de cadastro).
  - [ ] Botão "Entrar" (link para rota de login).
  - [ ] Uso de gradiente e tema escuro conforme design system.

- [ ] Adicionar rota `''` (raiz) em `core/urls.py` apontando para `home`.

---

### Sprint 3 – Models de domínio (profiles, accounts, categories, transactions)

#### 3.1 Model Profile

- [ ] Em `profiles/models.py`, criar model `Profile` com:
  - [ ] FK para `users.User` (`OneToOneField`).
  - [ ] Campo `full_name` (`CharField`).
  - [ ] Campos `created_at`, `updated_at` (`DateTimeField` com `auto_now_add`/`auto_now`).
- [ ] Criar `__str__` retornando nome do usuário ou `full_name`.
- [ ] Registrar model no `profiles/admin.py`.
- [ ] Criar migrações (`makemigrations` e `migrate`).

#### 3.2 Model Account

- [ ] Em `accounts/models.py`, criar model `Account`:
  - [ ] FK `user` para `users.User`.
  - [ ] Campo `name` (`CharField`).
  - [ ] Campo `balance` (`DecimalField` com `max_digits` e `decimal_places` adequados).
  - [ ] Campos `created_at`, `updated_at`.
- [ ] Definir `__str__` exibindo nome da conta.
- [ ] Registrar model em `accounts/admin.py`.
- [ ] Migrar.

#### 3.3 Model Category

- [ ] Em `categories/models.py`, criar model `Category`:
  - [ ] FK `user` para `users.User`.
  - [ ] Campo `name`.
  - [ ] Campo `type` com choices `entrada` e `saida`.
  - [ ] Campos `created_at`, `updated_at`.
- [ ] Registrar em `categories/admin.py`.
- [ ] Migrar.

#### 3.4 Model Transaction

- [ ] Em `transactions/models.py`, criar model `Transaction`:
  - [ ] FK `user` para `users.User`.
  - [ ] FK `account` para `Account`.
  - [ ] FK `category` para `Category`.
  - [ ] Campo `amount` (`DecimalField`).
  - [ ] Campo `date` (`DateField`).
  - [ ] Campo `description` (`CharField` ou `TextField`, opcional).
  - [ ] Campos `created_at`, `updated_at`.
- [ ] Criar `__str__` exibindo categoria + valor + data.
- [ ] Registrar em `transactions/admin.py`.
- [ ] Migrar.

---

### Sprint 4 – CRUDs e telas básicas

#### 4.1 CRUD de contas

- [ ] Criar views baseadas em classe em `accounts/views.py`:
  - [ ] `AccountListView` (lista contas do usuário logado).
  - [ ] `AccountCreateView`.
  - [ ] `AccountUpdateView`.
  - [ ] `AccountDeleteView`.

- [ ] Garantir uso de `LoginRequiredMixin` em todas as views.
- [ ] Filtrar objetos por `user=request.user`.

- [ ] Criar `accounts/urls.py` com rotas:
  - [ ] `/contas/` → lista.
  - [ ] `/contas/nova/` → criação.
  - [ ] `/contas/<pk>/editar/` → edição.
  - [ ] `/contas/<pk>/excluir/` → exclusão.

- [ ] Incluir `accounts/urls.py` em `core/urls.py`.

- [ ] Criar templates:
  - [ ] `accounts/account_list.html`:
    - [ ] Tabela ou cards listando contas.
    - [ ] Botão "Nova conta".
  - [ ] `accounts/account_form.html`:
    - [ ] Formulário com campos estilizados segundo design system.
  - [ ] `accounts/account_confirm_delete.html`:
    - [ ] Mensagem clara "Você tem certeza que deseja excluir esta conta?".

#### 4.2 CRUD de categorias

- [ ] Criar views em `categories/views.py` (List/Create/Update/Delete).
- [ ] Proteger com `LoginRequiredMixin` e filtragem por `request.user`.
- [ ] Criar `categories/urls.py` com padrões similares a contas.
- [ ] Criar templates:
  - [ ] `categories/category_list.html`.
  - [ ] `categories/category_form.html`.
  - [ ] `categories/category_confirm_delete.html`.

#### 4.3 CRUD de transações

- [ ] Criar views em `transactions/views.py`:
  - [ ] `TransactionListView`.
  - [ ] `TransactionCreateView`.
  - [ ] `TransactionUpdateView`.
  - [ ] `TransactionDeleteView`.

- [ ] Garantir que formulários listem apenas contas e categorias do usuário autenticado.
- [ ] Criar `transactions/urls.py`.
- [ ] Criar templates:
  - [ ] `transactions/transaction_list.html` (listagem, filtros básicos).
  - [ ] `transactions/transaction_form.html`.
  - [ ] `transactions/transaction_confirm_delete.html`.

---

### Sprint 5 – Dashboard, lógica de saldo e UX

#### 5.1 Lógica de saldo

- [ ] Definir estratégia para atualização de `balance` em `Account`:
  - [ ] Ao criar transação de entrada, somar valor ao saldo da conta.
  - [ ] Ao criar transação de saída, subtrair valor.
  - [ ] Ao editar transação, recalcular diferença.
  - [ ] Ao excluir transação, desfazer efeito no saldo.

- [ ] Implementar essa lógica:
  - [ ] Via override de `form_valid` nas CBVs, **ou**
  - [ ] Via signals (`post_save`, `post_delete`) em `transactions/signals.py` (se for usado, respeitar regra de colocar signals em `signals.py`).
  - [ ] Garantir que essas regras são aplicadas sempre para o usuário correto.

#### 5.2 Dashboard

- [ ] Criar view `DashboardView` (ex.: em `core/views.py`).
- [ ] Proteger com `LoginRequiredMixin`.
- [ ] No `get_context_data`:
  - [ ] Calcular total de entradas (somatório de transações de categorias tipo entrada).
  - [ ] Calcular total de saídas (somatório de categorias tipo saída).
  - [ ] Calcular saldo total (ex.: soma dos saldos das contas).
  - [ ] Obter últimas X transações.

- [ ] Criar template `templates/core/dashboard.html`:
  - [ ] Cards com:
    - [ ] "Total de entradas".
    - [ ] "Total de saídas".
    - [ ] "Saldo total".
  - [ ] Listagem das últimas transações em tabela ou lista.
  - [ ] Usar classes do design system (cards, textos, cores).

#### 5.3 Aplicar design system globalmente

- [ ] Revisar `base.html`:
  - [ ] Garantir uso correto de background escuro.
  - [ ] Navbar com gradiente ou detalhe de destaque.
  - [ ] Tipografia consistente.

- [ ] Revisar todos os formulários:
  - [ ] Aplicar classes de input padrão.
  - [ ] Garantir espaçamento entre campos (`space-y-4`).

- [ ] Revisar listas (contas, categorias, transações):
  - [ ] Usar tabelas ou cards com cores consistentes.
  - [ ] Ações (editar/excluir) com botões utilizando estilo secundário/perigo.

---

### Sprint 6 – Planejamento de testes e Docker (futuro)

> Não implementar agora; apenas documentar plano.

#### 6.1 Planejamento de testes

- [ ] Documentar em um arquivo (ex.: `docs/tests-plan.md`):
  - [ ] Lista de casos de teste de autenticação.
  - [ ] Lista de casos de teste de contas.
  - [ ] Lista de casos de teste de transações.
  - [ ] Lista de casos de teste de cálculo de saldo.

#### 6.2 Planejamento de Docker

- [ ] Documentar em `docs/docker-plan.md`:
  - [ ] Imagem base Python.
  - [ ] Passos de instalação de dependências.
  - [ ] Comando para rodar migrações.
  - [ ] Comando para iniciar o servidor (`gunicorn` ou `runserver` em dev).c
