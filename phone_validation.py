# Carga de librerias
import re

# Funcion para comprobar patrones
def comprobar_telefono(telefono):
    # Diccionario con los diferentes patrones
    patterns = {'pat1':'[0-9]{3}-([0-9]{2}-){2}[0-9]{2}',
               'pat2':'\([0-9]{3}\)[0-9]{3}-[0-9]{3}',
               'pat3':'([0-9]{3}-){2}[0-9]{3}',
               'pat4':'([0-9]{3}\s){2}[0-9]{3}',
               'pat5':'[0-9]{9}',
               'pat6':'34\s([0-9]{3}\s){2}[0-9]{3}',
               'pat7': '\([0-9]{3}\)\s([0-9]{2}\s){2}[0-9]{2}',
               'pat8': '[0-9]{3}\s([0-9]{2}\s){2}[0-9]{2}',
               'pat9': '34\s[0-9]{3}\s([0-9]{2}\s){2}[0-9]{2}'}
    # Bucle que recorre el diccionario comprueba cada patron con el telefono
    for pat in patterns.values():
        correcto = re.match(pat, str(telefono))
        if correcto:
            return True
    return False

# Introducir telefono
telefono = input('Introduce tu número de teléfono:')
print(comprobar_telefono(telefono))
