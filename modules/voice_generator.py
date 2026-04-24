import os
  import requests
    from config import ELEVENLABS_API_KEY, VOICE_IDS
      BASE = 'https://api.elevenlabs.io/v1'
      def gerar_audio_elevenlabs(texto, idioma, nome_arquivo, output_dir='output'):
      vid = VOICE_IDS.get(idioma)
      if not vid: raise ValueError(f'Voice ID faltando: {idioma}')
        os.makedirs(output_dir, exist_ok=True)
        out = os.path.join(output_dir, f'{nome_arquivo}_{idioma}.mp3')
        h = {'xi-api-key': ELEVENLABS_API_KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'}
        p = {'text': texto, 'model_id': 'eleven_multilingual_v2', 'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0.5, 'use_speaker_boost': True}}
        r = requests.post(f'{BASE}/text-to-speech/{vid}', json=p, headers=h)
        if r.status_code != 200: raise RuntimeError(f'ElevenLabs {r.status_code}: {r.text}')
          open(out, 'wb').write(r.content)
          print(f'Audio: {out}')
              return out
          def gerar_audios_todos_idiomas(traducoes, nome_base, output_dir='output'):
          a = {}
          for i, t in traducoes.items():
                    if not t or i not in VOICE_IDS: continue
                      try: a[i] = gerar_audio_elevenlabs(t, i, nome_base, output_dir)
                      except Exception as e: print(f'Erro {i}: {e}')
                          return a
