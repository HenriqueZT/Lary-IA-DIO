"""Testes locais da interface e da montagem de contexto da Lary."""

import unittest
from unittest.mock import patch
from pathlib import Path

import requests
from streamlit.testing.v1 import AppTest


APP_FILE = Path(__file__).resolve().parents[1] / "src" / "app.py"


class FakeResponse:
    def raise_for_status(self):
        return None

    def json(self):
        return {"response": "Resposta educacional de teste."}


class LaryAppTests(unittest.TestCase):
    def test_interface_loads(self):
        app = AppTest.from_file(APP_FILE).run(timeout=30)
        self.assertFalse(app.exception)
        self.assertEqual(len(app.chat_input), 1)

    def test_empty_context_and_rules_reach_model(self):
        with patch("requests.post", return_value=FakeResponse()) as request:
            app = AppTest.from_file(APP_FILE).run(timeout=30)
            app.chat_input[0].set_value("Quanto falta para a reserva?").run(timeout=30)

        self.assertFalse(app.exception)
        payload = request.call_args.kwargs["json"]
        prompt = payload["prompt"]
        self.assertEqual(payload["model"], "gpt-oss:20b")
        self.assertIn("Aguardando informações fornecidas pela pessoa", prompt)
        self.assertIn('"renda_mensal": null', prompt)
        self.assertIn('"perfil_investidor": null', prompt)
        self.assertIn("não recomende", prompt)
        self.assertIn("comece sem presumir dados", prompt)
        self.assertTrue(any(item.value == "Resposta educacional de teste." for item in app.markdown))

    def test_conversation_is_sent_as_temporary_context(self):
        with patch("requests.post", return_value=FakeResponse()) as request:
            app = AppTest.from_file(APP_FILE).run(timeout=30)
            app.chat_input[0].set_value("Minha renda mensal é R$ 3.000").run(timeout=30)
            app.chat_input[0].set_value("Como posso organizar meu orçamento?").run(timeout=30)

        prompt = request.call_args.kwargs["json"]["prompt"]
        self.assertIn("Minha renda mensal é R$ 3.000", prompt)
        self.assertIn("Como posso organizar meu orçamento?", prompt)

    def test_missing_ollama_has_friendly_message(self):
        with patch("requests.post", side_effect=requests.ConnectionError):
            app = AppTest.from_file(APP_FILE).run(timeout=30)
            app.chat_input[0].set_value("Como está meu orçamento?").run(timeout=30)

        self.assertFalse(app.exception)
        text = " ".join(item.value for item in app.markdown)
        self.assertIn("Não consegui acessar o Ollama local", text)


if __name__ == "__main__":
    unittest.main()
