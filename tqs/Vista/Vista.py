import subprocess

def clear_screen():
    subprocess.run('cls', shell=True)

def MenuPrincipal():
    clear_screen()
    print('\033[1m\033[4m QUI ES QUI \033[0m')
    print('1 - Jugar\n2 - Ranking\n3 - Exit')

    numero = int(input('Introdueix el número: '))

    while numero > 3 or numero <= 0:
        numero = int(input('Introdueix el número: '))
    
    return numero


def mostraLeaderboard(leaderboard):
        clear_screen()
        # Ordena la llista d'acuerdo al temps
        leaderboard.sort(key=lambda x: x[1])

        # Mosta el leaderboard.
        print("Leaderboard:")
        for i, (nombre, tiempo) in enumerate(leaderboard, start=1):
            print(f"{i}. {nombre}: {tiempo} segundos")

        numero = 1

        while numero != 0:
            numero = int(input('Per tornar al Menú Principal, pren 0: '))

def escollirDificultat():
    clear_screen()
    print("Escull dificultat introduint el numero 1: facil, 2: mitja, 3: dificil")
    dificultad = int(input("Introduce el número de la dificultad: "))

    while dificultad > 3 or dificultad <= 0:
        dificultad = int(input("Introduce el número de la dificultad: "))

    if dificultad == 1:
        print("Has seleccionado la dificultad fácil.")
    elif dificultad == 2:
        print("Has seleccionado la dificultad media.")
    elif dificultad == 3:
        print("Has seleccionado la dificultad difícil.")
    
    return dificultad

def nombre():
    clear_screen()
    nombre = input("Introdueix el teu nom: ")

    return nombre


def mostrar_dataframe_sin_columnas(df):
    print('\033[1m\033[4m Llistat de personatges: \033[0m')
    print(df)

def escollir(df):
    clear_screen()
    mostrar_dataframe_sin_columnas(df)
    personatge = int(input("Fica numero de Personatge que vols escollir: "))

    while personatge > len(df):
        personatge = int(input("Fica numero de Personatge que vols escollir: "))
    
    clear_screen()
    return personatge

def vista_preguntes(df):
    mostrar_dataframe_sin_columnas(df)
    print('''1 El teu personatge es...?
2 El teu personatge es home o dona?
3 El teu personatge té la pell blanca o morena?
4 El teu personatge té barba? (Sí/No)
5 El teu personatge es gros o prim?
6 El teu personatge té un gorro? (Sí/No)
7 El teu personatge té gafas? (Sí/No)
8 El teu personatge té els ulls de color blau, marro o verd?
9 El teu personatge es alt, mitja o petit?
10 El teu personatge es un adult, un nen o un avi?
11 El teu personatge té el cabell ros, moreno, fosc o roig?

0 - Sortir de la partida
''')
    
    num_pregunta=int(input("Introdueix num de la pregunta: "))

    while num_pregunta < 0 or num_pregunta > 11:
        num_pregunta=int(input("Introdueix num de la pregunta: "))
    
    def case_1(df):
        print("Es el personatge número...?")
        num_personatge = int(input("Introdueix el índex del personatge: "))

        while num_personatge not in df.index:
            num_personatge = int(input("Introdueix el índex del personatge: "))

        return num_pregunta, num_personatge

    def case_2():
        print("Es...\n0 - home\n1 - dona? ")
        genero = int(input("Introdueix número: "))

        while genero < 0 or genero > 1:
            genero = int(input("Introdueix número: "))

        return num_pregunta, genero

    def case_9():
        print("Es...\n0 - Alt\n1 - Baix\n2 - Mitja")
        altura = int(input("Introdueix número: "))

        while altura < 0 or altura > 2:
            altura = int(input("Introdueix número: "))

        return num_pregunta, altura

    def case_11():
        print("Té el cabell...\n0 - Ros\n1 - Moreno\n2 - Fosc")
        color_cabell = int(input("Introdueix número: "))

        while color_cabell < 0 or color_cabell > 2:
            color_cabell = int(input("Introdueix número: "))
            
        return num_pregunta, color_cabell
        
    def case_3():
        print("Té la pell...\n0 - Blanca\n1 - Morena")
        pell = int(input("Introdueix número: "))

        while pell < 0 or pell > 1:
            pell = int(input("Introdueix número: "))

        return num_pregunta, pell
            
    def case_4():
        print("Té...\n0 - Barba\n1 - No barba")
        barba = int(input("Introdueix número: "))

        while barba < 0 or barba > 1:
            barba = int(input("Introdueix número: "))

        return num_pregunta, barba
            
    def case_5():
        print("Té el cos...\n0 - Gros\n1 - Prim")
        tipus_cos = int(input("Introdueix número: "))

        while tipus_cos < 0 or tipus_cos > 1:
            tipus_cos = int(input("Introdueix número: "))

        return num_pregunta, tipus_cos
       
    def case_8():
        print("Té els ulls de color...\n0 - Blau\n1 - Marró\n2 - Verd")
        color_ulls = int(input("Introdueix número: "))

        while color_ulls < 0 or color_ulls > 2:
            color_ulls = int(input("Introdueix número: "))
        
        return num_pregunta, color_ulls
                
    def case_6():
        print("Té gorro...?\n0 - Sí\n1 - No")
        gorro = int(input("Introdueix número: "))

        while gorro < 0 or gorro > 1:
            gorro = int(input("Introdueix número: "))

        return num_pregunta, gorro
            
    def case_7():
        print("Té ulleres...?\n0 - Sí\n1 - No")
        ulleres = int(input("Introdueix número: "))

        while ulleres < 0 or ulleres > 1:
            ulleres = int(input("Introdueix número: "))

        return num_pregunta, ulleres

    def case_10():
        print("És un...?\n0 - Avi\n1 - Adult\n2 - Nen")
        edat = int(input("Introdueix número: "))

        while edat < 0 or edat > 2:
            edat = int(input("Introdueix número: "))

        return num_pregunta, edat
    
    def case_0():
        return num_pregunta, 0
    
    # Crear un diccionari que mapeja els números a las funcions de case
    switch = {
        0: case_0,
        1: case_1,
        2: case_2,
        3: case_3,
        4: case_4,
        5: case_5,
        6: case_6,
        7: case_7,
        8: case_8,
        9: case_9,
        10: case_10,
        11: case_11
    }

    accion = switch[num_pregunta]
    
    if num_pregunta == 1:
        num_pregunta, opcion = accion(df)
    else:
        num_pregunta, opcion = accion()

    return num_pregunta, opcion

def resultat_preguntes(pregU, pregO):
    print(f'\033[34mPregunta Usuari:\033[39m \033[33m{pregU}\033[39m')
    print(f'\033[34mPregunta Ordinador:\033[39m \033[33m{pregO}\033[39m')
    
def vuelta_menu():
    numero = 1

    while numero != 0:
        numero = int(input('Per tornar al Menú Principal, pren 0: '))

def final(respuesta):
    print(respuesta)