from Model.Model import *
from Vista.Vista import *
import copy
import tkinter as tk
import datetime

def iniciar_juego():
    Npersonatges = escollirDificultat()
    while Npersonatges > 3:
        Npersonatges = escollirDificultat()

    personatges = generaPersonatges(extractNombres(Npersonatges))
    df = escollirPersonatge(personatges, escollir(personatges))
    df_bot = copy.deepcopy(df)
    print(df)
    
    usuario = False
    ordenador = False
    
    tiempo_inicial = datetime.datetime.now()
    while True:
        mostrar_dataframe_sin_columnas(amagarColumnas(df))

        vista_preguntes()
        pregU = pregunta_usuari(df)
        print(pregU)
        if pregU == "Has endevinat el personatge!":
            usuario = True
            break
        
        pregO = pregunta_ordinador(df_bot)
        print(pregO)
        if pregO == "Has endevinat el personatge!":
            ordenador = True
            break
    
    if usuario:
        tiempo_final = datetime.datetime.now()
        print("L'usuari ha guanyat la partida!")
    
    if ordenador:
        print("L'ordinador ha guanyat la partida!")
    
    if usuario == False and ordenador == False:
        df_bot.to_csv('../csv/partida_guardada_bot.csv')
        df.to_csv('../csv/partida_usuari.csv')

def scoreboard():
    sb = leerleaderboard()

    mostraLeaderboard(sb)

    