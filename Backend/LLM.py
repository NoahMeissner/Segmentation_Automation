import os
import openai
from dotenv import load_dotenv

class LLM:

    def __init__(self, tuple):
        import openai
        load_dotenv()
        openai.api_type = os.getenv("API_TYPE")
        openai.api_base = os.getenv("API_BASE")
        openai.api_version = os.getenv("API_VERSION")
        openai.api_key = os.getenv("API_KEY")

        self.tuple = tuple
        self.prompt = """
        I want you to act as a Python interpreter. I will type commands and you will reply with what the
        python output should show. I want you to only reply with the terminal output inside one unique
        code block, and nothing else. Do no write explanations, output only what python outputs. Do not type commands unless I
        instruct you to do so. When I need to tell you something in English I will do so by putting
        text inside curly brackets like this: {example text}. My first command is a=1.
        the object is  a {type}, the color of the object is {color}, 
        the material of the object is {material}, and the size of the object is {size}. Output a Python tuple with the object as a String,
        the color as a BGR tuple, the material as a String, and the size of the object in meters as an int in that order. If the user's input
        for any of these parameters is unreasonable, label that slot with the bool False. Do not include any extra words in your answer. 
        If the user's input is not reasonable, write False.
        """

    def make_prompt(self):
        p = self.prompt.replace('{type}',self.tuple[0]) \
                        .replace('{material}', self.tuple[2]) \
                        .replace('{color}', self.tuple[1]) \
                        .replace('{size}',self.tuple[3])
        return p
    
    def get_Information_LLM(self, text):
        response = openai.Completion.create(
        engine="api3_1",
        messages=[{"role": "system", "content": text}],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
        return response

    def getanswer(self):
        return self.get_Information_LLM(self.make_prompt()) # false, or information

