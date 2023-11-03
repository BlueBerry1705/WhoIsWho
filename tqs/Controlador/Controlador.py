from Model.Model import *
from Vista.Vista import *
import copy

def main():
    personatges = NumeroPersonatges()

    df = escollirPersonatge(generaPersonatges(extractNombres(personatges)))
    df_bot = copy.deepcopy(df)
    print(df)
    
    usuario = False
    ordenador = False

    while True:
        if pregunta_usuari(df) == "Has endevinat el personatge!":
            usuario = True
            break
        
        if pregunta_ordinador(df) == "Has endevinat el personatge!":
            ordenador = True
            break
    
    if usuario:
        printer("L'usuari ha guanyat la partida!")
    
    if ordenador:
        printer("L'ordinador ha guanyat la partida!")




