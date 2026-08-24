# Leitura dos dados do cliente fictício

Todos os dados pessoais, transações e atendimentos da pasta `data/` são
sintéticos e existem somente para demonstrar o protótipo.

## Ordem de leitura

1. Leia `perfil_investidor.json` e confirme objetivo, perfil e aceitação de risco.
2. Leia `transacoes.csv`; some entradas e saídas sem criar lançamentos ausentes.
3. Calcule saldo como entradas menos saídas.
4. Calcule a referência de reserva como seis vezes as despesas do período.
5. Consulte `produtos_financeiros.json` apenas como catálogo educacional.
6. Use `fontes_oficiais.json` para mostrar de onde vêm as afirmações verificáveis.

## Regras de decisão

- Se `aceita_risco` for `false`, essa recusa prevalece sobre uma classificação
  geral como “moderado”. Não sugira renda variável ou fundos de maior risco.
- Se a reserva estiver abaixo da referência, priorize organização e liquidez.
- Nunca informe rentabilidade, preço, taxa, carência, disponibilidade ou
  tributação atual que não esteja sendo consultada em fonte oficial naquele momento.
- Diferencie explicação de categoria de uma recomendação ou oferta comercial.
- Quando faltar dado, diga claramente que não há informação suficiente.
- Não execute operações nem solicite senha, token, CPF ou dados bancários.

## Dados derivados do cenário atual

- Entradas: R$ 5.000,00
- Saídas: R$ 2.279,90
- Saldo: R$ 2.720,10
- Referência de reserva (6 meses): R$ 13.679,40
- Reserva fictícia atual: R$ 10.000,00
- Diferença para a referência: R$ 3.679,40

Esses valores devem ser recalculados pela aplicação; não devem substituir a
leitura dos arquivos.
