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
img5 = Image.open("image/gamificacao.jpg")

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
        st.image(img1, width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'> Bryan Alexandre de Lima Brantl</span></strong><br><br>
                 RA: 2414139<br><br>
                 E-mail: brantl@alunos.utfpr.edu.br<br><br>
                 Contato: (41) 99278-3929
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.image(img2, width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>João Roberto Klassen</span></strong><br>
                <br>
                RA: 2414155<br>
                <br>
                E-mail: joaoklassen@alunos.utfpr.edu.br<br>
                <br>
                Contato: (41) 99742-4536
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.image(img3, width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>Leonardo Amancio</span></strong><br>
                <br>
                RA: 2402580<br>
                <br>
                E-mail: leonardoamancio@alunos.utfpr.edu.br<br>
                <br>
                Contato: (41) 99805-1279
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col4:
        st.image(img4, width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>Luiz Prado</span></strong><br>
                <br>
                RA: 2402629<br>
                <br>
                E-mail: luizoliveira.2002@alunos.utfpr.edu.br<br>
                <br>
                Contato: (41) 99815-6532
            </div>
            """,
            unsafe_allow_html=True
        )
############################################################################################
######################################   BIOMOVE    ########################################

elif selected == "BioMove": 
    st.markdown("""
        <h1 style='text-align: center; color: #008080 ;'>
            OVERVIEW DO PROJETO
        </h1>
    """, unsafe_allow_html=True)
##        
    Bcol1, Bcol2 = st.columns(2)  
    with Bcol1:
        st.image(img5, width=500)   
##
    with Bcol2:
        st.markdown("""
            <div style='text-align: justify;'>
                <h2 style='color: #008080; text-align: center;'>Problemática e Objetivo</h2>
                <p>
                    O projeto BioMove surge para <span style='text-decoration: underline; text-decoration-color: #008080;'>melhorar a interação do paciente com a fisioterapia</span>, tornando-a mais motivadora e eficaz, com objetivo de <span style='text-decoration: underline; text-decoration-color: #008080;'>acelerar o progresso de reabilitação</span>. Muitos pacientes desistem antes de alcançar melhora significativa devido a:
                </p>
                <ul>
                    <li>Métodos tradicionais repetitivos e pouco engajadores;</li>
                    <li>Dificuldade em perceber progresso imediato, causando desmotivação;</li>
                    <li>Falta de acesso a equipamentos modernos que estimulem o tratamento.</li>
                </ul>
                <p>
                    A proposta central é <span style='text-decoration: underline; text-decoration-color: #008080;'>estabelecer uma base de gamificação</span> para o tratamento, inspirando-se em exemplos como o Instituto Albert Einstein, para tornar o processo mais dinâmico e envolvente.
                </p>
            </div>
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
    st.markdown("<h1 style='text-align: center; color: #008080;'>RELATÓRIOS</h1>", unsafe_allow_html=True)

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
