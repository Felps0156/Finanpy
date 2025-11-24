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

### Sprint 2 – Autenticação, custom User e landing page [x]

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

#### 2.3 Templates de autenticação [x]

- [x] Criar `templates/base.html` com:
  - [x] Estrutura básica HTML5.
  - [x] Inclusão de `{% load static %}`.
  - [x] Link para `/static/css/styles.css`.
  - [x] Navbar simples com logo "Finanpy" e links "Entrar" e "Cadastre-se" (quando usuário anônimo).
  - [x] Blocos `{% block content %}` para conteúdo principal.

- [x] Criar `templates/users/login.html`:
  - [x] Estender `base.html`.
  - [x] Formulário estilizado com Design System (inputs, labels, botão primário).
  - [x] Placeholders e labels em português brasileiro.
  - [x] Exibição de mensagens de erro de validação.

- [x] Criar `templates/users/signup.html`:
  - [x] Estender `base.html`.
  - [x] Formulário com campos email, senha, confirmação de senha.
  - [x] Exibir erros campo a campo, seguindo estilo do design system.

#### 2.4 Landing page pública [x]

- [x] Criar view `home` em `core/views.py`.
- [x] Criar template `templates/core/home.html`:
  - [x] Seção hero com título principal (ex.: "Organize suas finanças com o Finanpy").
  - [x] Subtítulo explicativo.
  - [x] Botão "Cadastre-se" (link para rota de cadastro).
  - [x] Botão "Entrar" (link para rota de login).
  - [x] Uso de gradiente e tema escuro conforme design system.

- [x] Adicionar rota `''` (raiz) em `core/urls.py` apontando para `home`.

---

### Sprint 3 – Models de domínio (profiles, accounts, categories, transactions) [x]

#### 3.1 Model Profile [x]

- [x] Em `profiles/models.py`, criar model `Profile` com:
  - [x] FK para `users.User` (`OneToOneField`).
  - [x] Campo `full_name` (`CharField`).
  - [x] Campos `created_at`, `updated_at` (`DateTimeField` com `auto_now_add`/`auto_now`).
- [x] Criar `__str__` retornando nome do usuário ou `full_name`.
- [x] Registrar model no `profiles/admin.py`.
- [x] Criar migrações (`makemigrations` e `migrate`).

#### 3.2 Model Account [x]

- [x] Em `accounts/models.py`, criar model `Account`:
  - [x] FK `user` para `users.User`.
  - [x] Campo `name` (`CharField`).
  - [x] Campo `balance` (`DecimalField` com `max_digits` e `decimal_places` adequados).
  - [x] Campos `created_at`, `updated_at`.
- [x] Definir `__str__` exibindo nome da conta.
- [x] Registrar model em `accounts/admin.py`.
- [x] Migrar.

#### 3.3 Model Category [x]

- [x] Em `categories/models.py`, criar model `Category`:
  - [x] FK `user` para `users.User`.
  - [x] Campo `name`.
  - [x] Campo `type` com choices `entrada` e `saida`.
  - [x] Campos `created_at`, `updated_at`.
- [x] Registrar em `categories/admin.py`.
- [x] Migrar.

#### 3.4 Model Transaction [x]

- [x] Em `transactions/models.py`, criar model `Transaction`:
  - [x] FK `user` para `users.User`.
  - [x] FK `account` para `Account`.
  - [x] FK `category` para `Category`.
  - [x] Campo `amount` (`DecimalField`).
  - [x] Campo `date` (`DateField`).
  - [x] Campo `description` (`CharField` ou `TextField`, opcional).
  - [x] Campos `created_at`, `updated_at`.
- [x] Criar `__str__` exibindo categoria + valor + data.
- [x] Registrar em `transactions/admin.py`.
- [x] Migrar.

---

### Sprint 4 – CRUDs e telas básicas [x]

#### 4.1 CRUD de contas [x]

- [x] Criar views baseadas em classe em `accounts/views.py`:
  - [x] `AccountListView` (lista contas do usuário logado).
  - [x] `AccountCreateView`.
  - [x] `AccountUpdateView`.
  - [x] `AccountDeleteView`.

- [x] Garantir uso de `LoginRequiredMixin` em todas as views.
- [x] Filtrar objetos por `user=request.user`.

- [x] Criar `accounts/urls.py` com rotas:
  - [x] `/contas/` → lista.
  - [x] `/contas/nova/` → criação.
  - [x] `/contas/<pk>/editar/` → edição.
  - [x] `/contas/<pk>/excluir/` → exclusão.

- [x] Incluir `accounts/urls.py` em `core/urls.py`.

- [x] Criar templates:
  - [x] `accounts/account_list.html`:
    - [x] Tabela ou cards listando contas.
    - [x] Botão "Nova conta".
  - [x] `accounts/account_form.html`:
    - [x] Formulário com campos estilizados segundo design system.
  - [x] `accounts/account_confirm_delete.html`:
    - [x] Mensagem clara "Você tem certeza que deseja excluir esta conta?".

#### 4.2 CRUD de categorias [x]

- [x] Criar views em `categories/views.py` (List/Create/Update/Delete).
- [x] Proteger com `LoginRequiredMixin` e filtragem por `request.user`.
- [x] Criar `categories/urls.py` com padrões similares a contas.
- [x] Criar templates:
  - [x] `categories/category_list.html`.
  - [x] `categories/category_form.html`.
  - [x] `categories/category_confirm_delete.html`.

#### 4.3 CRUD de transações [x]

- [x] Criar views em `transactions/views.py`:
  - [x] `TransactionListView`.
  - [x] `TransactionCreateView`.
  - [x] `TransactionUpdateView`.
  - [x] `TransactionDeleteView`.

- [x] Garantir que formulários listem apenas contas e categorias do usuário autenticado.
- [x] Criar `transactions/urls.py`.
- [x] Criar templates:
  - [x] `transactions/transaction_list.html` (listagem, filtros básicos).
  - [x] `transactions/transaction_form.html`.
  - [x] `transactions/transaction_confirm_delete.html`.

---

### Sprint 5 – Dashboard, lógica de saldo e UX [x]

#### 5.1 Lógica de saldo [x]

- [x] Definir estratégia para atualização de `balance` em `Account`:
  - [x] Ao criar transação de entrada, somar valor ao saldo da conta.
  - [x] Ao criar transação de saída, subtrair valor.
  - [x] Ao editar transação, recalcular diferença.
  - [x] Ao excluir transação, desfazer efeito no saldo.

- [x] Implementar essa lógica:
  - [x] Via override de `form_valid` nas CBVs, **ou**
  - [x] Via signals (`post_save`, `post_delete`) em `transactions/signals.py` (se for usado, respeitar regra de colocar signals em `signals.py`).
  - [x] Garantir que essas regras são aplicadas sempre para o usuário correto.

#### 5.2 Dashboard [x]

- [x] Criar view `DashboardView` (ex.: em `core/views.py`).
- [x] Proteger com `LoginRequiredMixin`.
- [x] No `get_context_data`:
  - [x] Calcular total de entradas (somatório de transações de categorias tipo entrada).
  - [x] Calcular total de saídas (somatório de categorias tipo saída).
  - [x] Calcular saldo total (ex.: soma dos saldos das contas).
  - [x] Obter últimas X transações.

- [x] Criar template `templates/core/dashboard.html`:
  - [x] Cards com:
    - [x] "Total de entradas".
    - [x] "Total de saídas".
    - [x] "Saldo total".
  - [x] Listagem das últimas transações em tabela ou lista.
  - [x] Usar classes do design system (cards, textos, cores).

#### 5.3 Aplicar design system globalmente [x]

- [x] Revisar `base.html`:
  - [x] Garantir uso correto de background escuro.
  - [x] Navbar com gradiente ou detalhe de destaque.
  - [x] Tipografia consistente.

- [x] Revisar todos os formulários:
  - [x] Aplicar classes de input padrão.
  - [x] Garantir espaçamento entre campos (`space-y-4`).

- [x] Revisar listas (contas, categorias, transações):
  - [x] Usar tabelas ou cards com cores consistentes.
  - [x] Ações (editar/excluir) com botões utilizando estilo secundário/perigo.

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
