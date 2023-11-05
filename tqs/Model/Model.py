import pandas as pd
import random
import csv

# Genera una lista de nombres aleatorios

def amagarColumnas(df):
    columnas_a_omitir = ["PersonatgeJugador","PersonatgeOrdinador"]
    df_temporal = df.drop(columns=columnas_a_omitir)
    return df_temporal
def leerleaderboard():
        nombre_archivo = '../csv/leaderBoard.csv'
        leaderboard = []  # Lista para almacenar los datos del archivo CSV.

    
        with open(nombre_archivo, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                if len(fila) == 2:
                    nombre, tiempo = fila
                    tiempo = float(tiempo)  # Convierte el tiempo a un número decimal.
                    leaderboard.append((nombre, tiempo))

        # Ordena la lista de acuerdo al tiempo (ascendente).
        leaderboard.sort(key=lambda x: x[1])
        return leaderboard

def agregarLeaderBoard(nombre, tiempo):
    nombre_archivo = '../csv/leaderBoard.csv'
    # Abre el archivo CSV en modo de agregación (a) o crea uno nuevo si no existe.
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        # Crea un objeto escritor de CSV.
        escritor_csv = csv.writer(archivo_csv)
        
        # Escribe los datos en una fila del archivo CSV.
        escritor_csv.writerow([nombre, tiempo])

def recuperarPartida():
    df_bot = pd.read_csv('../csv/partida_guardada_bot.csv')
    df = pd.read_csv('../csv/partida_usuari.csv')

    return df,df_bot

def NumeroPersonatges(dificultad):
    if dificultad == 1:
        num= 10    
    if dificultad == 2:
        num= 20
    if dificultad == 3:
        num= 30
    return num

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

def escollirPersonatge(df, num_personatge):
    df['PersonatgeJugador'] = False
    df['PersonatgeOrdinador'] = False
    pd.set_option('display.max_rows', None)  # Para mostrar todas las filas
    print(df.to_string())

    df.at[num_personatge, 'PersonatgeJugador'] = True
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
            return "Has endevinat el personatge!"
        
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
        return accion
    else:
        print("Número no válido.")

def pregunta_ordinador(df):
    numero = random.randint(1, 11)

    if len(df) == 1:
        numero = 1

    def case_1(df):
        num_personatge = random.randint(0, len(df) - 1)
        if df.at[num_personatge, 'PersonatgeOrdinador'] == True:
            return "Has endevinat el personatge!"
        
        df.drop(df[num_personatge], inplace=True)
        #eliminar personaje
        return "Ese no era el personaje :("

    def case_2(df):
        l = ['home', 'dona']
        genero = random.choice(l)
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
        l = ['alt', 'baix', 'mitja']
        altura = random.choice(l)
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
        l = ['ros', 'roig', 'moreno', 'fosc']
        ## 4 ¿De qué color es el cabello de esta persona? ¿Es rubio, moreno, oscuro o rojo?
        color_cabell = random.choice(l)
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
        l = ['blanc', 'moreno']
        ## 5 ¿Cuál es el tono de piel de esta persona? ¿Es blanco o moreno?
        pell = random.choice(l)
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
        l = ['si', 'no']
        ## 6 ¿Esta persona tiene barba? (Sí/No)
        barba = random.choice(l)
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
        l = ['gros', 'prim']
        ## 7 ¿Cómo es el tipo de cuerpo de esta persona? ¿Es gordo o delgado?
        tipus_cos = random.choice(l)
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
        l = ['blau', 'marro', 'verd']
        ## 8 ¿De qué color son los ojos de esta persona? ¿Son azules, marrones o verdes?
        color_ulls = random.choice(l)
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
        l = ['si', 'no']
        ## 9 ¿Lleva esta persona un gorro? (Sí/No)
        gorro = random.choice(l)
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
        l = ['si', 'no']
        ulleres = random.choice(l)
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
        l = ['avi', 'adult', 'nen']
        edat = random.choice(l)
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

    if numero in switch:
        accion = switch[numero](df)
        return accion
    else:
        print("Número no válido.")


