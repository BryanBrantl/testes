import streamlit as st

st.set_page_config(page_title="Site Customizado", layout="wide")

# Simula navegação horizontal
menu = st.radio(
    "Navegação",
    ["Home", "Página 1", "Página 2"],
    horizontal=True
)

st.markdown("---")

if menu == "Home":
    st.title("Página Inicial")
    st.write("Bem-vindo ao site com navegação horizontal.")
elif menu == "Página 1":
    st.title("Página 1")
    st.write("Conteúdo da Página 1.")
elif menu == "Página 2":
    st.title("Página 2")
    st.write("Conteúdo da Página 2.")
