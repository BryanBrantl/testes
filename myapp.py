import streamlit as st
import serial
import time
import os

# --- Interface Streamlit ---
st.title("🧠 Controle de Carrinho com ChatGPT")
st.write("Digite comandos em linguagem natural e o carrinho irá executá-los!")

# --- Modo de operação ---
modo_simulado = st.sidebar.radio("Modo de operação:", ["Simulado", "Real (ChatGPT)"])

# --- Conectar ao Arduino ---
try:
    arduino = serial.Serial('COM3', 9600)  # Altere conforme sua porta
    time.sleep(2)
    st.sidebar.success("🔌 Arduino conectado com sucesso.")
    conectado = True
except:
    st.sidebar.error("❌ Arduino não encontrado.")
    conectado = False

# --- Função para interpretar comandos ---
def interpretar_comando(msg):
    if modo_simulado == "Simulado":
        comandos_exemplo = {
            "vá até o objeto": "FIND_OBJECT",
            "pare": "STOP",
            "vá para frente": "GO",
            "volte": "BACK",
            "vire à esquerda": "TURN_LEFT",
            "vire à direita": "TURN_RIGHT"
        }
        for chave, valor in comandos_exemplo.items():
            if chave in msg.lower():
                return valor
        return "STOP"
    else:
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY", "sua_chave_aqui")
        prompt = f"""
        Você é um assistente que traduz comandos de linguagem natural para comandos simples de um carrinho robô.
        Comandos válidos: GO, STOP, TURN_LEFT, TURN_RIGHT, FIND_OBJECT, BACK.

        Comando do usuário: \"{msg}\"
        Traduza para um desses comandos:
        """
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return resposta.choices[0].message.content.strip().upper()

# --- Enviar comando para o Arduino ---
def enviar_comando(comando):
    if conectado:
        arduino.write((comando + "\n").encode())
        return f"✅ Comando enviado: `{comando}`"
    else:
        return "❌ Erro: Arduino não conectado."

# --- Entrada de texto ---
texto = st.text_input("Comando para o carrinho", placeholder="Ex: 'Vá até o objeto e pare'", key="input")

if st.button("Enviar comando"):
    if texto:
        comando = interpretar_comando(texto)
        st.write(f"🧠 Comando interpretado: `{comando}`")
        resultado = enviar_comando(comando)
        st.success(resultado)
    else:
        st.warning("Digite um comando primeiro.")
