# 2. Base de conhecimento

## Contexto pessoal progressivo

| Arquivo | Uso |
|---|---|
| `data/perfil_investidor.json` | Estrutura vazia dos dados que podem ser informados |
| `data/transacoes.csv` | Cabeçalho para transações, sem lançamentos predefinidos |
| `data/historico_atendimento.csv` | Cabeçalho para atendimentos, sem histórico predefinido |

O projeto não contém personagem. Na conversa, a Lary começa sem conhecer renda,
despesas, patrimônio, objetivo ou perfil. Ela usa temporariamente somente o que a
pessoa fornecer e não grava essas informações nos arquivos.

## Informações verificáveis

`data/produtos_financeiros.json` não é uma prateleira comercial. É um catálogo
educacional de categorias, sem taxa prometida ou disponibilidade presumida.
`data/fontes_oficiais.json` registra as páginas oficiais usadas e a data da revisão.

Foram priorizadas fontes do Tesouro Direto, FGC e B3. Como regras e produtos
podem mudar, o agente orienta a consulta atualizada antes de qualquer decisão.

## Processo de atualização

1. Revisar os links em `fontes_oficiais.json`.
2. Confirmar se cada afirmação continua publicada pela instituição responsável.
3. Atualizar `verificado_em` e o catálogo.
4. Repetir os cenários de `docs/04-metricas.md` no agente.
5. Registrar data, resultado observado e eventuais correções.
