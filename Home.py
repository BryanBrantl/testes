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
    st.title("Atualizações Semanais")
    
    def bloco_atualizacao(titulo, texto):
        st.markdown(f"""
            <div style="background-color:#1e1e1e; padding:20px; margin-bottom:10px; border-radius:10px; border-left: 5px solid red;">
                <h4 style="color:white;">{titulo}</h4>
                <p style="color:gray;">{texto}</p>
            </div>
        """, unsafe_allow_html=True)
    
    bloco_atualizacao("📅 Semana 1 - 20/05/2025", """
   - Realizados testes nos principais componentes do carrinho (motor DC, ESP32 e ponte H), sem identificação de defeitos.<br>
   - Conduzido estudo sobre softwares de modelagem 3D. Optou-se pela utilização do Eagle para o desenvolvimento do carrinho e do sistema EMG.<br>
   - Modelo do site finalizado.
   - Proposta e cronograma revisados e atualizados conforme a devolutiva, já disponíveis no site.<br>
   - Decisões sobre o projeto: Definido que será utilizado baterias 18650 (4.2v) para alimentação dos sistemas.<br>
   - Construção do esquemático EMG:
    """)
    
    bloco_atualizacao("📅 Semana 2 - 27/05/2025", """
    - Realizado testes com protótipo 1.<br>
    - Melhorias na eficiência do algoritmo de leitura.<br>
    - Planejamento da próxima sprint.
    """)
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
            width: 100%;
            background-color: #0E1117;
            color: #888888;;
            text-align: center;
            padding: 10px;
            font-size: 15px;
        }
    </style>
    <div class="footer">
        <hr>
        UTFPR - Universidade Tecnológica Federal do Paraná - Engenharia Eletrônica - 2025
    </div>
""", unsafe_allow_html=True)
