from groq import Groq
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *
import openai

load_dotenv()

cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))
# cliente = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo ="meta-llama/llama-4-scout-17b-16e-instruct"
# modelo = "gpt-4o"
contexto = carrega("dados/ecomart.txt")

assistente = cliente.chat.completions.create(
    messages=[
        {
            "role": "assistant",
            "content": f"""
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            Além disso, adote a persona abaixo para responder ao cliente.
            
            ## Contexto
            {contexto}
        
             ## Persona
        
            {personas["neutro"]}
            
            """
        }
    ],
    model = modelo,
)
