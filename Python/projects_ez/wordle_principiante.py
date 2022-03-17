"""
_ _ _ _ _ _
_ _ _ _ _ _
_ _ _ _ _ _
_ _ _ _ _ _
_ _ _ _ _ _
_ _ _ _ _ _

palabra == intento - ganar
letra in palabra - ayuda
letra not in palabra - no existe
"""
colors = {
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'ENDC': '\033[0m', 
}
def color_letter(letter, color):
    return colors[color] + letter + colors ['ENDC']

#init game
from itertools import tee

from matplotlib.pyplot import text


print("Comenzar a jugar")

ganar =  False
palabra = 'trineo'

tablero = []
for i in range(6):
    tablero.append(['_' for l in range(6)])

contador = 0

while (not ganar) and (contador < len(palabra)):
    respuesta = input("")
    while len(respuesta) != len(palabra):
        print(f"La palabra debe tener {len(palabra)} de caracteres.")
        respuesta = input("")

    #para ganar
    if palabra == respuesta:
        tablero[contador] = [l for l in respuesta]
        ganar = True


    #letra en palabra
    else:
        test = []
        for j in range(len(respuesta)):
            if respuesta[j] == palabra[j]:
                test.append(color_letter(respuesta[j], 'green'))
            elif respuesta[j] in palabra:
                test.append(color_letter(respuesta[j], 'yellow'))
            else:
                test.append(color_letter(respuesta[j], 'red'))
        tablero[contador] = test
    #dibujo del tablero
    for i in range(6):
        print(" ".join(tablero[i]))
    
    contador =+ 1

if ganar:
    print("GANASTE")
else:
    print("PERDISTE")