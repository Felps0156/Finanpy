# AGENTS.md

Documento de alinhamento rapido para colaboradores assistidos por IA no projeto **Finanpy**. Use estas diretrizes como briefing inicial antes de gerar codigo, textos ou assets.

## 1. Contexto do produto
- Finanpy e uma aplicacao web full-stack em Django para controle de financas pessoais com fluxo simples: landing publica -> cadastro/login -> dashboard -> CRUDs.
- Publico-alvo: pessoas fisicas, profissionais autonomos e estudantes que buscam organizar receitas e despesas sem ferramentas complexas.
- Diferenciais: tema escuro moderno com TailwindCSS, interface 100% em PT-BR, arquitetura modular por dominio e uso intenso de recursos nativos do Django.

## 2. Escopo funcional principal (PRD)
| Area | Requisitos chave |
| --- | --- |
| Autenticacao | Cadastro e login por email/senha usando user model customizado; redirect para dashboard apos login; logout leva de volta para landing. |
| Perfis | Cada usuario possui profile 1-1 com nome completo editavel e isolamento total dos dados. |
| Contas bancarias | CRUD completo (lista, criar, editar, excluir) com campos nome e saldo; listagem limitada ao owner. |
| Categorias | CRUD de categorias com nome e tipo (`entrada`/`saida`). |
| Transacoes | CRUD com campos conta, categoria, valor, data, descricao opcional; tipo deriva da categoria; atualizar saldo das contas em todas as operacoes. |
| Dashboard | Mostrar total de entradas, saidas, saldo somado das contas e ultimas transacoes em layout responsivo. |
| Landing page | Pagina publica com hero, resumo do produto e CTAs "Cadastre-se" e "Entrar". |
| Regras gerais | Textos em PT-BR, modelos com `created_at`/`updated_at`, layout dark compartilhado. |

## 3. Requisitos nao-funcionais essenciais
- Stack: Python 3.11+, Django 4+, SQLite em dev, TailwindCSS compilado para `static/`.
- Padrões: seguir PEP8, usar aspas simples, priorizar Class Based Views e recursos nativos do framework.
- Responsividade: abordagem mobile-first, gradientes e tokens definidos no design system do PRD.
- Sem testes automatizados ou Docker nas primeiras sprints (apenas planejamento futuro).

## 4. Design system (resumo operativo)
- **Cores:** fundo `bg-zinc-950`, cards `bg-zinc-900`, textos `text-slate-50/400`, destaque primario `from-indigo-600 to-purple-600`.
- **Componentes:** cards `rounded-2xl border-zinc-800 p-6`, inputs `bg-zinc-900 border-zinc-700`, botoes principais com gradiente indigo->purple.
- **Tipografia:** fonte sans (Inter/afim), titulos `text-xl md:text-2xl font-semibold`.
- **Layouts:** grid do dashboard `grid-cols-1 md:grid-cols-3 gap-6`, navbar fixa com fundo transluxido escuro.

## 5. Estrutura inicial do repositorio
| Caminho | Funcao esperada |
| --- | --- |
| `core/` | Configuracoes globais Django, urls raiz, views compartilhadas (home/dashboard). |
| `users/` | Custom user model baseado em email e fluxos de auth (login, signup, logout). |
| `profiles/` | Perfil 1-1 com dados adicionais do usuario. |
| `accounts/` | Models, views e templates relacionados a contas bancarias. |
| `categories/` | Domínio de categorias de lancamentos. |
| `transactions/` | Transacoes financeiras e regras de saldo. |
| `agents/` | Pasta reservada para prompts/automacoes (nao descrita no PRD, verificar antes de editar). |
| `docs/` | Documentacao complementar (`README`, arquitetura, setup, guias). |
| `templates/`, `static/` | Devem consolidar o design system global (criar se ainda nao existirem). |

## 6. Prioridades de implementacao (roadmap resumido)
1. **Sprint 1** – Ajustar `core/settings.py`, registrar apps, configurar templates/static e pipeline do Tailwind.
2. **Sprint 2** – Custom user com email, views/templates de auth e landing page hero.
3. **Sprint 3** – Models de dominio (profile, account, category, transaction) com migrations e admin.
4. **Sprint 4** – CRUDs completos para contas, categorias e transacoes usando CBVs e templates seguindo o design system.
5. **Sprint 5** – Regras de saldo, dashboard com agregacoes e refinamento visual global.
6. **Sprint 6** – Planejar testes e Docker em arquivos dedicados dentro de `docs/` (sem implementar ainda).

## 7. Referencias rapidas
- PRD completo: `PRD.md`.
- Indice da documentacao auxiliar: `docs/README.md` (aponta para visao geral, setup, arquitetura e padroes).
- Banco local: `db.sqlite3` (usar apenas em dev).
- Dependencias: `requirements.txt`.

## 8. Como colaborar como assistente
- Respeite o escopo e as prioridades listadas; evite propor features fora do PRD.
- Sempre escreva textos e mensagens na UI em portugues brasileiro.
- Preserve o tema escuro e as classes Tailwind prescritas ao criar novos templates.
- Ao manipular regras de saldo, mantenha a consistencia via signals em `transactions/signals.py` ou override das CBVs, conforme diretrizes do PRD.
- Documente decisoes tecnicas adicionais dentro de `docs/` para manter o time alinhado.
