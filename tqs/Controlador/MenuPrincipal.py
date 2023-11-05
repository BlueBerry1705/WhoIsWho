from Controlador.Juego import *

def main():
    from Vista.Vista import MenuPrincipal
    opcion = MenuPrincipal()
    
    if opcion == 1:
        iniciar_juego()
    elif opcion == 2:
        scoreboard()
    elif opcion == 3:
        return 0




