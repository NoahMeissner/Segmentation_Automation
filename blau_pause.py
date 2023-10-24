import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_type = os.getenv("API_TYPE")
openai.api_base = os.getenv("API_BASE")
openai.api_version = os.getenv("API_VERSION")
openai.api_key = os.getenv("API_KEY")

print(openai.api_base)


response = openai.ChatCompletion.create(
    engine="api3_1",
    messages=[{"role": "system", "content": "Was ist 1+3"}],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

print(response)
