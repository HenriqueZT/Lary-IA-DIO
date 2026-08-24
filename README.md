# Lary — Mentora Financeira Educacional

Projeto desenvolvido para o Lab **Construa Seu Assistente Virtual Com
Inteligência Artificial**, da DIO. A Lary ajuda uma pessoa iniciante a entender
um orçamento fictício, estimar uma referência de reserva de emergência e aprender
conceitos básicos de investimento sem inventar taxas ou ofertas.

> Projeto educacional, sem vínculo ou integração oficial com o Bradesco. Não
> constitui recomendação, consultoria ou oferta de investimento.

## Como executar a Lary

A aplicação usa Streamlit e um modelo local executado pelo Ollama. Não é
necessária chave de API.

```bash
pip install -r requirements.txt
ollama pull gpt-oss:20b
ollama serve
streamlit run src/app.py
```

Testes técnicos, sem necessidade de Ollama:

```bash
python -m unittest discover -s tests -v
```

Também é possível abrir a pasta diretamente em uma ferramenta compatível com
`AGENTS.md`, como Codex, Claude Code ou Cursor, e conversar com a Lary sem usar a
interface Streamlit.

Perguntas sugeridas:

```text
Como está meu orçamento?
Quanto falta para completar minha reserva de emergência?
Devo comprar ações agora?
O que é liquidez?
Quanto rende um CDB do Bradesco hoje?
```

A resposta deve usar os arquivos da pasta `data/`, respeitar as restrições do
agente e admitir quando não houver informação suficiente.

Essa é a mesma lógica de engenharia de contexto usada pelo agente Edu do
repositório de referência: instruções + dados do cliente + base de conhecimento +
resposta educacional. A aplicação mantém `AGENTS.md` como fonte principal das
regras e usa o Ollama local para gerar a resposta.

## Os 6 passos do desafio

| Etapa | Evidência |
|---|---|
| 1. Documentação | `docs/01-documentacao-agente.md` |
| 2. Base de conhecimento | `docs/02-base-conhecimento.md`, `agent/knowledge/` e `data/` |
| 3. Prompts | `AGENTS.md`, `agent/persona.md` e `docs/03-prompts.md` |
| 4. Aplicação funcional | `src/app.py`; instruções em `src/README.md` |
| 5. Avaliação e métricas | `tests/test_app.py` e `docs/04-metricas.md` |
| 6. Pitch | `docs/05-pitch.md` |

## Estrutura

```text
Lary-IA-DIO/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── agent/
│   ├── persona.md
│   └── knowledge/
│       ├── cliente.md
│       └── conceitos.md
├── data/
│   ├── README.md
│   ├── fontes_oficiais.json
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
├── requirements.txt
├── src/
│   ├── README.md
│   └── app.py
└── tests/
    └── test_app.py
```

## Dados e fontes

Nome, perfil, patrimônio, transações e atendimentos são sintéticos. Os conceitos
financeiros foram revisados em 24/08/2026 usando páginas oficiais do
[Tesouro Direto](https://www.tesourodireto.com.br/sobre-o-tesouro/regras-e-regulamento),
[FGC](https://www.fgc.org.br/garantia-fgc/sobre-a-garantia-fgc) e
[B3](https://www.b3.com.br/pt_br/noticias/suitability.htm).

Taxas, preços, tributação, limites e condições podem mudar. O agente não consulta
informações em tempo real; decisões finais devem ser confirmadas com a instituição
responsável ou profissional habilitado.

## Limitações

A qualidade da resposta depende do modelo local escolhido. Não há acesso a conta
bancária, atualização automática de fontes ou execução de operações financeiras.
