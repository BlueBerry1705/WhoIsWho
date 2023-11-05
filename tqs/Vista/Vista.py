

def MenuPrincipal():
    print('\033[1m\033[4m QUI ES QUI \033[0m')
    print('1 - Jugar\n 2 - Ranking\n 3 - Exit')

    numero = int(input('Introdueix el número: '))

    while numero > 3:
        numero = int(input('Introdueix el número: '))
    
    return numero


def mostraLeaderboard(leaderboard):
        # Ordena la lista de acuerdo al tiempo (ascendente).
        leaderboard.sort(key=lambda x: x[1])

        # Muestra el leaderboard.
        print("Leaderboard:")
        for i, (nombre, tiempo) in enumerate(leaderboard, start=1):
            print(f"{i}. {nombre}: {tiempo} segundos")

def escollirDificultat():
    print("Escull dificultat introduint el numero 1: facil, 2: mitja, 3: dificil")
    dificultad = int(input("Introduce el número de la dificultad: "))

    if dificultad == 1:
        print("Has seleccionado la dificultad fácil.")
    elif dificultad == 2:
        print("Has seleccionado la dificultad media.")
    elif dificultad == 3:
        print("Has seleccionado la dificultad difícil.")
    else:
        print("Dificultad no válida. Por favor, selecciona 1, 2 o 3 para la dificultad.")
    
    return dificultad


def mostrar_dataframe_sin_columnas(df):
    print('\033[1m\033[4m Llistat de personatges: \033[0m')
    print(df)

def escollir(df):
    personatge = int(input("Fica numero de Personatge que vols escollir: "))

    while personatge > len(df):
        personatge = int(input("Fica numero de Personatge que vols escollir: "))
    
    return personatge

def vista_preguntes():
    print('''1 ¿Cuál es el nombre de esta persona?
2 ¿Cuál es el género de esta persona? ¿Es hombre o mujer?
3 ¿Cuál es el tono de piel de esta persona? ¿Es blanco o moreno?
4 ¿Esta persona tiene barba? (Sí/No)
5 ¿Cómo es el tipo de cuerpo de esta persona? ¿Es gordo o delgado?
6 ¿Lleva esta persona un gorro? (Sí/No)
7 ¿Lleva esta persona gafas? (Sí/No)
8 ¿De qué color son los ojos de esta persona? ¿Son azules, marrones o verdes?
9 ¿Cuál es la altura de esta persona? ¿Es alto, de altura media o bajo?
10 ¿Cuál es la edad de esta persona? ¿Es un adulto, un niño o un anciano?
11 ¿De qué color es el cabello de esta persona? ¿Es rubio, moreno, oscuro o rojo?

0 - Sortir de la partida
''')
    
    num_pregunta=int(input("Fica num de la pregunta: "))

    while num_pregunta > 11:
        num_pregunta=int(input("Fica num de la pregunta: "))
    
    def case_1():
        num_personatge = int(input("Fica el índex del personatge: "))

        return num_personatge

    def case_2():
        genero = input("Es home o dona? ")

        return genero

    def case_9():
        altura = input("Es alt, baix o mitja d'altura? ")  

        return altura

    def case_11():
        ## 4 ¿De qué color es el cabello de esta persona? ¿Es rubio, moreno, oscuro o rojo?
        color_cabell = input("Es ros, moreno, fosc, roig? ")
            
        return color_cabell
        
    def case_3():
        ## 5 ¿Cuál es el tono de piel de esta persona? ¿Es blanco o moreno?
        pell = input("Es blanc o moreno? ")

        return pell
            
    def case_4():
        ## 6 ¿Esta persona tiene barba? (Sí/No)
        barba = input("Té barba o no? ")

        return barba
            
    def case_5():
        ## 7 ¿Cómo es el tipo de cuerpo de esta persona? ¿Es gordo o delgado?
        tipus_cos = input("Quin cos té? Es gros o prim? ")

        return tipus_cos
       
    def case_8():
        ## 8 ¿De qué color son los ojos de esta persona? ¿Son azules, marrones o verdes?
        color_ulls = input("Te els ulls de color blau, marro o verd? ")
        
        return color_ulls
                
    def case_6():
        ## 9 ¿Lleva esta persona un gorro? (Sí/No)
        gorro = input("Porta gorro la persona? ")

        return gorro
            
    def case_7():
        ulleres = input("Porta Ulleres si o no? ")

        return ulleres

    def case_10():
        edat = input("Es un avi, un adult o un nen? ")

        return edat

    # Crear un diccionario que mapea los números a las funciones de caso
    switch = {
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

    if num_pregunta in switch:
        accion = switch[num_pregunta]
        return accion
    else:
        print("Número no válido.")
    