import random


def jugar():
    usuario = input("Escoge una opción: 'Pi' para Piedra, 'Pa' para Papel y 'Ti' para Tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
    
    if usuario == computadora:
        print(f"Porque la computadora eligió: {computadora}, entonces es un:")
        return 'Empate'

    if gana_jugador(usuario, computadora):
        print(f"Porque la computadora eligió: {computadora}, entonces:")
        return 'Ganas'

    print(f"Porque la computadora eligió: {computadora}, entonces:")
    return 'Pierdes'

def gana_jugador(jugador, oponente):
    #regresar True si gana el jugador
    #Reglas:
    # Piedra gana a tijera (pi > ti)
    # tijera gana a papel (ti > pa)
    # papel gan a piedra (pa > pi)
    if (
        (jugador == 'pi' and oponente == 'ti') or (jugador == 'ti' and oponente == 'pa') or (jugador == 'pa' and oponente == 'pi') ):
        return True
    else:
        return False


print(jugar())
