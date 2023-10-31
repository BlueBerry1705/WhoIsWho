import pandas as pd
import random
import csv

# Genera una lista de nombres aleatorios

def NumeroPersonatges():
    usuario_input = int(input("Fica numero de Personatges(Maxim 100): "))
    if  usuario_input >100:
        while usuario_input > 100:
            usuario_input = int(input("Fica numero de Personatges(Maxim 100): "))
    
    return usuario_input

def extractNombres(numeroPersonatges):
    nombre_archivo = "csv/Personatges.csv"
    numero_lineas_a_leer = numeroPersonatges  # Cambia esto al número de líneas que deseas leer

    nombres = []

    with open(nombre_archivo, mode='r', newline='') as file:
        reader = csv.reader(file)
        for i, fila in enumerate(reader):
            if i < numero_lineas_a_leer:
                nombres.append(fila[0])  # Agregar la fila a la lista
            else:
                break
    
    return nombres


def generaPersonatges(nombres):
    nombres = random.sample(nombres, len(nombres))  

    # Genera datos aleatorios para cada columna
    genero = [random.choice(["home", "dona"]) for _ in range(len(nombres))]
    altura = [random.choice(["alt", "mitja", "baix"]) for _ in range(len(nombres))]
    color_cabell = [random.choice(["ros", "moreno", "fosc", "roig"]) for _ in range(len(nombres))]
    pell = [random.choice(["blanc", "moreno"]) for _ in range(len(nombres))]
    barba = [random.choice(["si", "no"]) for _ in range(len(nombres))]
    tipus_cos = [random.choice(["gros", "prim"]) for _ in range(len(nombres))]
    color_ulls = [random.choice(["blau", "marro", "verd"]) for _ in range(len(nombres))]
    gorro = [random.choice(["si", "no"]) for _ in range(len(nombres))]
    ulleres = [random.choice(["si", "no"]) for _ in range(len(nombres))]
    edat = [random.choice(["avi", "adult", "nen"]) for _ in range(len(nombres))]

    # Crea el DataFrame
    data = {
        "nom": nombres,
        "genere": genero,
        "altura": altura,
        "color cabell": color_cabell,
        "pell": pell,
        "barba": barba,
        "tipus cos": tipus_cos,
        "color ulls": color_ulls,
        "gorro": gorro,
        "ulleres": ulleres,
        "edat": edat
    }

    df = pd.DataFrame(data)

    # Muestra el DataFrame
    return df

def escollirPersonatge(df):
    df['PersonatgeJugador'] = False
    df['PersonatgeOrdinador'] = False
    pd.set_option('display.max_rows', None)  # Para mostrar todas las filas
    print(df.to_string())
   
    num_persontatge = int(input("Fica numero de Personatge que vols escollir: "))

    df.at[num_persontatge, 'PersonatgeJugador'] = True
    df.at[random.randint(0, len(df)), 'PersonatgeOrdinador'] = True

    return df


def pregunta_usuari(df):
   
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
''')
    num_pregunta=int(input("Fica num de la pregunta: "))

    def case_1(df):
        num_personatge = int(input("Fica el índex del personatge: "))
        if df.at[num_personatge, 'PersonatgeOrdinador'] == True:
            return "Has adivinado el personaje!"
        
        df.drop(df[num_personatge], inplace=True)
        #eliminar personaje
        return "Ese no era el personaje :("

    def case_2(df):
        genero = input("Es home o dona? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['genere'] == genero:
                    #eliminar el otro genero del mundo
                    df.drop(df[df['genere'] != genero].index, inplace=True)
                    return f"Es {genero}"
                
                df.drop(df[df['genere'] == genero].index, inplace=True)
                return f"No es {genero}"
            
        return "eres tonto"

    def case_9(df):
        altura = input("Es alt, baix o mitja d'altura? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['altura'] == altura:
                    #eliminar las otras alturas del mundo
                    df.drop(df[df['altura'] != altura].index, inplace=True)
                    return f"Es {altura}"
                
                df.drop(df[df['altura'] == altura].index, inplace=True)
                return f"No es {altura}"
            
        return "eres tonto"

    def case_11(df):
        ## 4 ¿De qué color es el cabello de esta persona? ¿Es rubio, moreno, oscuro o rojo?
        color_cabell = input("Es ros, moreno, fosc, roig? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if color_cabell == row['color cabell']:
                    #eliminar las otras alturas del mundo
                    df.drop(df[df['color cabell'] != color_cabell].index, inplace=True)
                    return f"Es {color_cabell}"
                
                df.drop(df[df['color cabell'] == color_cabell].index, inplace=True)
                return f"No es {color_cabell}"
            
        return "eres tonto"

    def case_3(df):
        ## 5 ¿Cuál es el tono de piel de esta persona? ¿Es blanco o moreno?
        pell = input("Es blanc o moreno? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if pell == row['pell']:
                    #eliminar las otras alturas del mundo
                    df.drop(df[df['pell'] != pell].index, inplace=True)
                    return f"Es {pell}"
                
                df.drop(df[df['pell'] == pell].index, inplace=True)
                return f"No es {pell}"
            
        return "eres tonto"

    def case_4(df):
        ## 6 ¿Esta persona tiene barba? (Sí/No)
        barba = input("Té barba o no? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if barba == row['barba']:
                    #eliminar las otras alturas del mundo
                    df.drop(df[df['barba'] != barba].index, inplace=True)
                    return f"Es {barba}"
                
                df.drop(df[df['barba'] == barba].index, inplace=True)
                return f"No es {barba}"
            
        return "eres tonto"

    def case_5(df):
        ## 7 ¿Cómo es el tipo de cuerpo de esta persona? ¿Es gordo o delgado?
        tipus_cos = input("Quin cos té? Es gros o prim? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if tipus_cos == row['tipus cos']:
                    #eliminar las otras alturas del mundo
                    df.drop(df[df['tipus cos'] != tipus_cos].index, inplace=True)
                    return f"Es {tipus_cos}"
                
                df.drop(df[df['tipus cos'] == tipus_cos].index, inplace=True)
                return f"No es {tipus_cos}"
            
        return "eres tonto"

    def case_8(df):
        ## 8 ¿De qué color son los ojos de esta persona? ¿Son azules, marrones o verdes?
        color_ulls = input("Te els ulls de color blau, marro o verd? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if color_ulls == row['color ulls']:
                    #eliminar las otras alturas del mundo
                    df.drop(df[df['color ulls'] != color_ulls].index, inplace=True)
                    return f"Es {color_ulls}"
                
                df.drop(df[df['color ulls'] == color_ulls].index, inplace=True)
                return f"No es {color_ulls}"
            
        return "eres tonto"

    def case_6(df):
        ## 9 ¿Lleva esta persona un gorro? (Sí/No)
        gorro = input("Porta gorro la persona? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['gorro'] == gorro:
                    #eliminar el otro genero del mundo
                    df.drop(df[df['gorro'] != gorro].index, inplace=True)
                    return f"Es {gorro}"
                
                df.drop(df[df['gorro'] == gorro].index, inplace=True)
                return f"No es {gorro}"
            
        return "eres tonto"

    def case_7(df):
        ulleres = input("Porta Ulleres si o no? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['ulleres'] == ulleres:
                    #eliminar el otro genero del mundo
                    df.drop(df[df['ulleres'] != ulleres].index, inplace=True)
                    return f"Es {ulleres}"
                
                df.drop(df[df['ulleres'] == ulleres].index, inplace=True)
                return f"No es {ulleres}"

        return "eres tonto"            

    def case_10(df):
        edat = input("Es un avi, un adult o un nen? ")
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['edat'] == edat:
                    #eliminar el otro genero del mundo
                    df.drop(df[df['edat'] != edat].index, inplace=True)
                    return f"Es {edat}"
                
                df.drop(df[df['edat'] == edat].index, inplace=True)
                return f"No es {edat}"
            
        return "eres tonto"
            
                
                


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
        accion = switch[num_pregunta](df)
        print(accion)
    else:
        print("Número no válido.")

def pregunta_ordinador(df, Npersonatges):
    numero = random.randint(1, 11)

    if numero == 1:
        pregunta = random.randint(0, Npersonatges)

        if df.at[pregunta, 'PersonatgeOrdinador'] == True:
            return "La maquina ha adivinat el personatge!"
        
        df.drop(df[pregunta], inplace=True)
        #eliminar personaje
        return "Ese no era el personaje :(" 
    elif numero <= 7:
        
    elif numero <= 10:

    elif numero == 11:

#def eliminar(df, IndexPersonatge):


