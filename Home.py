import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="BIOMOVE", layout="wide")

# CSS para os botões com hover (borda e texto mudam, fundo continua)
st.markdown("""
    <style>
        .my-button {
            background-color: #1c1f26;
            color: white;
            border: 2px solid white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            text-align: center;
            transition: 0.3s;
        }

        .my-button:hover {
            color: #00CED1;
            border-color: #00CED1;
        }
    </style>
""", unsafe_allow_html=True)

############################################################## MODELO BOTAO ######################################################################
##
##    <button class="my-button" onclick="window.open('https://www.google.com', '_blank')">
##        ABRIR RELATORIO
##    </button> 
##
########################################################### Título principal #####################################################################

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
        "nav-link-selected": {"background-color": "#0E1117", "color": "teal", "border-bottom": "2px solid teal"},
    }
)


############################################ IMAGENS ############################################
img1 = Image.open("image/foto_01.png")
img2 = Image.open("image/foto_02.png")
img3 = Image.open("image/foto_03.png")
img4 = Image.open("image/foto_04.png")

############################################ Conteúdo de acordo com o menu selecionado ############################################
################################################################################################   HOME    #################################
if selected == "Home":
    st.markdown("""
        <h1 style='text-align: center; color: #008080 ;'>
            HOME
        </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h1 style='text-align: center; color: #008080 ;'>
            MEMBROS
        </h1>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)  
    with col1:
        st.image(img1, caption='Coluna 3 (width=100)', width=300)
    with col2:
        #st.image(img2, caption='Coluna 2 (mesma imagem, parecerá menor se a imagem original for grande)')
        st.image(img2, caption='Coluna 3 (width=100)', width=300)
    # Você também pode usar o parâmetro 'width' dentro das colunas
    with col3:
        st.image(img3, caption='Coluna 3 (width=100)', width=300)
    with col4:
        st.image(img4, caption='Coluna 3 (width=100)', width=300)

############################################################################################
######################################   BIOMOVE    ########################################

elif selected == "BioMove":
        st.markdown("""
        <h1 style='text-align: center; color: #008080 ;'>
            OVERVIEW DO PROJETO
        </h1>
    """, unsafe_allow_html=True)

############################################################################################
##########################   ATUALIZAÇÃO SEMANAL    ########################################

elif selected == "Atualização Semanal":
    st.title("Atualizações Semanais")
    
    def bloco_atualizacao(titulo, texto):
        st.markdown(f"""
            <div style="background-color:#1e1e1e; padding:20px; margin-bottom:10px; border-radius:10px; border-left: 5px solid teal;">
                <h4 style="color:white;">{titulo}</h4>
                <p style="color:gray;">{texto}</p>
            </div>
        """, unsafe_allow_html=True)
     
    bloco_atualizacao(" Semana 2 - 27/05/2025", """
    - Definido a utilização de um Kit chassi para a construção do carrinho. <br>
    - Montagem do sensor EMG em protoboard baseado no esquemático da semana anterior. <br>
    - Validamos o sinal no osciloscópio, detectado presença de ruído da rede. <br>
    - Definido a necessidade de implementar mais filtros no circuito para reduzir o ruído. <br>
    - Circuito montado em protoboard: <br>
    """)
    
    bloco_atualizacao(" Semana 1 - 20/05/2025", """
   - Realizados testes nos principais componentes do carrinho (motor DC, ESP32 e ponte H), sem identificação de defeitos.<br>
   - Conduzido estudo sobre softwares de modelagem 3D. Optou-se pela utilização do Eagle para o desenvolvimento do carrinho e do sistema EMG.<br>
   - Modelo do site finalizado.
   - Proposta e cronograma revisados e atualizados conforme a devolutiva, já disponíveis no site.<br>
   - Decisões sobre o projeto: Definido que será utilizado baterias 18650 (4.2v) para alimentação dos sistemas.<br>
   - Construção do esquemático EMG:
    """)
    

############################################################################################
###################################   RELATORIOS    ########################################

elif selected == "Relatórios":
    st.markdown("""
        <h1 style='text-align: center; color: #008080;'>Relatórios</h1>
        <hr style='border: 2px solid #008080 ; margin-top: 10px; margin-bottom: 30px;'/>
    """, unsafe_allow_html=True)

    # Estilo CSS para os botões e caixas
st.markdown("""
    <style>
        .card {
            border: 1px solid #00bfa6;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 25px;
            background-color: #f0f0f0;
            color: #202020; /* COR DO TEXTO */
        }
        .my-button {
            background-color: #00bfa6;
            color: white;
            padding: 10px 20px;
            text-align: center;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .my-button:hover {
            background-color: #009e8a;
        }
        .disabled-button {
            background-color: #cccccc;
            color: #444444;
            padding: 10px 20px;
            text-align: center;
            border-radius: 8px;
            font-size: 16px;
            cursor: not-allowed;
        }
    </style>
""", unsafe_allow_html=True)

    # Proposta de Projeto
    st.markdown("""
        <div class="card">
            <h3>📄 Proposta de Projeto</h3>
            <p>Nesta seção, está disponibilizada a proposta de projeto do <strong>BioMove</strong>.<br>
            O documento reúne informações detalhadas sobre o escopo do projeto, sendo esta proposta já aprovada.</p>
            <button class="my-button" onclick="window.open('https://docs.google.com/document/d/1uJpoXcehrK1Lv2cPMxUtHkvSNNtmgnatSJdmxfzy8gc/edit?usp=sharing', '_blank')">
                📂 Acessar Proposta
            </button>
        </div>
    """, unsafe_allow_html=True)

    # Relatório Final
    st.markdown("""
        <div class="card">
            <h3>📘 Relatório Final</h3>
            <p>Você poderá acessar o relatório final do projeto assim que for disponibilizado.</p>
            <div class="disabled-button">⏳ Relatório Final (em breve)</div>
        </div>
    """, unsafe_allow_html=True)

############################################################################################
###################################   CRONOGRAMA    ########################################
elif selected == "Cronograma":
    st.markdown("""
        <h1 style='text-align: center; color: #008080;'>
            Cronograma | Orçamento
        </h1>
        <hr style='border: 2px solid #888; margin-top: 10px; margin-bottom: 30px;'/>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Cronograma:

    Nesta seção, está disponibilizado o cronograma completo juntamente com os custos previstos e realizados do projeto BioMove.  
    Você pode acessar o documento completo clicando no botão abaixo:
    """)

    st.markdown("""
        <a href="https://docs.google.com/spreadsheets/d/1Fb5_otX8z50tuy9RbcGGC89BLKfErs_SCnML-JGeyQU/edit?usp=sharing" target="_blank" class="custom-button">
            Abrir Cronograma e Orçamento
        </a>
    """, unsafe_allow_html=True)

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
