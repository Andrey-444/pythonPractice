# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DUADXgd22NcFoErlVpn9Ul3_js-LK-qM

Python
"""

personajes = ["una princesa", "un caballero", "un mago"]
lugares = ["en un castillo", "en el bosque", "en la casa britney spears"]
acciones = ["lucha contra", "habla con", "baila con", "huye de"]

import random

personaje = random.choice(personajes)
lugar = random.choice (lugares)
accion = random.choice (acciones)

historia = f"{personaje} {accion} goku {lugar}."

print (historia)

if personaje ==  "una princesa" : print("historia de princesas!")
else : print("es hora de aventura llama a tus amigos")

import random

for i in range(10):
  personaje = random.choice(personajes)
  lugar = random.choice (lugares)
  accion = random.choice (acciones)

  historia = f"{personaje} {accion} goku {lugar}."

  print(f"historia {i+1}: {historia}")

# @title Texto de título predeterminado
import random

def generar_historia():
  historias = []
  personaje = random.choice (personajes)
  lugar = random.choice (lugares)
  accion = random.choice (acciones)
  historia = f"{personaje} {accion} goku {lugar}."
  historias.append(historia)
  return historia

for i in range(10):
   historia = generar_historia()
   print(f"historia {i+1}: {historia}")

nuevo_personaje= input("ingresar un nuevo personaje:")
personajes.append(nuevo_personaje)

nuevo_lugar= input("ingresar un nuevo lugar")
lugares.append(nuevo_lugar)

nuevo_accion= input("ingresar una nueva accion")
acciones.append(nuevo_accion)