import streamlit.components.v1 as components

text = 'Meu carro de ouro'
codeJs = f"""
const htmlContent = {text};
navigator.clipboard.writeText(htmlContent);
"""

jsHtml = f"""
<script>
    {codeJs};
</script>
"""
components.html(jsHtml)
