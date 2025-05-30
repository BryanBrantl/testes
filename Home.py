import streamlit as stMore actions
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="BIOMOVE", layout="wide")

# CSS para os botões com hover (borda e texto mudam, fundo continua)
# e outros estilos
st.markdown("""
    <style>
        .my-button,
        a.my-button,                 /* Aplica a tags <a> com a classe .my-button */
        a.my-button:link,            /* Links não visitados */
        a.my-button:visited          /* Links visitados */
        {
            background-color: #1c1f26;
            color: white !important;     /* Força a cor branca para o texto */
            border: 2px solid white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            text-align: center;
            text-decoration: none;       /* Remove o sublinhado do link */
            display: inline-block;       /* Garante que padding e etc. funcionem bem em <a> */
            transition: 0.3s;
        }

        .my-button:hover,
        a.my-button:hover              /* Estilo hover para tags <a> com a classe */
        {
            background-color: #1c1f26; /* Mantém o fundo no hover, se não quiser que mude */
            color: #00CED1 !important;    /* Força a cor ciano no hover */
            border-color: #00CED1;
        }

        /* Se você tiver outros estilos globais, eles continuam aqui... */
        /* Exemplo: .info-block-title que usamos antes (se ainda for necessário)
        .info-block-title {
            color: #00CED1;
            margin-bottom: 5px;
        }
        .info-block-button-container {
            margin-top: 15px;
            margin-bottom: 10px;
        }
        */
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
    st.markdown("<h1 style='text-align: center; color: #008080;'>RELATÓRIOS</h1>", unsafe_allow_html=True)

    def bloco_relatorio_final(titulo_bloco, texto_descricao, texto_botao, url_botao):
        """
        Cria um bloco de conteúdo estilizado com título, descrição e um botão clicável.
        """
        texto_descricao_html = texto_descricao.replace('\n', '<br>')
        st.markdown(f"""
            <div style="background-color:#1e1e1e; padding:20px; margin-bottom:10px; border-radius:10px; border-left: 5px solid teal;">
                <h4 style="color:white;">{titulo_bloco}</h4>
                <p style="color:gray;">{texto_descricao_html}</p>
                <div style="margin-top: 15px; margin-bottom: 5px;"> <a href="{url_botao}" target="_blank" class="my-button" style="text-decoration: none; display: inline-block;">
                        {texto_botao}
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # URL fornecida para o relatório final
    link_do_relatorio_final = "https://docs.google.com/spreadsheets/d/1Fb5_otX8z50tuy9RbcGGC89BLKfErs_SCnML-JGeyQU/edit?usp=sharing"

    # Chamando a função para criar o bloco do Relatório Final
    bloco_relatorio_final(
        titulo_bloco="Relatório Final do Projeto",
        texto_descricao="""O relatório final consolida todos os resultados, análises e conclusões do projeto BioMove.
Acesse o documento completo para mais detalhes.""", # \n será convertido para <br>
        texto_botao="ABRIR RELATÓRIO FINAL",
        url_botao=link_do_relatorio_final
    )

    # Exemplo de como adicionar outro bloco de relatório, se necessário:
    # link_relatorio_parcial = "SUA_URL_PARA_OUTRO_RELATORIO"
    # bloco_relatorio_final(
    #     titulo_bloco="Relatório Parcial Q1",
    #     texto_descricao="Este relatório cobre as atividades e progresso do primeiro trimestre do projeto.",
    #     texto_botao="ABRIR RELATÓRIO PARCIAL Q1",
    #     url_botao=link_relatorio_parcial
    # )

############################################################################################
###################################   CRONOGRAMA    ########################################
elif selected == "Cronograma":
 st.markdown("""
        <h1 style='text-align: center; color: #008080 ;'>
            CRONOGRAMA - alterar
        </h1>
    """, unsafe_allow_html=True)


 link3 = "https://docs.google.com/spreadsheets/d/1Fb5_otX8z50tuy9RbcGGC89BLKfErs_SCnML-JGeyQU/edit?usp=sharing"

 bloco_relatorio_final(
     titulo_bloco="Relatório Parcial Q1",
     texto_descricao="Este relatório cobre as atividades e progresso do primeiro trimestre do projeto.",
     texto_botao="ABRIR RELATÓRIO PARCIAL Q1",
     url_botao=link_relatorio_parcial
 )

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
