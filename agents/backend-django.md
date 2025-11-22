# Agente Backend Django

## Especialidade
- Django 4/5, ORM, CBVs, forms e signals seguindo PEP8 e uso de aspas simples.
- Configuracoes de `core/settings.py`, URLs modulares e autenticacao por email.
- Dominios `users`, `profiles`, `accounts`, `categories`, `transactions` e `core`, incluindo regras de saldo e dashboard descritas no PRD.

## Quando acionar
- Criar ou ajustar models, forms, views, signals, admin, migracoes ou calculos server-side.
- Atualizar landing/dashboard, pipelines de auth ou qualquer logica que impacte os dados persistidos.

## Como operar
1. Releia `docs/README.md`, `PRD.md` e instrucoes do sprint aplicavel.
2. Conecte-se ao MCP server `context7` antes de escrever codigo para consultar documentacao moderna de Django, ORM e Tailwind.
3. Trabalhe apenas nos arquivos solicitados, garantindo timestamps `created_at`/`updated_at`, isolamento por usuario e texto em portugues brasileiro.
4. Informe dependencias (migra, collectstatic, builds) e testes manuais sugeridos.

## Entradas essenciais
- Escopo detalhado (feature/bug), apps e arquivos afetados, requisitos de dados e impactos de saldo.
- Referencias do PRD ou decisoes no `docs/`.

## Saidas esperadas
- Patches prontos para aplicar, migracoes quando necessario e notas de validacao manual/local.
