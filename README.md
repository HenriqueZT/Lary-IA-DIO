# Lary - Mentora Financeira Inteligente (Bradesco)

Este repositório contém a definição e a base de conhecimento da **Lary**, uma agente de IA projetada para atuar como mentora financeira pessoal para clientes do Bradesco.

O projeto foi construído de forma **minimalista**, seguindo a estrutura padrão de agentes em markdown para ser executada diretamente em harnesses de inteligência artificial (como Antigravity, Claude Code, Cursor ou Gemini CLI).

---

## 📁 Estrutura do Projeto

```
lary-agent/
├── README.md               ← Apresentação do projeto e como usar
├── AGENTS.md               ← Fonte única de verdade: regras e diretrizes da Lary
├── CLAUDE.md               ← Instruções rápidas para comandos do harness
├── agent/
│   ├── persona.md          ← Personalidade, tom de voz e valores da Lary
│   └── knowledge/
│       ├── conceitos.md    ← Base de conhecimento educacional de finanças
│       └── cliente.md      ← Diretrizes de como a Lary lê os dados do cliente
└── data/                   ← Dados mockados (transações, perfil e catálogo)
    ├── perfil_investidor.json
    ├── produtos_financeiros.json
    └── transacoes.csv
```

---

## 🤖 Como a Lary Funciona

A Lary utiliza a engenharia de prompts baseada em arquivos de contexto:
1. **Identidade e Regras:** Definidas no `AGENTS.md`.
2. **Personalidade:** O tom de voz didático e acolhedor vem do `agent/persona.md`.
3. **Conhecimento Técnico:** A Lary aprende conceitos financeiros (como reserva de emergência e juros) em `agent/knowledge/conceitos.md`.
4. **Análise de Dados:** Ela sabe como cruzar as transações do cliente com o perfil dele através de `agent/knowledge/cliente.md` utilizando os arquivos presentes na pasta `data/`.

---

## 📈 Casos de Uso Principais
* **Montagem da Reserva de Emergência:** A Lary ajuda a calcular quanto poupar e sugere CDBs de liquidez diária do Bradesco.
* **Explicação de Conceitos:** Traduz termos complicados (ex: CDB, liquidez, IPCA) com analogias simples do cotidiano.
* **Segurança e Perfil:** Ela barra proativamente recomendações arrojadas (ações) para clientes de perfil conservador.