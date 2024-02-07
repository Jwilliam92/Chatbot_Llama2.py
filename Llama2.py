# 1. Instalar Replicate and Spyder
# pip install replicate
# pip install spyder

# 2. Definir token de API Replicate

import os
os.environ['REPLICATE_API_TOKEN'] = 'r8_FRW14AR69kzo3zmaeHEoUhj4c7OKayG3h5puK'
# Busque seu Token: https://replicate.com/meta/llama-2-13b-chat?input=python

# 3. Rodar Modelo Llama 2 

import replicate

import replicate

# Prompts
pre_prompt = "Você é um assistente útil. Você não responde como 'Usuário' nem finge ser 'Usuário'. Você só responde uma vez como 'Assistente'."
prompt_input = "Você consegue falar português?"


# Generate LLM response
output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                        input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                        "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})  # Model parameters

# 4. Exibindo a resposta gerada pelo LLM
output

full_response = ""

for item in output:
  full_response += item

print(full_response)