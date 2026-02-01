import streamlit as st
from openai import OpenAI
from gtts import gTTS
import os

# --- Configurações Iniciais da Página ---
st.set_page_config(
    page_title="Assistente de Voz IA",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Assistente de Voz Online")
st.markdown("Fale algo e o ChatGPT responderá em áudio.")

# --- Gerenciamento da API Key ---
# Tenta buscar dos Secrets (Nuvem) ou pede entrada manual (Local)
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
else:
    api_key = st.sidebar.text_input("Insira sua OpenAI API Key:", type="password")

if not api_key:
    st.info("Aguardando configuração da API Key para iniciar...")
    st.stop()

client = OpenAI(api_key=api_key)

# --- Interface de Gravação ---
audio_input = st.audio_input("Clique para gravar sua voz:")

if audio_input:
    try:
        with st.spinner("1. Transcrevendo áudio..."):
            # Salva o áudio temporariamente para enviar à API
            with open("temp_input.wav", "wb") as f:
                f.write(audio_input.read())

            # 2. SPEECH-TO-TEXT (OpenAI Whisper API)
            with open("temp_input.wav", "rb") as f:
                transcricao = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=f
                )
            
            texto_usuario = transcricao.text
            st.chat_message("user").write(texto_usuario)

        with st.spinner("2. Pensando na resposta..."):
            # 3. INTELIGÊNCIA (ChatGPT)
            resposta_ia = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente prestativo e conciso."},
                    {"role": "user", "content": texto_usuario}
                ]
            )
            texto_resposta = resposta_ia.choices[0].message.content
            st.chat_message("assistant").write(texto_resposta)

        with st.spinner("3. Gerando áudio de resposta..."):
            # 4. TEXT-TO-SPEECH (gTTS)
            tts = gTTS(text=texto_resposta, lang='pt')
            tts.save("resposta.mp3")

            # 5. EXIBIÇÃO DO ÁUDIO
            st.audio("resposta.mp3", format="audio/mp3", autoplay=True)
            
        # Limpeza de arquivos temporários
        if os.path.exists("temp_input.wav"):
            os.remove("temp_input.wav")

    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

else:
    st.write("Dica: Clique no microfone acima e faça uma pergunta.")

---
st.caption("Desenvolvido com Streamlit + OpenAI API")
