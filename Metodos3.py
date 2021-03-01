# Punto 3

def check_char(caracter):  # función con un único parámetro de entrada
    if type(caracter) is str:  # Verifica si es un string
        if caracter.isalpha() is True:  # Verifica si es una letra de la A-Z
            if len(caracter) == 1:  # Verifica si es solo una letra
                return 0  # Imprime un 0 debido a que es un caracter de la A-Z
            else:  # Identifica el caso cuando es más de una letra
                return "ERROR #3: Mas de un caracter en el rango A-Z"
        else:  # Caracteres que no sean parte del rango A-Z
            return "ERROR #2: Uno o más caracteres fuera del rango A-Z"
    else:  # Identifica que el parámetro no es un carácter o string
        return "ERROR #1: no es un carácter o string"


# Punto 3.2 caps_switch
def caps_switch(caracter):  # función con un único parámetro de entrada
    codigo = check_char(caracter)  # llama a la función check_char
    if codigo == 0:  # Identifica si se ingresó un único carácter entre A-Z
        if caracter.islower() is True:  # Si el caracter está en minúscula
            return caracter.upper()  # Caracter de minúscula a mayúscula
        else:  # Verifica si el caracter está en mayúscula
            return caracter.lower()  # Caracter de mayúscula a minúscula
    else:  # Identifica si se obtuvo un codigo de error
        return codigo  # Imprime el cógido de error igual a check_char
