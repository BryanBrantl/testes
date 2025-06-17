import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from pathlib import Path

st.set_page_config(page_title="BIOMOVE", layout="wide")

cor_botao = "#008080"
st.markdown(f"""
<style>
a.stButton {{
    display: inline-block;
    padding: 0.4em 0.6em; /* Ajuste o padding para o tamanho desejado */
    background-color: {cor_botao};
    color: white !important; /* '!important' para garantir a sobreposição */
    border: none;
    border-radius: 4px;
    text-align: center;
    text-decoration: none; /* Remove o sublinhado do link */
    font-size: 14px;
}}
a.stButton:hover {{
    background-color: #006666; /* Cor mais escura ao passar o mouse */
    color: white !important;
    text-decoration: none;
}}
a.stButton:active {{
    background-color: #008080; /* Cor ao clicar */
    color: white !important;
    text-decoration: none;
}}
</style>
""", unsafe_allow_html=True)


########################################################### Título principal #############################################################
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
    img8 = Image.open("image/pcb1.png")
    img9 = Image.open("image/pcb2.jpg")	
    img10 = Image.open("image/pcb3.jpg")
    img11 = Image.open("image/sinal_emg1.png")
    img12 = Image.open("image/Diagrama_EMG.png")
    img13 = Image.open("image/Diagrama_Hardware_carrinho.png")
    img14 = Image.open("image/Esquematico_EMG.jpg")
    img15 = Image.open("image/ESQUEMATICO_Semana1.jpg")	
    img16 = Image.open("image/Protoboard.jpg")
    img17 = Image.open("image/Osciloscopio_Protoboard.jpg")	
    img18 = Image.open("image/Placa_Perfurada.jpg")	
except FileNotFoundError:
    st.error("Uma ou mais imagens não foram encontradas. Verifique os caminhos dos arquivos.")
    # Atribui None para evitar mais erros
    img1, img2, img3, img4, img5, img6, img7, img = (None,)*8

video1 = "https://www.youtube.com/watch?v=jdvn68mhcQE"
video2 = "https://youtube.com/shorts/xoU3nnxIE90"

proposta_url ="https://docs.google.com/document/d/1uJpoXcehrK1Lv2cPMxUtHkvSNNtmgnatSJdmxfzy8gc/edit?usp=sharing"
relatorio_final_url ="https://docs.google.com/document/d/1uJpoXcehrK1Lv2cPMxUtHkvSNNtmgnatSJdmxfzy8gc/edit?usp=sharing"
cronograma_url = "https://docs.google.com/spreadsheets/d/1Fb5_otX8z50tuy9RbcGGC89BLKfErs_SCnML-JGeyQU/edit?usp=sharing"
############################################ Conteúdo de acordo com o menu selecionado ############################################
################################################################################################   HOME    #################################
if selected == "Home" and all([img1, img2, img3, img4]):
    st.markdown("<h1 style='text-align: center; color: #008080 ;'>MEMBROS</h1>", unsafe_allow_html=True)
    st.write("") # Espaço

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(img1, width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'> Bryan Alexandre de Lima Brantl</span></strong><br><br>
                 RA: 2414139<br>
                 E-mail: brantl@alunos.utfpr.edu.br<br>
                 Contato: (41) 99278-3929
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.image(img2,width=500)
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
        st.image(img3, width=500)
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
        st.image(img4, width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>Luiz Prado</span></strong><br><br>
                RA: 2402629<br>
                E-mail: luizoliveira.2002@alunos.utfpr.edu.br<br>
                Contato: (41) 99815-6532
            </div>
            """, unsafe_allow_html=True)
######################################### ###################################################
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

	##########################################
	st.markdown(
	    """
	    <hr style="border: 2px solid #008080; border-radius: 2px;">
	    """,
	    unsafe_allow_html=True
	)
	st.markdown("<h1 style='text-align: center; color: #008080;'>ENTREGA E VALIDAÇÃO DO HARDWARE - 06/06</h1>", unsafe_allow_html=True)
	st.markdown(
	    """
	    <hr style="border: 2px solid #008080; border-radius: 2px;">
	    """,
	    unsafe_allow_html=True
	)
	##########################################
	A0_col1, A0_col2, A0_col3 = st.columns([1, 0.05, 3])
	with A0_col1:
		st.image(img11, caption="Trecho do vídeo - Circuito EMG", use_container_width=True)
		st.link_button("▶", video1, use_container_width=True)
	with A0_col3:
		st.markdown("""
		    <div style='text-align: justify;'>
		        <h3>Demonstração do Circuito EMG e Próximos Passos no Tratamento de Ruído:</h3>
		        <ul>
		            <li>A equipe realizou uma demonstração do funcionamento do circuito EMG.</li>
		            <li>O vídeo com essa demonstração foi postado no YouTube.</li>
		            <li>Conforme planejado nas semanas anteriores, a equipe decidiu tratar a interferência do ruído via software, através da implementação de um filtro digital, que será desenvolvido nas próximas semanas.</li>
		        </ul>
		    </div>
		""", unsafe_allow_html=True)
	#########	
	st.subheader("Produção da Nova Versão da Placa de Circuito Impresso (PCI)")
	A0_col3_2, A0_col4, A0_col5 = st.columns([1, 2, 1])
	with A0_col3_2:
		st.image(img9, caption="PCI Soldada com Componentes",use_container_width=True)
	with A0_col4:
	        st.markdown("""
	            <div style='text-align: justify;'>
	                Na tentativa de reduzir significativamente o ruído, confeccionamos uma <span style='color: #008080;'>segunda e nova versão da Placa de Circuito Impresso</span>. Esta versão apresenta um <span style='color: #008080;'>roteamento otimizado e diferente</span>, com a implementação de um <span style='color: #008080;'>plano terra</span>, visando aprimorar a performance e reduzir interferências.
	                <br><br>
	                As imagens ao lado ilustram este progresso: à esquerda, temos a PCI já soldada com seus componentes, pronta para uso; e à direita, a visualização do layout da PCB no KiCad, detalhando o novo roteamento.
	            </div>
	        """, unsafe_allow_html=True)
	with A0_col5:
		st.image(img10, caption="Layout da PCI no KiCad", width=400)
	###########	
	
	A0_col6_1, A0_col6_2 = st.columns(2)
	st.subheader("Descritivo de Hardware do Carrinho")
	with A0_col6_1:
		st.markdown("""
		    <div style='text-align: justify;'>
		        O sistema do carrinho é composto por um <span style='color: #008080;'>ESP-32</span>, responsável pelo controle, enviando sinais de comando para a <span style='color: #008080;'>ponte H L298N</span>, que atua como driver dos dois motores DC (esquerdo e direito). Ambos os módulos (ESP-32 e L298N) são alimentados por uma única fonte de alimentação, que fornece energia tanto para o funcionamento do sistema quanto para a tração dos motores.
		    </div>
		""", unsafe_allow_html=True)
	with A0_col6_2:
		st.image(img12, caption="Diagrama de Hardware EMG", use_container_width=True)

	st.subheader("Descritivo de Hardware do EMG")
	A0_col7_1, A0_col7_2 = st.columns(2)
	with A0_col7_1:
		st.image(img13, caption="Diagrama de Hardware do Carrinho", use_container_width=True)
	with A0_col7_2:
		st.markdown("""
		    <div style='text-align: justify;'>
		        O diagrama de blocos representa um sistema de aquisição de sinais EMG. O sinal é captado por eletrodos, amplificado na etapa de pré-amplificação, e então filtrado por um filtro passa-faixa de 20 a 500 Hz. Após o condicionamento final do sinal, ele é enviado ao microcontrolador ESP32 por uma porta ADC para processamento.
		    </div>
		""", unsafe_allow_html=True)

	st.subheader("Esquemático do Circuito EMG Apresentado")
	st.markdown("""
	    <div style='text-align: justify;'>
	        Esquemático apresentado no entregavel de hardware:
	    </div>
	""", unsafe_allow_html=True)
	st.image(img14, caption="Esquemático Eletrônico Detalhado", use_container_width=True)
	st.divider()
	

########################### atualizacao 4 ##########################################################3
	
	st.markdown("""
	    <h2 style='color: #008080; text-align: center;'> #4 - Atualização Semanal - 30/05/2025 </h2>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Desafios na Produção da Placa de Circuito Impresso (PCI):</h3>
	        <ul>
	            <li>Avançamos na produção da placa de circuito impresso (PCI) para o projeto, reproduzindo o modelo com o filtro notch para testes.</li>
	            <li>Enfrentamos contratempos significativos durante a montagem e teste da placa, identificando problemas no roteamento do circuito e na soldagem de componentes.</li>
	            <li>Esses erros comprometeram o funcionamento da PCI, impossibilitando a continuidade dos testes nesta fase.</li>
	            <li>Estamos trabalhando na correção do layout e no aprimoramento do processo de soldagem para evitar recorrências.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Desenvolvimento do Sistema de Controle do Carrinho:</h3>
	        <ul>
	            <li>Conforme informado na semana passada, a montagem do carrinho foi finalizada.</li>
	            <li>Nesta semana, a equipe desenvolveu o software que permite controlar o carrinho por meio de um joystick no celular, utilizando conexão via Bluetooth.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Demonstração do Controle do Carrinho:</h3>
	        <ul>
	            <li>Foi adicionado um vídeo no YouTube demonstrando o funcionamento básico do carrinho via controle Bluetooth.</li>
	            <li>Para visualizar, clique no botão abaixo.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	st.link_button("▶", video1, type="secondary")
	
	st.divider()
#####################################################################################################		
	#semana3
	st.markdown("""
	    <h2 style='color: #008080; text-align: center;'> #3 - Atualização Semanal - 23/05/2025 </h2>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Montagem do Carrinho e Otimização do Circuito EMG:</h3>
	        <ul>
	            <li>Finalizada a montagem do carrinho.</li>
	            <li>Adição de novos filtros no esquemático do EMG.</li>
	            <li>Montagem do circuito EMG em placa perfurada para melhorar os testes quando comparado a protoboard.</li>
	            <li>O filtro Notch não apresentou o resultado esperado, levantando a hipótese de utilizar filtros digitais para melhorar a performance.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Circuito EMG em Placa Perfurada:</h3>
	        <ul>
	            <li>Circuito montado em placa perfurada:</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	st.image(img18, caption="Circuito do sensor EMG montado em placa perfurada.")
#####################################################################################################
	#semana2
	st.markdown("""
	    <h2 style='color: #008080; text-align: center;'> #2 - Atualização Semanal - 16/05/2025 </h2>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Desenvolvimento e Validação do Circuito EMG:</h3>
	        <ul>
	            <li>Definida a utilização de um Kit chassi para a construção do carrinho.</li>
	            <li>Montagem do sensor EMG em protoboard baseado no esquemático da semana anterior.</li>
	            <li>Validamos o sinal no osciloscópio, detectando presença de ruído da rede.</li>
	            <li>Definida a necessidade de implementar mais filtros no circuito para reduzir o ruído.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	
	st.subheader("Detalhes do Circuito e Sinal:")
	A4_col1, A4_col2 = st.columns(2)
	with A4_col1:
		st.markdown("""
		    <div style='text-align: justify;'>
		        <ul>
		            <li>Circuito montado em protoboard:</li>
		        </ul>
		    </div>
		""", unsafe_allow_html=True)
		st.image(img16, caption="Circuito montado em protoboard")
	with A4_col2:
		st.markdown("""
		    <div style='text-align: justify;'>
		        <ul>
		            <li>Sinal no osciloscópio:</li>
		        </ul>
		    </div>
		""", unsafe_allow_html=True)
		st.image(img17, caption="Sinal do sensor EMG capturado no osciloscópio", width = 480)
	st.divider()
#####################################################################################################
	#semana1
	st.markdown("""
 		<h2 style='color: #008080; text-align: center;'> #1 - Atualização Semanal - 09/05/2025 </h2>
 	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
		 <h3>Progresso e Decisões Iniciais do Projeto:</h3>
		<ul>
			<li>Realizados testes nos principais componentes do carrinho (motor DC, ESP32 e ponte H), sem identificação de defeitos.</li>
			<li>Conduzido estudo sobre softwares de modelagem 3D. Optou-se pela utilização do Eagle para o desenvolvimento do carrinho e do sistema EMG.</li>
			<li>Modelo do site finalizado.</li>
			<li>Proposta e cronograma revisados e atualizados conforme a devolutiva, já disponíveis no site.</li>
		<ul>
	    </div>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Decisões sobre o projeto:</h3>
	        <ul>
	            <li>Definido que serão utilizadas baterias 18650 (4.2V) para alimentação dos sistemas.</li>
	        </ul>
	        <h3>Construção do esquemático EMG:</h3>
	    </div>
	""", unsafe_allow_html=True)
	st.image(img15)
	st.divider()
############################################################################################
###################################   RELATORIO    ########################################
elif selected == "Relatórios":
	def bloco_informacao(titulo_bloco, texto_descricao, texto_botao, url_botao):
	    st.markdown(f"""
	        <div style="background-color:#1e1e1e; padding:20px; margin-bottom:10px; border-radius:10px; border-left: 5px solid teal;">
	            <h4 style="color:white; margin-top:0;">{titulo_bloco}</h4>
	            <p style="color:gray; font-size:16px;">{texto_descricao}</p>
	            <div style="margin-top: 15px; text-align: center;"> 
	                <a href="{url_botao}" target="_blank" style="
	                    text-decoration: none; 
	                    display: inline-block; 
	                    padding: 10px 20px; 
	                    background-color: #008080; 
	                    color: white; 
	                    border-radius: 5px; 
	                    text-align: center; 
	                    cursor: pointer;
	                    font-weight: bold;
	                    transition: background-color 0.3s ease;
	                ">
	                    {texto_botao}
	                </a>
	            </div>
	        </div>
	    """, unsafe_allow_html=True)
	
	# Título principal da seção de RELATÓRIOS
	st.markdown("<h1 style='text-align: center; color: #008080;'>RELATÓRIOS</h1>", unsafe_allow_html=True)
	
	# Bloco para a Proposta do Projeto
	bloco_informacao(
	    titulo_bloco="Proposta do Projeto",
	    texto_descricao="Nesta seção, está disponibilizada a proposta de projeto do BioMove. O documento reúne informações detalhadas sobre o escopo do projeto, sendo esta proposta já aprovada.",
	    texto_botao="ACESSAR PROPOSTA",
	    url_botao=proposta_url
	)
	
	# Bloco para o Relatório Final do Projeto
	bloco_informacao(
	    titulo_bloco="Relatório Final do Projeto",
	    texto_descricao="O relatório final do projeto BioMove, contendo todos os resultados, análises e conclusões, também pode ser acessado através do botão abaixo:",
	    texto_botao="ACESSAR RELATÓRIO FINAL",
	    url_botao=relatorio_final_url
	)

############################################################################################
###################################   CRONOGRAMA    ########################################
elif selected == "Cronograma":
	def bloco_informacao(titulo_bloco, texto_descricao, texto_botao, url_botao):
	    st.markdown(f"""
	        <div style="background-color:#1e1e1e; padding:20px; margin-bottom:10px; border-radius:10px; border-left: 5px solid teal;">
	            <h4 style="color:white; margin-top:0;">{titulo_bloco}</h4>
	            <p style="color:gray; font-size:16px;">{texto_descricao}</p>
	            <div style="margin-top: 15px; text-align: center;"> 
	                <a href="{url_botao}" target="_blank" style="
	                    text-decoration: none; 
	                    display: inline-block; 
	                    padding: 10px 20px; 
	                    background-color: #008080; 
	                    color: white; 
	                    border-radius: 5px; 
	                    text-align: center; 
	                    cursor: pointer;
	                    font-weight: bold;
	                    transition: background-color 0.3s ease;
	                ">
	                    {texto_botao}
	                </a>
	            </div>
	        </div>
	    """, unsafe_allow_html=True)
     
	bloco_informacao(
	    titulo_bloco="Cronograma Detalhado",
	    texto_descricao="Acesse a planilha detalhada com todas as fases, tarefas e prazos do projeto BioMove.",
	    texto_botao="ABRIR CRONOGRAMA",
	    url_botao=cronograma_url
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
