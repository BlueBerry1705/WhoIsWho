from Model.Model import *
from Vista.Vista import *
import copy
import datetime
import subprocess

def iniciar_juego():
    dificultad = escollirDificultat()
    user = nombre()

    Npersonatges = NumeroPersonatges(dificultad)

    personatges = generaPersonatges(extractNombres(Npersonatges))
    df = escollirPersonatge(personatges, escollir(personatges))
    df_bot = copy.deepcopy(df)
    
    usuario = False
    ordenador = False
    
    tiempo_inicial = datetime.datetime.now()
    while True:
        sin = amagarColumnas(df)

        preguntes, opcio = vista_preguntes(sin)
        subprocess.run('cls', shell=True)

        if preguntes == 0:
            df_bot.to_csv('../csv/partida_guardada_bot.csv')
            df.to_csv('../csv/partida_usuari.csv')
            break

        pregU = pregunta_usuari(df, preguntes, opcio)
        
        if pregU == "Has endevinat el personatge!":
            usuario = True
            break
        
        pregO = pregunta_ordinador(df_bot)
        
        if pregO == "Has endevinat el personatge!":
            ordenador = True
            break
        
        resultat_preguntes(pregU, pregO)

    if usuario:
        tiempo_final = datetime.datetime.now()
        print("L'usuari ha guanyat la partida!")
    
    if ordenador:
        print("L'ordinador ha guanyat la partida!")

def scoreboard():
    sb = leerleaderboard()

    mostraLeaderboard(sb)

    