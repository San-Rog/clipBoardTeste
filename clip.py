import streamlit.components.v1 as components

text = 'Meu carro de ouro - sdfsdflkslfksdlfksdlksdlfksdf'
codeJs = f"""
navigator.clipboard.writeText({text});
"""

jsHtml = f"""
<script>
    {codeJs};
</script>
"""
components.html(jsHtml)
