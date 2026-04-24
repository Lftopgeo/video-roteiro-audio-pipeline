import openai
import os
from config import OPENAI_API_KEY, WHISPER_MODEL

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def extrair_audio_do_video(caminho_video: str) -> str:
    """Extrai o audio de um arquivo de video e salva como MP3."""
    try:
        from moviepy.editor import VideoFileClip
        caminho_audio = caminho_video.rsplit(".", 1)[0] + "_audio.mp3"
        print(f"[Transcriber] Extraindo audio de: {caminho_video}")
        with VideoFileClip(caminho_video) as video:
            video.audio.write_audiofile(caminho_audio, logger=None)
        print(f"[Transcriber] Audio extraido: {caminho_audio}")
        return caminho_audio
    except Exception as e:
        raise RuntimeError(f"Erro ao extrair audio do video: {e}")

def transcrever(caminho_arquivo: str) -> str:
    """
    Transcreve um arquivo de video ou audio usando OpenAI Whisper.
    Aceita: .mp4, .mp3, .wav, .m4a, .mov, etc.
    """
    extensoes_video = [".mp4", ".mov", ".avi", ".mkv", ".webm"]
    ext = os.path.splitext(caminho_arquivo)[1].lower()

    if ext in extensoes_video:
        caminho_arquivo = extrair_audio_do_video(caminho_arquivo)

    print(f"[Transcriber] Transcrevendo: {caminho_arquivo}")

    with open(caminho_arquivo, "rb") as arquivo:
        resposta = client.audio.transcriptions.create(
            model=WHISPER_MODEL,
            file=arquivo,
            response_format="text",
            language="pt"
        )

    transcricao = resposta.strip()
    print(f"[Transcriber] Transcricao concluida ({len(transcricao)} caracteres)")
    return transcricao
