from flask import Flask,render_template, request, Response
import openai
from dotenv import load_dotenv
import os
from time import sleep
from groq import Groq
from helpers import *
from selecionar_persona import *
from selecionar_documento import *

load_dotenv()

cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))
# cliente = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo ="meta-llama/llama-4-scout-17b-16e-instruct"
# modelo = "gpt-4o"
print(cliente)

app = Flask(__name__)
app.secret_key = 'alura'

def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0
    personalidade = personas[selecionar_persona(prompt)]
    contexto = selecionar_contexto(prompt)
    documento_selecionado = selecionar_documento(contexto)
    while True:
        try:
            prompt_do_sistema = f"""
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            Você deve gerar respostas utilizando o contexto abaixo.
            Você deve adotar a persona abaixo.
            
            # Contexto
            {documento_selecionado}
            # Personalidade
            {personalidade}
            """
            response = cliente.chat.completions.create(
                messages=[
                        {
                                "role": "system",
                                "content": prompt_do_sistema
                        },
                        {
                                "role": "user",
                                "content": prompt
                        }
                ],
            model=modelo,
            temperature=1,
            max_completion_tokens=200,
            top_p=1,
            )
            return response
        except Exception as erro:
                repeticao += 1
                if repeticao >= maximo_tentativas:
                        return "Erro no GPT: %s" % erro
                print('Erro de comunicação com OpenAI:', erro)
                sleep(1)
            


@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    texto_resposta = resposta.choices[0].message.content
    return texto_resposta

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
