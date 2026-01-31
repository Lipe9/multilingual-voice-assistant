🤖 Voice-to-Voice AI Assistant (Whisper + GPT + gTTS)
Este projeto consiste em um assistente virtual capaz de ouvir, processar e responder comandos de voz em múltiplos idiomas. A solução integra três tecnologias pilares da Inteligência Artificial moderna para criar uma experiência de conversação fluida e natural.

🎯 Objetivo do Projeto
Desenvolver um pipeline completo de Conversação por Voz (Voice-to-Voice), demonstrando a integração de modelos de Reconhecimento de Fala (ASR), Processamento de Linguagem Natural (NLP) e Síntese de Voz (TTS).

🧩 Como funciona?
O sistema opera em um fluxo de quatro estágios principais:

Speech-to-Text (STT): O áudio do usuário é capturado e processado pelo OpenAI Whisper. Diferente de outros motores de busca, o Whisper é robusto contra ruídos e entende sotaques técnicos de forma excepcional.

Lógica e Inteligência (LLM): O texto transcrito é enviado para a API do ChatGPT (GPT-3.5/4). Aqui, a IA interpreta a intenção, busca a resposta ou realiza a tradução necessária.

Text-to-Speech (TTS): A resposta textual é convertida em áudio pelo Google Text-to-Speech (gTTS), gerando um arquivo de saída amigável.

Interface de Saída: O sistema reproduz o arquivo final, permitindo uma conversa sem necessidade de teclado.

🛠️ Tecnologias e Ferramentas
Linguagem: Python 3.10+

Transcrição: OpenAI Whisper (Local ou via API)

Cérebro: OpenAI Chat Completions API

Voz: gTTS (Google Text-to-Speech)

Gestão de Ambiente: Python-dotenv (para proteção de API Keys)

🚀 Destaques Técnicos
Suporte Multilingue: O sistema detecta automaticamente o idioma falado.

Segurança: Implementação de variáveis de ambiente para evitar vazamento de credenciais no GitHub.

Modularidade: Código organizado em funções para facilitar a troca de modelos (ex: trocar gTTS pelas vozes da ElevenLabs ou OpenAI Speech).
