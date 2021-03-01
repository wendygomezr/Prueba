#Código con al menos 3 errores detectables

import string
import matplotlib.pyplot as plt

Alfabeto=list(string.ascii_letters)  # Crea un lista de letras

def ImprimirLetras():

    VariableLocalNoUsada = 0#El proposito de este comentario es ilustrar que la herramienta Flake8 no permite hacer comentarios que excedan un límite predfinido de caracteres.
    return Alfabeto

    
