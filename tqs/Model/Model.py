import pandas as pd
import random
import csv

def amagarColumnas(df):
    columnas_a_omitir = ["PersonatgeJugador","PersonatgeOrdinador"]
    df_temporal = df.drop(columns=columnas_a_omitir)
    return df_temporal

def leer_leaderboard(dificultad):
    nombre_archivo = f'csv/leaderBoard_{dificultad}.csv'
    leaderboard = []  # Llista per emmagatzemar les dades del arxiu CSV.

    with open(nombre_archivo, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if len(fila) == 2:
                nombre, tiempo = fila
                tiempo = float(tiempo)  # Converteix el temps a un número decimal.
                leaderboard.append((nombre, tiempo))

    # Ordenar la llista d'acuerdo al temps
    leaderboard.sort(key=lambda x: x[1])
    return leaderboard

def agregar_leaderboard(nombre, tiempo, dificultad):
    nombre_archivo = f'csv/leaderBoard_{dificultad}.csv'

    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([nombre, tiempo])

def NumeroPersonatges(dificultad):
    num = 0
    if dificultad == 1:
        num= 10    
    if dificultad == 2:
        num= 20
    if dificultad == 3:
        num= 30
    return num

def extractNombres(numeroPersonatges):
    nombre_archivo = "csv/Personatges.csv"
    numero_lineas_a_leer = numeroPersonatges  # Cambia això al número de línies que vulguis llegir

    nombres = []

    with open(nombre_archivo, mode='r', newline='') as file:
        reader = csv.reader(file)
        for i, fila in enumerate(reader):
            if i < numero_lineas_a_leer:
                nombres.append(fila[0])  # Agregar la fila a la llista
            else:
                break
    
    return nombres


def generaPersonatges(nombres):
    nombres = random.sample(nombres, len(nombres))  

    # Genera dades aleatories per a cada columna
    genero = [random.choice(["home", "dona"]) for _ in range(len(nombres))]
    altura = [random.choice(["alt", "mitja", "baix"]) for _ in range(len(nombres))]
    color_cabell = [random.choice(["ros", "moreno", "fosc"]) for _ in range(len(nombres))]
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

    return df

def escollirPersonatge(df, num_personatge):
    if num_personatge < 0 or num_personatge >= len(df):
        # Índex fora del rang, no realitzar cambis en el DataFrame original
        return df.copy()

    df['PersonatgeJugador'] = False
    df['PersonatgeOrdinador'] = False
    pd.set_option('display.max_rows', None)  # Mostrar totes les files

    df.at[num_personatge, 'PersonatgeJugador'] = True
    df.at[random.randint(0, len(df)), 'PersonatgeOrdinador'] = True

    return df


def pregunta_usuari(df, pregunta, opcio):
    def case_1(df, opcio):
        if df.at[opcio, 'PersonatgeOrdinador'] == True:
            return "Has endevinat el personatge!"
        
        df.drop(opcio, inplace=True)
        # eliminar personatge
        return "Ese no era el personaje :("

    def case_2(df, opcio):
        l = ['home', 'dona']
        cat = l[opcio]
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['genere'] == cat:
                    # eliminar genere
                    df.drop(df[df['genere'] != cat].index, inplace=True)
                    return f"Es {cat}"
                
                df.drop(df[df['genere'] == cat].index, inplace=True)
                return f"No es {cat}"
            
    def case_9(df, opcio):
        l = ['alt', 'baix', 'mitja']
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['altura'] == l[opcio]:
                    # eliminar altura 
                    df.drop(df[df['altura'] != l[opcio]].index, inplace=True)
                    return f"Es {l[opcio]}"
                
                df.drop(df[df['altura'] == l[opcio]].index, inplace=True)
                return f"No es {l[opcio]}"
            
    def case_11(df, opcio):
        l = ['ros', 'moreno', 'fosc']
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if l[opcio] == row['color cabell']:
                    # eliminar color pel 
                    df.drop(df[df['color cabell'] != l[opcio]].index, inplace=True)
                    return f"Té el cabell {l[opcio]}"
                
                df.drop(df[df['color cabell'] == l[opcio]].index, inplace=True)
                return f"No té el cabell {l[opcio]}"
            
    def case_3(df, opcio):
        l = ['blanc', 'moreno']
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if l[opcio] == row['pell']:
                    # eliminar pell
                    df.drop(df[df['pell'] != l[opcio]].index, inplace=True)
                    return f"Es {l[opcio]}"
                
                df.drop(df[df['pell'] == l[opcio]].index, inplace=True)
                return f"No es {l[opcio]}"
            
    def case_4(df, opcio):
        l = ['si', 'no']
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if l[opcio] == row['barba']:
                    #eliminar barba
                    df.drop(df[df['barba'] != l[opcio]].index, inplace=True)
                    return "Té barba"
                
                df.drop(df[df['barba'] == l[opcio]].index, inplace=True)
                return "No té barba"
            
    def case_5(df, opcio):
        l = ['gros', 'prim']
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if l[opcio] == row['tipus cos']:
                    #eliminar tipus cos
                    df.drop(df[df['tipus cos'] != l[opcio]].index, inplace=True)
                    return f"Es {l[opcio]}"
                
                df.drop(df[df['tipus cos'] == l[opcio]].index, inplace=True)
                return f"No es {l[opcio]}"
            
    def case_8(df, opcio):
        l = ['blau', 'marro', 'verd']
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if l[opcio] == row['color ulls']:
                    #eliminar color ulls
                    df.drop(df[df['color ulls'] != l[opcio]].index, inplace=True)
                    return f"Té els ulls {l[opcio]}"
                
                df.drop(df[df['color ulls'] == l[opcio]].index, inplace=True)
                return f"No té els ulls {l[opcio]}"
             
    def case_6(df, opcio):
        l = ['si', 'no']
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['gorro'] == l[opcio]:
                    #eliminar gorro
                    df.drop(df[df['gorro'] != l[opcio]].index, inplace=True)
                    return "Té gorro"
                
                df.drop(df[df['gorro'] == l[opcio]].index, inplace=True)
                return "No té gorro" 

    def case_7(df, opcio):
        l = ['si', 'no']
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['ulleres'] == l[opcio]:
                    #eliminar ulleres
                    df.drop(df[df['ulleres'] != l[opcio]].index, inplace=True)
                    return "Té ulleres"
                
                df.drop(df[df['ulleres'] == l[opcio]].index, inplace=True)
                return f"No té ulleres"

    def case_10(df, opcio):
        l = ['avi', 'adult', 'nen']
        for index, row in df.iterrows():
            if row['PersonatgeOrdinador'] == True:
                if row['edat'] == l[opcio]:
                    #eliminar edat
                    df.drop(df[df['edat'] != l[opcio]].index, inplace=True)
                    return f"Es {l[opcio]}"
                
                df.drop(df[df['edat'] == l[opcio]].index, inplace=True)
                return f"No es {l[opcio]}"

    # Crear un diccionari que mapeja els números a las funcions de case
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

    accion = switch[pregunta](df, opcio)
    return accion

def pregunta_ordinador(df):
    numero = random.randint(1, 11)
    if len(df) == 1:
        numero = 1
    
    def case_1(df):
        while True:
            num_personatge = random.randint(0, df.index.max())
            try:
                if df.at[num_personatge, 'PersonatgeJugador'] == True:
                    return "Has endevinat el personatge!"
                
                df.drop(num_personatge, inplace=True)
                #eliminar personatge
                return "Ese no era el personaje :("
            except KeyError:
                continue
        
        

    def case_2(df):
        l = ['home', 'dona']
        genero = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if row['genere'] == genero:
                    #eliminar genere
                    df.drop(df[df['genere'] != genero].index, inplace=True)
                    return f"Es {genero}"
                
                df.drop(df[df['genere'] == genero].index, inplace=True)
                return f"No es {genero}"

    def case_9(df):
        l = ['alt', 'baix', 'mitja']
        altura = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if row['altura'] == altura:
                    #eliminar altura
                    df.drop(df[df['altura'] != altura].index, inplace=True)
                    return f"Es {altura}"
                
                df.drop(df[df['altura'] == altura].index, inplace=True)
                return f"No es {altura}"

    def case_11(df):
        l = ['ros', 'moreno', 'fosc']
        color_cabell = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if color_cabell == row['color cabell']:
                    #eliminar color cabell
                    df.drop(df[df['color cabell'] != color_cabell].index, inplace=True)
                    return f"Té el cabell {color_cabell}"
                
                df.drop(df[df['color cabell'] == color_cabell].index, inplace=True)
                return f"No té el cabell {color_cabell}"

    def case_3(df):
        l = ['blanc', 'moreno']
        pell = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if pell == row['pell']:
                    #eliminar pell
                    df.drop(df[df['pell'] != pell].index, inplace=True)
                    return f"Es {pell}"
                
                df.drop(df[df['pell'] == pell].index, inplace=True)
                return f"No es {pell}"

    def case_4(df):
        l = ['si', 'no']
        barba = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if barba == row['barba']:
                    #eliminar barba
                    df.drop(df[df['barba'] != barba].index, inplace=True)
                    return "Té barba"
                
                df.drop(df[df['barba'] == barba].index, inplace=True)
                return "No té barba"
            

    def case_5(df):
        l = ['gros', 'prim']
        tipus_cos = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if tipus_cos == row['tipus cos']:
                    #eliminar tipus cos
                    df.drop(df[df['tipus cos'] != tipus_cos].index, inplace=True)
                    return f"Es {tipus_cos}"
                
                df.drop(df[df['tipus cos'] == tipus_cos].index, inplace=True)
                return f"No es {tipus_cos}"

    def case_8(df):
        l = ['blau', 'marro', 'verd']
        color_ulls = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if color_ulls == row['color ulls']:
                    #eliminar color ulls
                    df.drop(df[df['color ulls'] != color_ulls].index, inplace=True)
                    return f"Té els ulls {color_ulls}"
                
                df.drop(df[df['color ulls'] == color_ulls].index, inplace=True)
                return f"No té els ulls {color_ulls}"

    def case_6(df):
        l = ['si', 'no']
        gorro = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if row['gorro'] == gorro:
                    #eliminar gorro
                    df.drop(df[df['gorro'] != gorro].index, inplace=True)
                    return "Té gorro"
                
                df.drop(df[df['gorro'] == gorro].index, inplace=True)
                return "No té gorro"

    def case_7(df):
        l = ['si', 'no']
        ulleres = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if row['ulleres'] == ulleres:
                    #eliminar ulleres
                    df.drop(df[df['ulleres'] != ulleres].index, inplace=True)
                    return "Té ulleres"
                
                df.drop(df[df['ulleres'] == ulleres].index, inplace=True)
                return "No té ulleres"        

    def case_10(df):
        l = ['avi', 'adult', 'nen']
        edat = random.choice(l)
        for index, row in df.iterrows():
            if row['PersonatgeJugador'] == True:
                if row['edat'] == edat:
                    #eliminar edat
                    df.drop(df[df['edat'] != edat].index, inplace=True)
                    return f"Es {edat}"
                
                df.drop(df[df['edat'] == edat].index, inplace=True)
                return f"No es {edat}"

    # Crear un diccionari que mapeja els números a las funcions de case
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

    accion = switch[numero](df)
    return accion


