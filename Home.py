import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from pathlib import Path

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

# Função para converter uma imagem local para Base64 (usada em outras partes, mantida por segurança)
def img_to_base64(img_path):
    try:
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return f"data:image/png;base64,{encoded}"
    except FileNotFoundError:
        return ""

########################################################### Título principal #####################################################################
st.markdown("<h1 style='color:white;'>BIOMOVE</h1>", unsafe_allow_html=True)

# Menu horizontal com abas
selected = option_menu(
    menu_title=None,
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
# Usando um bloco try-except para evitar que o app quebre se uma imagem não for encontrada
try:
    img1 = Image.open("image/foto_01.png")
    img2 = Image.open("image/foto_02.png")
    img3 = Image.open("image/foto_03.png")
    img4 = Image.open("image/foto_04.png")
    img5 = Image.open("image/gamificacao.jpg")
    img6 = Image.open("image/Musculo_0.png")
    img7 = Image.open("image/Musculo_1.png")
except FileNotFoundError:
    st.error("Uma ou mais imagens não foram encontradas. Verifique os caminhos dos arquivos.")
    # Atribui None para evitar mais erros
    img1, img2, img3, img4, img5, img6, img7 = (None,)*7

############################################ Conteúdo de acordo com o menu selecionado ############################################
################################################################################################   HOME    #################################
if selected == "Home" and all([img1, img2, img3, img4]):
    st.markdown("<h1 style='text-align: center; color: #008080 ;'>MEMBROS</h1>", unsafe_allow_html=True)
    st.write("") # Espaço

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(img1, use_column_width=True)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'> Bryan Alexandre de Lima Brantl</span></strong><br><br>
                 RA: 2414139<br>
                 E-mail: brantl@alunos.utfpr.edu.br<br>
                 Contato: (41) 99278-39299
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.image(img2, use_column_width=True)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>João Roberto Klassen</span></strong><br><br>
                RA: 2414155<br>
                E-mail: joaoklassen@alunos.utfpr.edu.br<br>
                Contato: (41) 99742-4536
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        st.image(img3, use_column_width=True)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>Leonardo Amancio</span></strong><br><br>
                RA: 2402580<br>
                E-mail: leonardoamancio@alunos.utfpr.edu.br<br>
                Contato: (41) 99805-1279
            </div>
            """, unsafe_allow_html=True)
    
    with col4:
        st.image(img4, use_column_width=True)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>Luiz Prado</span></strong><br><br>
                RA: 2402629<br>
                E-mail: luizoliveira.2002@alunos.utfpr.edu.br<br>
                Contato: (41) 99815-6532
            </div>
            """, unsafe_allow_html=True)
############################################################################################
######################################   BIOMOVE    ########################################

elif selected == "BioMove" and all([img5, img6, img7]):
    st.markdown("<h1 style='text-align: center; color: #008080;'>OVERVIEW DO PROJETO</h1>", unsafe_allow_html=True)
    st.divider()

    # Bloco 1
    B1col1, B1col2 = st.columns(2)
    with B1col1:
        vazia, img_col_b1, vazia2 = st.columns([1, 4, 1])
        with img_col_b1:
            st.image(img5)
    with B1col2:
        st.markdown("""
            <div style='text-align: justify;'>
                <h2 style='color: #008080; text-align: center;'>Problemática e Objetivo</h2>
                <p>O projeto BioMove surge para <span style='text-decoration: underline; text-decoration-color: #008080;'>melhorar a interação do paciente com a fisioterapia</span>, tornando-a mais motivadora e eficaz, com objetivo de <span style='text-decoration: underline; text-decoration-color: #008080;'>acelerar o progresso de reabilitação</span>. Muitos pacientes desistem antes de alcançar melhora significativa devido a:</p>
                <ul>
                    <li>Métodos tradicionais repetitivos e pouco engajadores;</li>
                    <li>Dificuldade em perceber progresso imediato, causando desmotivação;</li>
                    <li>Falta de acesso a equipamentos modernos que estimulem o tratamento.</li>
                </ul>
                <p>A proposta central é <span style='text-decoration: underline; text-decoration-color: #008080;'>estabelecer uma base de gamificação</span> para o tratamento, inspirando-se em exemplos como o Instituto Albert Einstein, para tornar o processo mais dinâmico e envolvente.</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()

    # Bloco 2
    texto_proposta_escopo = """...""" # Mantido para não quebrar, mas pode ser removido se não for usado
    texto_funcionamento = """...""" # Mantido para não quebrar, mas pode ser removido se não for usado
    
    B2col1, B2col2 = st.columns([2, 1.5])
    with B2col1:
        st.markdown("""
            <div style='text-align: justify;'>
                <h2 style='color: #008080; text-align: center;'>Proposta e Escopo</h2>
                <p>O sistema BioMove utiliza <strong style='color: #008080;'>sensores EMG</strong> (montados a partir de amplificadores de instrumentação e filtros analógicos) para captar sinais musculares do paciente.</p>
                <p>Estes sinais são processados (amplificação, filtragem, retificação e análise digital) para serem transformados em comandos de controle de um carrinho autônomo.</p>
                <p>O projeto prioriza a qualidade do controle baseado em EMG, em vez de funcionalidades avançadas no robô, concentrando esforços na aquisição e interpretação dos sinais.</p>
            </div>
        """, unsafe_allow_html=True)
    with B2col2:
        vazia1, img_col, vazia2 = st.columns([1, 4, 1])
        with img_col:
            st.image(img6)
    
    st.divider()
    
    # Bloco 3
    B3col1, B3col2 = st.columns([1.5, 2])
    with B3col1:
        vazia3, img_col2, vazia4 = st.columns([1, 4, 1])
        with img_col2:
            st.image(img7)
    with B3col2:
        st.markdown("""
            <div style='text-align: justify;'>
                <h2 style='color: #008080; text-align: center;'>Funcionamento Básico</h2>
                <p>Eletrodos são posicionados em músculos-alvo (por exemplo, bíceps direito e esquerdo) para captar o sinal EMG e processá-lo, identificando a ativação muscular.</p>
                <p>Os sinais são traduzidos em comandos para mover o carrinho, conforme a lógica:</p>
                <ul>
                    <li><strong>Ambos músculos ativados:</strong> carrinho anda para frente.</li>
                    <li><strong>Somente esquerdo ativado:</strong> carrinho vira à direita.</li>
                    <li><strong>Somente direito ativado:</strong> carrinho vira à esquerda.</li>
                    <li><strong>Sem ativação:</strong> carrinho permanece parado.</li>
                </ul>
                <p>A comunicação entre o módulo EMG e o carrinho é feita via <strong style='color: #008080;'>Wi-Fi</strong> ou <strong style='color: #008080;'>Bluetooth</strong>, já que ambos os módulos rodam com um ESP32.</p>
            </div>
        """, unsafe_allow_html=True)
    
############################################################################################
##########################   ATUALIZAÇÃO SEMANAL    ########################################
elif selected == "Atualização Semanal":
    st.markdown("<h1 style='text-align: center; color: #008080;'>ATUALIZAÇÕES SEMANAIS</h1>", unsafe_allow_html=True)
    st.divider()

    # --- FUNÇÕES AUXILIARES PARA OS ESTILOS DOS BLOCOS ---

    # Função para um bloco que contém APENAS texto
    def bloco_completo(titulo, texto):
        st.markdown(f"""
            <div style="background-color:#1e1e1e; padding: 20px; margin-bottom: 20px; border-radius: 10px; border-left: 5px solid teal;">
                <h4 style="color:white;">{titulo}</h4>
                <p style="color:gray;">{texto}</p>
            </div>
        """, unsafe_allow_html=True)

    # Função para ABRIR um bloco que terá mais conteúdo (imagens, vídeos, etc.)
    def bloco_texto_inicial(titulo, texto):
        st.markdown(f"""
            <div style="background-color:#1e1e1e; padding: 20px; padding-bottom: 15px; border-radius: 10px 10px 0 0; border-left: 5px solid teal; margin-bottom: -2px;">
                <h4 style="color:white;">{titulo}</h4>
                <p style="color:gray;">{texto}</p>
            </div>
        """, unsafe_allow_html=True)

    # Função para FECHAR um bloco que teve conteúdo adicionado
    def base_bloco():
        st.markdown(f"""
            <div style="background-color:#1e1e1e; padding-top: 10px; border-radius: 0 0 10px 10px; border-left: 5px solid teal; margin-bottom: 20px;">
            </div>
        """, unsafe_allow_html=True)
    # ---------------------------------------------------

    # --- Semana 5 (Apenas Texto) ---
    bloco_completo("Semana 5 - 06/06/2025", """
    - <strong>[PLACEHOLDER]</strong> Nesta semana, o foco foi na correção da PCI e na integração do software de controle.<br>
    - Realizamos novos testes de soldagem e estamos validando o layout do circuito.<br>
    - Próximos passos: Finalizar a PCI funcional e iniciar a integração com o sensor EMG.
    """)

    # --- Semana 4 (Apenas Texto) ---
    bloco_completo("Semana 4 - 30/05/2025", """
    - Avançamos na produção da placa de circuito impresso (PCI), mas enfrentamos contratempos no roteamento e soldagem que comprometeram o funcionamento da primeira versão.<br>
    - Estamos corrigindo o layout da PCI e aprimorando o processo de soldagem.<br><br>
    - Em paralelo, o software para controlar o carrinho via joystick no celular (Bluetooth) foi desenvolvido e finalizado com sucesso.
    """)

    # --- Semana 3 (Texto + Imagem) ---
    bloco_texto_inicial("Semana 3 - 23/05/2025", """
    - Finalizada a montagem do chassi e estrutura do carrinho.<br>
    - Adicionados novos filtros ao esquemático do EMG para melhorar a qualidade do sinal.<br>
    - O circuito EMG foi montado em placa perfurada, oferecendo mais estabilidade que a protoboard.<br>
    - O filtro Notch não apresentou o resultado esperado, levando à hipótese de usar filtros digitais no futuro.<br>
    - Circuito montado em placa perfurada:
    """)
    vazia1, col_img1, vazia2 = st.columns([1, 1.5, 1])
    with col_img1:
        st.image("caminho/para/imagem_placa_perfurada.png", caption="Circuito EMG em placa perfurada")
    base_bloco()

    # --- Semana 2 (Texto + Imagem) ---
    bloco_texto_inicial("Semana 2 - 27/05/2025", """
    - Definido a utilização de um Kit chassi para a construção do carrinho. <br>
    - Montagem do sensor EMG em protoboard baseado no esquemático da semana anterior. <br>
    - Validamos o sinal no osciloscópio, detectado presença de ruído da rede. <br>
    - Definido a necessidade de implementar mais filtros no circuito para reduzir o ruído. <br>
    - Circuito montado em protoboard:
    """)
    vazia3, col_img2, vazia4 = st.columns([1, 1.5, 1])
    with col_img2:
        st.image("caminho/para/imagem_protoboard.png", caption="Protótipo em protoboard")
    base_bloco()
    
    # --- Semana 1 (Texto + Imagem) ---
    bloco_texto_inicial("Semana 1 - 20/05/2025", """
    - Realizados testes nos principais componentes do carrinho (motor DC, ESP32 e ponte H), sem identificação de defeitos.<br>
    - Conduzido estudo sobre softwares de modelagem 3D. Optou-se pela utilização do Eagle para o desenvolvimento do carrinho e do sistema EMG.<br>
    - Modelo do site finalizado.<br>
    - Proposta e cronograma revisados e atualizados conforme a devolutiva, já disponíveis no site.<br>
    - Decisões sobre o projeto: Definido que será utilizado baterias 18650 (4.2v) para alimentação dos sistemas.<br>
    - Construção do esquemático EMG:
    """)
    vazia5, col_img3, vazia6 = st.columns([1, 1.5, 1])
    with col_img3:
        st.image("caminho/para/imagem_esquematico.png", caption="Esquema do circuito EMG")
    base_bloco()

############################################################################################
###################################   CRONOGRAMA    ########################################
elif selected == "Cronograma":
    st.markdown("<h1 style='text-align: center; color: #008080;'>CRONOGRAMA</h1>", unsafe_allow_html=True)
    
    # Você pode usar a mesma função de bloco se o layout for parecido
    # ou criar uma específica para o cronograma
    def bloco_cronograma(titulo_bloco, texto_descricao, texto_botao, url_botao):
        st.markdown(f"""
            <div style="background-color:#1e1e1e; padding:20px; margin-bottom:10px; border-radius:10px; border-left: 5px solid teal;">
                <h4 style="color:white;">{titulo_bloco}</h4>
                <p style="color:gray;">{texto_descricao}</p>
                <div style="margin-top: 15px; margin-bottom: 5px;"> <a href="{url_botao}" target="_blank" class="my-button" style="text-decoration: none; display: inline-block;">
                        {texto_botao}
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    link_cronograma = "https://docs.google.com/spreadsheets/d/1Fb5_otX8z50tuy9RbcGGC89BLKfErs_SCnML-JGeyQU/edit?usp=sharing"

    bloco_cronograma(
        titulo_bloco="Cronograma Detalhado",
        texto_descricao="Acesse a planilha detalhada com todas as fases, tarefas e prazos do projeto BioMove.",
        texto_botao="ABRIR CRONOGRAMA",
        url_botao=link_cronograma
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
            color: #888888;
            text-align: center;
            padding: 10px;
            font-size: 15px;
            border-top: 1px solid #262730;
        }
    </style>
    <div class="footer">
        UTFPR - Universidade Tecnológica Federal do Paraná - Engenharia Eletrônica - 2025
    </div>
""", unsafe_allow_html=True)
