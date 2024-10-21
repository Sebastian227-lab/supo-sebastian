from masa import *
from temperatura import *
from tiempo import *

def convertir():
    categoria = input("Selecciona la categoría (temperatura, masa, tiempo): ")
    valor = float(input("Ingresa el valor a convertir: "))
    
    if categoria == "temperatura":
        unidad_origen = input("Ingresa la unidad de origen (C, F, K): ")
        unidad_destino = input("Ingresa la unidad de destino (C, F, K): ")
        # Lógica de conversión...
    elif categoria == "masa":
        unidad_origen = input("Ingresa la unidad de origen (kg, lb, oz): ")
        unidad_destino = input("Ingresa la unidad de destino (kg, lb, oz): ")
        # Lógica de conversión...
    elif categoria == "tiempo":
        unidad_origen = input("Ingresa la unidad de origen (s, min, h): ")
        unidad_destino = input("Ingresa la unidad de destino (s, min, h): ")
        # Lógica de conversión...

# Llama a la función
convertir()
