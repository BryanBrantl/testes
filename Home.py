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
########################################################### linhas  #####################################################################
## Linha padrão do HTML
## st.markdown("<hr>", unsafe_allow_html=True)
##    
##    # Linha customizada com a cor do seu projeto
## st.markdown("<hr style='border: 1px solid #008080;'>", unsafe_allow_html=True)
##    
##    # Outro exemplo de linha mais grossa e com margens
## st.markdown("<hr style='height:2px; background-color:#008080; border:none; margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)
#####################################################################################################################################################


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
    B1col1, B1col2 = st.columns(2)  
    with B1col1:
        st.write("")
        st.write("")
        st.image(img5, width=500)   
##
    with B1col2:
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
# Linha padrão do HTML
        st.markdown("<hr>", unsafe_allow_html=True)
        texto_proposta_escopo = """
        <div style='text-align: justify;'>
            <h2 style='color: #008080; text-align: center;'>Proposta e Escopo</h2>
            <p>
                O sistema BioMove utiliza <strong style='color: #008080;'>sensores EMG </strong> (montados a partir de amplificadores de instrumentação e filtros analógicos) para captar sinais musculares do paciente.
            </p>
            <p>
                Estes sinais são processados (amplificação, filtragem, retificação e análise digital) para serem transformados em comandos de controle de um carrinho autônomo.
            </p>
            <p>
                O projeto prioriza a qualidade do controle baseado em EMG, em vez de funcionalidades avançadas no robô, concentrando esforços na aquisição e interpretação dos sinais.
            </p>
        </div>
    """
    
    # 2. Defina o texto para o segundo bloco (Funcionamento Básico)
    texto_funcionamento = """
        <div style='text-align: justify;'>
            <h2 style='color: #008080; text-align: center;'>Funcionamento Básico</h2>
            <p>
                Eletrodos são posicionados em músculos-alvo (por exemplo, bíceps direito e esquerdo) para captar o sinal EMG e processá-lo, identificando a ativação muscular.
            </p>
            <p>
                Os sinais são traduzidos em comandos para mover o carrinho, conforme a lógica:
            </p>
            <ul>
                <li><strong>Ambos músculos ativados:</strong> carrinho anda para frente.</li>
                <li><strong>Somente esquerdo ativado:</strong> carrinho vira à direita.</li>
                <li><strong>Somente direito ativado:</strong> carrinho vira à esquerda.</li>
                <li><strong>Sem ativação:</strong> carrinho permanece parado.</li>
            </ul>
            <p>
                A comunicação entre o módulo EMG e o carrinho é feita via <strong style='color: #008080;'>Wi-Fi</strong> ou <strong style='color: #008080;'>Bluetooth</strong>, já que ambos os módulos rodam com um ESP32.
            </p>
        </div>
    """
    
    # 3. Construção do Layout no Streamlit
    
    # Bloco 1: Texto na Esquerda, Imagem na Direita
    B2col1, B2col2 = st.columns([2, 1.5]) # Dando mais espaço para o texto
    with B2col1:
        st.markdown(texto_proposta_escopo, unsafe_allow_html=True)
    
    with B2col2:
        # Centralizando a imagem
        vazia1, img_col, vazia2 = st.columns([1, 4, 1])
        with img_col:
            st.image(img5) 
    
    # Adiciona uma linha para separar os blocos
   # st.divider()
    
    # Bloco 2: Imagem na Esquerda, Texto na Direita
    B3col1, B3col2 = st.columns([1.5, 2]) # Dando mais espaço para o texto
    with B3col1:
        # Centralizando a imagem
        vazia3, img_col2, vazia4 = st.columns([1, 4, 1])
        with img_col2:
            st.image(img5)
    
    with B3col2:
        st.markdown(texto_funcionamento, unsafe_allow_html=True)
    
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
