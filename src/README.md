# Aplicação da Lary

A interface segue um fluxo simples:

```text
pergunta → Streamlit → Ollama local → regras da Lary + base de dados → resposta
```

O programa carrega `AGENTS.md`, a persona, a base de conhecimento, os dados
fornecidos durante a conversa e as fontes oficiais. O modelo recebe instruções explícitas para não
inventar informações nem recomendar produtos específicos.

## Execução

Na raiz do projeto:

```bash
pip install -r requirements.txt
ollama pull gpt-oss:20b
ollama serve
streamlit run src/app.py
```

Para usar outro modelo já instalado:

```bash
OLLAMA_MODEL=nome-do-modelo streamlit run src/app.py
```

No PowerShell:

```powershell
$env:OLLAMA_MODEL = "nome-do-modelo"
streamlit run src/app.py
```

Não são necessárias chaves de API. O Ollama e o modelo rodam localmente.
