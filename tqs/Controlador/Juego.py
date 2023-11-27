from Model.Model import *
import copy
import datetime
import subprocess
import os

def iniciar_juego(dificultad):
    Npersonatges = NumeroPersonatges(dificultad)
    df = generaPersonatges(extractNombres(Npersonatges))
    df_bot = copy.deepcopy(df)
    
    return df, df_bot

def seleccion(df, personatge):
    df = escollirPersonatge(df, personatge)
    df_bot = copy.deepcopy(df)

    return df, df_bot

def esconder(df):
    return amagarColumnas(df)

def bucle_principal(df, df_bot, preguntes, opcio, dificultad):
    subprocess.run('cls', shell=True)
    pregO = ' '
    pregU = ' '

    if preguntes == 0:
        df_bot.to_csv('csv/partida_guardada_bot.csv')
        df.to_csv(f'csv/partida_usuari_{dificultad}.csv')
        pregU = 'Partida guardada!'
        pregO = 'Partida guardada!'
        return 0, pregU, pregO
        

    pregU = pregunta_usuari(df, preguntes, opcio)
        
    if pregU == "Has endevinat el personatge!":
        return 1, pregU, pregO
        
    pregO = pregunta_ordinador(df_bot)
        
    if pregO == "Has endevinat el personatge!":
        return 2, pregU, pregO
    
    return 3, pregU, pregO

def final_partida(archivos_partida_usuari, preguntes, usuario, ordenador, user, tiempo_inicial, dificultad):
    if archivos_partida_usuari and preguntes != 0:
        nombre_archivo = archivos_partida_usuari[0]
        os.remove(os.path.join('csv', nombre_archivo))
        os.remove('csv/partida_guardada_bot.csv')

    if usuario:
        tiempo_final = datetime.datetime.now()

        diferencia = tiempo_final - tiempo_inicial

        diferencia = diferencia.total_seconds()

        agregar_leaderboard(user, diferencia, dificultad)

        return "L'usuari ha guanyat la partida!"
    elif ordenador:
        return "L'ordinador ha guanyat la partida!"

    return "Partida guardada con éxito!"

def scoreboard(dificultat):
    return leer_leaderboard(dificultat)

    

    