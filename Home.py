import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="BIOMOVE", layout="wide")

# Título principal
st.markdown("<h1 style='color:white;'>BIOMOVE</h1>", unsafe_allow_html=True)

# Menu horizontal com abas
selected = option_menu(
    menu_title=None,  # remove o título do menu
    options=["Home", "BioMove", "Atualização Semanal", "Relatórios", "Cronograma"],
    orientation="horizontal",
    default_index=0,
    icons=["house", "bar-chart", "calendar", "file-earmark-text", "clock"],
    styles={
        "container": {"padding": "0!important", "background-color": "#0E1117"},
        "icon": {"color": "white", "font-size": "16px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "color": "white"},
        "nav-link-selected": {"background-color": "#0E1117", "color": "red", "border-bottom": "2px solid red"},
    }
)

# Conteúdo de acordo com o menu selecionado
if selected == "Home":
    st.title("Página Inicial")
    st.write("Conteúdo da Home.")
elif selected == "BioMove":
    st.title("BioMove")
    st.write("Conteúdo do projeto BioMove.")
elif selected == "Atualização Semanal":
    st.title("Atualização Semanal")
    st.write("Conteúdo das atualizações semanais.")
elif selected == "Relatórios":
    st.title("Relatórios")
    st.write("Conteúdo dos relatórios.")
elif selected == "Cronograma":
    st.title("Cronograma")
    st.write("Conteúdo do cronograma.")


# Rodapé
st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 200%;
            background-color: #A9A9A9;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 16px;
        }
    </style>
    <div class="footer">
        UTFPR - Universidade Tecnológica Federal do Paraná - Engenharia Eletrônica - 2025
    </div>
""", unsafe_allow_html=True)
