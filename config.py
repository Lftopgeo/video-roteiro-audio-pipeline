import os
from dotenv import load_dotenv

load_dotenv()

# === API KEYS ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# === MODELOS ===
OPENAI_MODEL = "gpt-4o"
WHISPER_MODEL = "whisper-1"

# === ELEVENLABS - Voice IDs por idioma ===
# Substitua pelos IDs reais das vozes na sua conta ElevenLabs
VOICE_IDS = {
      "pt": "pNInz6obpgDQGcFmaJgB",
      "en": "EXAVITQu4vr4xnSDxMaL",
      "es": "VR6AewLTigWG4xSOukaG",
      "fr": "ErXwobaYiN019PkySvjV",
      "de": "MF3mGyEYCl7XYWbV9V6O",
}

# === IDIOMAS PARA TRADUCAO ===
IDIOMAS = {
      "en": "English",
      "es": "Spanish",
      "fr": "French",
      "de": "German",
}

# === PROMPT BASE PARA ROTEIRO ===
PROMPT_ROTEIRO = """
Voce e um roteirista profissional de videos virais para YouTube e Instagram.

Com base na transcricao abaixo, crie um ROTEIRO otimizado seguindo EXATAMENTE esta estrutura:

1. GANCHO (0-5 segundos): Uma frase impactante para prender a atencao imediatamente.
2. PROBLEMA/CONTEXTO (5-30 segundos): Apresente o problema ou contexto de forma envolvente.
3. DESENVOLVIMENTO (30-90 segundos): Desenvolva o conteudo principal com clareza e ritmo.
4. CONCLUSAO/CTA (ultimos 10 segundos): Feche com uma chamada para acao poderosa.

Regras:
- Use linguagem natural e conversacional
- Escreva como se estivesse falando, nao como texto formal
- Mantenha o ritmo dinamico
- Use pontuacao para indicar pausas naturais
- NAO inclua descricoes de cena, apenas o texto falado

TRANSCRICAO:
{transcricao}

ROTEIRO FINAL:
"""
