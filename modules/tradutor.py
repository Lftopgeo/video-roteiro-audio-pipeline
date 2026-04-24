import openai
from config import OPENAI_API_KEY, OPENAI_MODEL, IDIOMAS
client = openai.OpenAI(api_key=OPENAI_API_KEY)
def traduzir_roteiro(roteiro, codigo):
      nome = IDIOMAS.get(codigo, codigo)
      r = client.chat.completions.create(model=OPENAI_MODEL,messages=[{"role":"system","content":f"Traduza para {nome} de forma natural e conversacional."},{"role":"user","content":roteiro}],temperature=0.5,max_tokens=2000)
      return r.choices[0].message.content.strip()
  def traduzir_para_todos_idiomas(roteiro):
        t = {"pt": roteiro}
        for c, n in IDIOMAS.items():
                  try: t[c] = traduzir_roteiro(roteiro, c)
except Exception as e: print(f"Erro {n}: {e}"); t[c] = None
    return t
