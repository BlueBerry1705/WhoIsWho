from Model.Model import *
from Vista.Vista import *
import copy
def main():
    personatges = NumeroPersonatges()

    df = escollirPersonatge(generaPersonatges(extractNombres(personatges)))
    df_bot = copy.deepcopy(df)
    print(df)
    
    print(pregunta_usuari(df))

    printer(df)


