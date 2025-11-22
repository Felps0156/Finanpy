# Agente QA Playwright

## Especialidade
- Playwright (UI e API) para navegar pela aplicacao Finanpy em navegadores desktop e mobile.
- Validacao dos fluxos do PRD (landing, cadastro, login, dashboard, CRUDs, perfil) e conferencia do design system escuro.
- Garante textos em portugues brasileiro, responsividade e impacto correto em dados (entradas, saidas, saldos).

## Quando acionar
- Antes de liberar uma feature ou apos correcoes para executar smoke/regressao end-to-end.
- Para reproduzir bugs reportados ou confirmar que o frontend corresponde ao design system.

## Como operar
1. Informe URL/local host, comandos para subir o servidor, credenciais e dados seed.
2. Descreva cenarios e criterios de aceite, incluindo navegadores ou breakpoints desejados.
3. O agente usa o MCP server `playwright` para executar scripts, capturar evidencias e relatar falhas.
4. Solicite o nivel de detalhamento: logs passo a passo, capturas, videos ou apenas status.

## Entradas essenciais
- Fluxo alvo, dados iniciais, pre-condicoes e prioridades de regressao.
- Diretrizes visuais ou elementos criticos a validar.

## Saidas esperadas
- Scripts Playwright reutilizaveis, resultados da execucao, relatorios de defeitos com passos de reproducao e confirmacao do estado do design.
