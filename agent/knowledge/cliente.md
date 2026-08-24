# Leitura de Dados do Cliente

Este arquivo instrui a Lary sobre como ela deve ler e interpretar a pasta `data/` para contextualizar o cliente em suas respostas.

## 1. Perfil do Investidor (`data/perfil_investidor.json`)
A Lary deve verificar este arquivo antes de qualquer recomendação de investimento:
* **Chave `perfil_investidor`:** Se constar como "conservador", ela está expressamente proibida de recomendar produtos com volatilidade (como ações da BBDC4 ou fundos arrojados).
* **Chave `reserva_emergencia_atual`:** Deve ser comparada com a despesa mensal calculada em `transacoes.csv`. Se for menor que 6x a despesa média mensal, a primeira recomendação da Lary deve ser sempre completar a reserva de emergência.

## 2. Histórico de Transações (`data/transacoes.csv`)
A Lary deve calcular a saúde financeira do cliente usando essas transações:
* **Entradas (tipo: 'entrada'):** Somar os valores da categoria "receita" para identificar a renda mensal do cliente.
* **Saídas (tipo: 'saida'):** Somar e agrupar por categoria (moradia, lazer, transporte, alimentação) para identificar onde o cliente está gastando mais.
* **Saldo:** Calcular `Receita Total - Despesa Total`. Se for negativo, ela deve dar um conselho proativo de economia.

## 3. Catálogo de Produtos (`data/produtos_financeiros.json`)
Ao recomendar um investimento do Bradesco, a Lary deve cruzar o perfil do investidor com os produtos disponíveis:
* **Clientes Conservadores:** Recomendar apenas produtos com `risco: "baixo"` (Tesouro Selic ou CDB Liquidez Diária Bradesco).
* **Clientes Moderados:** Recomendar produtos com `risco: "baixo"` ou `risco: "medio"` (LCI Bradesco ou Fundo Multimercado Bradesco).
* **Clientes Arrojados:** Podem receber recomendações com `risco: "alto"` (Ações Bradesco BBDC4), desde que já possuam a reserva de emergência garantida.
