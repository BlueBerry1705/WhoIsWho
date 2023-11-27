from Controlador.Juego import *
from Vista.Vista import *

def main():
    while True:
        from Vista.Vista import MenuPrincipal
        opcion = MenuPrincipal()
        
        if opcion == 1:
            archivos_en_csv = os.listdir('csv/')
            archivos_partida_usuari = [archivo for archivo in archivos_en_csv if archivo.startswith('partida_usuari')]
            
            dificultad = 0
            user = " "
            if archivos_partida_usuari == []:
                dificultad = escollirDificultat()
                user = nombre()
            
                df, df_bot = iniciar_juego(dificultad)

                personatge = escollir(df) 

                df, df_bot = seleccion(df, personatge)     
            else:
                nombre_archivo = archivos_partida_usuari[0]

                dificultad = int(nombre_archivo.split('_')[-1].split('.')[0])

                df = pd.read_csv(os.path.join('csv', nombre_archivo), index_col=0)
                df_bot = pd.read_csv('csv/partida_guardada_bot.csv')
            
            ordenador = False
            usuario = False
            tiempo_inicial = datetime.datetime.now()
            while True:
                pregunta, opcion = vista_preguntes(esconder(df))

                salida, pregU, pregO = bucle_principal(df, df_bot, pregunta, opcion, dificultad)

                if salida == 0:
                    break
                elif salida == 1:
                    usuario = True
                    break
                elif salida == 2:
                    ordenador = True
                    break
                
                resultat_preguntes(pregU, pregO)
            
            final(final_partida(archivos_partida_usuari, salida, usuario, ordenador, user, tiempo_inicial, dificultad))

            vuelta_menu()

        elif opcion == 2:
            mostraLeaderboard(scoreboard())
        elif opcion == 3:
            return 0




