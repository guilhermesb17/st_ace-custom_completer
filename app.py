import streamlit as st
from streamlit_ace import st_ace
import json

# Função para gerar o completer personalizado
def custom_completer(words):
    completions = [{"name": word, "value": word, "meta": "custom"} for word in words]
    completer = {"getCompletions": f"function(editor, session, pos, prefix, callback) {{callback(null, {json.dumps(completions)});}}"}
    return json.dumps(completer)

# Lista de palavras personalizadas para autocompletar
custom_words = ["minha_palavra1", "minha_palavra2", "minha_palavra3"]
 
sistema = 'teste_sistema'
# Criação do editor ACE no Streamlit
code = st_ace(language='sql',custom_word=custom_words, sistem=sistema)

