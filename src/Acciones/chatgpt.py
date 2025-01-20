
from Acciones.lectura_chat import *
from Acciones.textos import menu_insult
import time
import os

import openai 

import mcpi.minecraft as minecraft

openai.api_key = os.getenv("OPENAI_API_KEY")


mc = minecraft.Minecraft.create("localhost")

def ChatGPT():

    time.sleep(0.2)
    mc.postToChat("Escribe tu peticion a ChatGPT:")
    peticion = str(Lectura_chat())

    respuesta = preguntar_a_chatgpt(peticion)
    
    print("Respuesta de ChatGPT:", respuesta)
    mc.postToChat("ChatGPT: %s" %respuesta)

def preguntar_a_chatgpt(mensaje_usuario):
    try:
        # Llamada a la API de OpenAI
        respuesta = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Especificacion del modelo de ChatGPT
            messages=[
                {"role": "system", "content": "Eres un asistente en un servidor de Minecraft, Responde de manera corta concisa y en una linea. No uses tildes y ni la letra 'ñ'"},
                {"role": "user", "content": mensaje_usuario}
            ],
            max_tokens=50,  # Respuesta breve
            temperature=0.5  # Nivel de creatividad
        )
        return respuesta["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error al conectar con ChatGPT: {e}"
        
        #Si el error es el siguiente es que falta meterle pasta (el numero puede no salir):
        # 429 - You exceeded your current quota, please check your plan and billing details