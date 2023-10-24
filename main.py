import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_type = os.getenv("API_TYPE")
openai.api_base = os.getenv("API_BASE")
openai.api_version = os.getenv("API_VERSION")
openai.api_key = os.getenv("API_KEY")


# Prompt You are 
prompt = [
    """
    You are an Amazon logistics officer. Your job is to keep track of the different products that you are shipping. 
    You will need to run a supervised machine learning model on your products to add them to a database. However, 
    first you will need to label your images. The user says the type of object is a {type}. Output a Python String with 
    the type of object. Do not include any extra words in your answer. If the user's input is not reasonable, write False. 
    """,
    """
    You are an Amazon logistics officer. Your job is to keep track of the different products that you are shipping. 
    You will need to run a supervised machine learning model on your products to add them to a database. However, 
    first you will need to label your images. The user says the type of the object is {type} and the color of the object is {color}. 
    Output a Python tuple of ints with the color of the object in BGR format. Do not include any extra words in your answer. 
    If the user's input is not reasonable, write False.
    """,
    """
    You are an Amazon logistics officer. Your job is to keep track of the different products that you are shipping. 
    You will need to run a supervised machine learning model on your products to add them to a database. However, 
    first you will need to label your images. The user says the type of the object is {type}, the color of the object is {color}, 
    and the material of the object is {material}. Output a Python String with the material of the object in BGR format. 
    Do not include any extra words in your answer. If the user's input is not reasonable, write False.
    """,
    """
    You are an Amazon logistics officer. Your job is to keep track of the different products that you are shipping. 
    You will need to run a supervised machine learning model on your products to add them to a database. However, 
    first you will need to label your images. The user says the type of the object is {type}, the color of the object is {color}, 
    the material of the object is {material}, and the size of the object is {size}. Output an int with the size of the object in meters. 
    Do not include any extra words in your answer. If the user's input is not reasonable, write False.
    """
]




class LLM:
    
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def combine_text(self):
        return "System: "+ self.question + '\n' + 'User:' + self.answer + '\n' + ""

    def get_Information_LLM(text):
        response = openai.ChatCompletion.create(
        engine="api3_1",
        messages=[{"role": "system", "content": text}],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    def getanswer(self):
        return self.get_Information_LLM(self.combine_text) # false, or information

