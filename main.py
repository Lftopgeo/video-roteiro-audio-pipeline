import os
import json
import argparse
from datetime import datetime

from modules.transcriber import transcrever
from modules.roteiro import gerar_roteiro
from modules.tradutor import traduzir_para_todos_idiomas
from modules.voice_generator import gerar_audios_todos_idiomas

def salvar_resultado(dados: dict, output_dir: str, nome_base: str):
    """Salva roteiro e traducoes em arquivos de texto."""
    os.makedirs(output_dir, exist_ok=True)

    caminho_json = os.path.join(output_dir, f"{nome_base}_resultado.json")
    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    for idioma, texto in dados.get("traducoes", {}).items():
        if texto:
            caminho_txt = os.path.join(output_dir, f"{nome_base}_roteiro_{idioma}.txt")
            with open(caminho_txt, "w", encoding="utf-8") as f:
                f.write(texto)

    print(f"\n[Main] Resultados salvos em: {output_dir}/")

def pipeline_completo(caminho_video: str, output_dir: str = "output"):
    """
    Pipeline completo:
    1. Transcricao do video
    2. Geracao do roteiro
    3. Traducao para multiplos idiomas
    4. Geracao de audio via ElevenLabs
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_base = f"video_{timestamp}"

    print("\n" + "="*60)
    print("PIPELINE DE GERACAO DE ROTEIRO E AUDIO")
    print("="*60)

    print("\nETAPA 1/4: Transcrevendo o video...")
    transcricao = transcrever(caminho_video)
    print(f"\n[Transcricao Preview]\n{transcricao[:300]}...\n")

    print("\nETAPA 2/4: Gerando roteiro...")
    roteiro = gerar_roteiro(transcricao)
    print(f"\n[Roteiro Preview]\n{roteiro[:400]}...\n")

    print("\nETAPA 3/4: Traduzindo para multiplos idiomas...")
    traducoes = traduzir_para_todos_idiomas(roteiro)
    print(f"[Tradutor] Idiomas gerados: {list(traducoes.keys())}\n")

    print("\nETAPA 4/4: Gerando audios via ElevenLabs...")
    audios = gerar_audios_todos_idiomas(traducoes, nome_base, output_dir)

    resultado = {
        "video_original": caminho_video,
        "timestamp": timestamp,
        "transcricao": transcricao,
        "roteiro_pt": roteiro,
        "traducoes": traducoes,
        "audios_gerados": audios
    }

    salvar_resultado(resultado, output_dir, nome_base)

    print("\n" + "="*60)
    print("PIPELINE CONCLUIDO COM SUCESSO!")
    print("="*60)
    print(f"\nArquivos gerados em: ./{output_dir}/")
    print(f"  - Roteiro PT:  {nome_base}_roteiro_pt.txt")
    for idioma in audios:
        print(f"  - Audio {idioma.upper()}:    {nome_base}_{idioma}.mp3")
    print(f"  - JSON completo: {nome_base}_resultado.json\n")

    return resultado

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pipeline: Video -> Roteiro -> Traducao -> Audio"
    )
    parser.add_argument(
        "video",
        help="Caminho para o arquivo de video ou audio (ex: meu_video.mp4)"
    )
    parser.add_argument(
        "--output",
        default="output",
        help="Diretorio de saida (padrao: output/)"
    )

    args = parser.parse_args()

    if not os.path.exists(args.video):
        print(f"Arquivo nao encontrado: {args.video}")
        exit(1)

    pipeline_completo(args.video, args.output)
