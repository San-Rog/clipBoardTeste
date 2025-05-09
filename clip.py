import streamlit as st
import streamlit.components.v1 as components

text = 'Meu carro de ouro - ---------------------------------------------------------'
codeJs = f"""
navigator.clipboard.writeText({text});
"""

jsHtml = f"""
<script>
    {codeJs};
</script>
"""
components.html(jsHtml)
