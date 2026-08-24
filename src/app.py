"""Interface simples da Lary com Streamlit e Ollama local."""

import csv
import json
import os
from pathlib import Path

import requests
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:20b")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(name: str):
    with (DATA / name).open(encoding="utf-8") as file:
        return json.load(file)


def read_csv(name: str):
    with (DATA / name).open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


@st.cache_data
def load_context() -> str:
    profile = read_json("perfil_investidor.json")
    products = read_json("produtos_financeiros.json")
    sources = read_json("fontes_oficiais.json")
    transactions = read_csv("transacoes.csv")
    history = read_csv("historico_atendimento.csv")

    derived = {"status": "Aguardando informações fornecidas pela pessoa."}
    if transactions:
        income = sum(float(item["valor"]) for item in transactions if item["tipo"] == "entrada")
        expenses = sum(float(item["valor"]) for item in transactions if item["tipo"] == "saida")
        reserve_target = expenses * 6
        reserve_current = profile.get("reserva_emergencia_atual")
        derived = {
            "entradas": round(income, 2),
            "saidas": round(expenses, 2),
            "saldo": round(income - expenses, 2),
            "referencia_reserva_6_meses": round(reserve_target, 2),
            "valor_para_atingir_referencia": (
                round(max(reserve_target - float(reserve_current), 0), 2)
                if reserve_current is not None
                else None
            ),
        }

    return "\n\n".join(
        [
            "REGRAS PRINCIPAIS:\n" + read_text(ROOT / "AGENTS.md"),
            "PERSONA:\n" + read_text(ROOT / "agent" / "persona.md"),
            "CONCEITOS:\n" + read_text(ROOT / "agent" / "knowledge" / "conceitos.md"),
            "REGRAS DE LEITURA:\n" + read_text(ROOT / "agent" / "knowledge" / "cliente.md"),
            "PERFIL INICIAL (PODE ESTAR VAZIO):\n" + json.dumps(profile, ensure_ascii=False, indent=2),
            "TRANSAÇÕES INICIAIS (PODEM ESTAR VAZIAS):\n" + json.dumps(transactions, ensure_ascii=False, indent=2),
            "ATENDIMENTOS INICIAIS (PODEM ESTAR VAZIOS):\n" + json.dumps(history, ensure_ascii=False, indent=2),
            "CÁLCULOS DERIVADOS:\n" + json.dumps(derived, ensure_ascii=False, indent=2),
            "CATÁLOGO EDUCACIONAL:\n" + json.dumps(products, ensure_ascii=False, indent=2),
            "FONTES OFICIAIS:\n" + json.dumps(sources, ensure_ascii=False, indent=2),
        ]
    )


def ask_lary(question: str, conversation: list[dict]) -> str:
    prompt = f"""
Use exclusivamente o contexto abaixo para responder como Lary.

Regras obrigatórias:
- ensine, mas não recomende a compra de produto específico;
- não invente taxas, ofertas, transações ou informações ausentes;
- comece sem presumir dados sobre a pessoa;
- use como contexto pessoal apenas o que ela informou no histórico da conversa;
- quando faltar um dado necessário, faça uma pergunta curta por vez;
- não transforme exemplos hipotéticos em dados reais da pessoa;
- se faltar informação, diga que não possui informação suficiente;
- não solicite nem repita senhas, tokens, CPF ou dados bancários;
- responda em português do Brasil, de forma simples e em até três parágrafos.

CONTEXTO:
{load_context()}

HISTÓRICO DESTA CONVERSA:
{json.dumps(conversation, ensure_ascii=False, indent=2)}

PERGUNTA:
{question}
"""

    response = requests.post(
        OLLAMA_URL,
        json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    result = response.json()
    if not result.get("response"):
        raise RuntimeError("O Ollama não retornou uma resposta válida.")
    return result["response"].strip()


st.set_page_config(page_title="Lary", page_icon="💰")
st.title("💰 Lary — Mentora Financeira Educacional")
st.caption("Seus dados não são predefinidos nem gravados. A Lary não realiza operações ou recomenda produtos específicos.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input("Digite sua dúvida sobre finanças"):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Lary está analisando os dados..."):
                answer = ask_lary(question, st.session_state.messages[:-1])
        except requests.RequestException:
            answer = (
                "Não consegui acessar o Ollama local. Confirme se ele está em execução "
                f"e se o modelo `{OLLAMA_MODEL}` foi instalado."
            )
        except (OSError, ValueError, RuntimeError) as error:
            answer = f"Não foi possível carregar a base com segurança: {error}"

        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
