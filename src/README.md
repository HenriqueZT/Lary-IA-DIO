# Código da Aplicação

Esta pasta é reservada para conter o código do seu agente financeiro, caso você decida implementar uma interface funcional ou integrar a Lary com APIs reais de modelos de linguagem (como Gemini ou OpenAI) em uma fase futura.

## Estrutura Sugerida para Implementação

Caso opte por codificar a Lary no futuro, a estrutura recomendada é:

```
src/
├── app.py              # Interface visual do chatbot (ex: Streamlit ou Gradio)
├── agente.py           # Lógica do agente (integração de dados e prompts com LLMs)
├── config.py           # Configurações de chaves de API e variáveis de ambiente
└── requirements.txt    # Lista de dependências Python (bibliotecas necessárias)
```
