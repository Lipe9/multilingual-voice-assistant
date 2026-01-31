import whisper
from openai import OpenAI
from gtts import gTTS
import os

# 1. Configurações Iniciais
# Certifique-se de definir sua chave de API da OpenAI nas variáveis de ambiente
client = OpenAI(api_key="SUA_CHAVE_AQUI")

def sistema_conversa_voz(arquivo_audio):
    print("--- Iniciando Processamento ---")
    
    # 2. SPEECH-TO-TEXT: Usando Whisper para transcrever
    print("Transcrevendo áudio com Whisper...")
    model_whisper = whisper.load_model("base") # Opções: tiny, base, small, medium, large
    resultado_transcricao = model_whisper.transcribe(arquivo_audio)
    texto_usuario = resultado_transcricao["text"]
    print(f"Usuário disse: {texto_usuario}")

    # 3. INTELIGÊNCIA: Enviando o texto para o ChatGPT
    print("Consultando o ChatGPT...")
    resposta_ia = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente prestativo e poliglota."},
            {"role": "user", "content": texto_usuario}
        ]
    )
    texto_resposta = resposta_ia.choices[0].message.content
    print(f"ChatGPT respondeu: {texto_resposta}")

    # 4. TEXT-TO-SPEECH: Sintetizando a resposta com gTTS
    print("Sintetizando voz de resposta...")
    audio_saida = gTTS(text=texto_resposta, lang='pt', slow=False)
    audio_saida.save("resposta.mp3")
    
    # 5. REPRODUÇÃO (Opcional - depende do sistema operacional)
    # os.system("start resposta.mp3") # Windows
    # os.system("afplay resposta.mp3") # macOS
    print("--- Processo Finalizado! Arquivo 'resposta.mp3' gerado. ---")

# Execução
# sistema_conversa_voz("pergunta_usuario.m4a")
