import random


def adivinador_pc (x):

    print("Bienvenido al juego")
    print(f"Selecciona un número entre 1 y {x} para que la máquina lo adivine.")
    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        # Se genera una predicción
        if limite_inferior != limite_superior:
           prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        #obtener respuesta del usuario
        respuesta = input(f"La predicción es {prediccion}. Si es muy alta ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C).").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    
    print(f"Adiviné tu número correctamente: {prediccion}")


adivinador_pc(100)