import openai
from config import OPENAI_API_KEY, OPENAI_MODEL, PROMPT_ROTEIRO

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def gerar_roteiro(transcricao):
    prompt = PROMPT_ROTEIRO.format(transcricao=transcricao)
    r = client.chat.completions.create(model=OPENAI_MODEL, messages=[{"role":"system","content":"Roteirista profissional de videos virais."},{"role":"user","content":prompt}], temperature=0.7, max_tokens=2000)
    return r.choices[0].message.content.strip()
