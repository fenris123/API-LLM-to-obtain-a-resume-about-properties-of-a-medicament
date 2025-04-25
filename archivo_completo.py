# -*- coding: utf-8 -*-

"""
Created on Wed Mar 12 12:21:08 2025

@author: fenris123
"""



import json
import requests
import re
import pyttsx3
from gpt4all import GPT4All
import sys





#  Paso 1:hacer la peticion a la API con informacion sobre un medicamento.
medicamento = input ("introduzca el nombre del medicamento: ")

respuesta_datos = requests.get(f"https://cima.aemps.es/cima/rest/medicamentos?nombre={medicamento}")


datos = json.loads(respuesta_datos.text)



# Verificar si hay resultados
if not datos.get("resultados"):  # También sirve si resultados no está presente
    print(f"No se han encontrado datos para el medicamento '{medicamento}'.")
    print("Por favor, compruebe que el nombre está correctamente escrito.")
    sys.exit()  # Finaliza el programa





# PASO 2: Obtener el resumen de los datos hecho por GPT4all


model = GPT4All("mistral-7b-openorca.Q4_0.gguf")  # primer uso lo descarga
with model.chat_session() as session:
    response = session.generate(f"""Estos son los datos del medicamento:
                                    {datos}
                                                                                                           
                                    Haz un pequeño resumen de los datos del medicamento obtenido, indicando la via de administracion, la forma farmaceutica,
                                    la via de administracion, y cualquier otro detalle que creas relevante. Cuando veas "mg en el texto, significa miligramos, ponlo con texto completo"
                                    """)
print(response)






# PASO 3 Leer el contenido del archivo de texto


def limpiar_texto_para_tts(texto):
    # Convierte solo las palabras completamente en mayúsculas a Capitalized
    return re.sub(r'\b[A-Z]{2,}\b', lambda m: m.group().capitalize(), texto)

# Limpiar el texto antes de leer
texto_limpio = limpiar_texto_para_tts(response)

# Inicializar motor TTS local
engine = pyttsx3.init()
engine.setProperty('rate', 140)     # Velocidad
engine.setProperty('volume', 1.0)   # Volumen

# Reproducir el texto
print(texto_limpio)
engine.say(texto_limpio)
engine.runAndWait()