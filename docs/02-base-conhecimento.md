# 2. Base de conhecimento

## Dados sintéticos

| Arquivo | Uso |
|---|---|
| `data/perfil_investidor.json` | Perfil, objetivo e tolerância a risco do personagem |
| `data/transacoes.csv` | Entradas e saídas do cenário |
| `data/historico_atendimento.csv` | Contexto fictício de atendimentos anteriores |

O nome “João Silva”, sua profissão, patrimônio e movimentações são fictícios.
Nenhum dado representa uma pessoa real.

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
