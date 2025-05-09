import streamlit.components.v1 as components

text = 'masmsmsmsmsm'

js_code = f"""
<script>
    navigator.clipboard.writeText({text});
</script>
"""
components.html(js_code)
