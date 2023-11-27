import unittest
from io import StringIO
import sys
import os
import pandas as pd
import copy
from unittest.mock import Mock, patch
from Model.Model import *
from Controlador.Juego import *

### Particions Equivalents
class TestEscollirPersonatge(unittest.TestCase):
    def test_particion_indices_validos(self):
        # Partició de índex vàlids
        df = pd.DataFrame({'PersonatgeJugador': [False, False, False],
                           'PersonatgeOrdinador': [False, False, False]})
        num_personatge = 1  # Índex vàlid
        resultado = escollirPersonatge(df.copy(), num_personatge)
        self.assertTrue(resultado.at[num_personatge, 'PersonatgeJugador'])
        self.assertTrue(any(resultado['PersonatgeOrdinador']))



    def test_particion_dataframe_vacio(self):
        # Partició de DataFrame buit
        df = pd.DataFrame(columns=['PersonatgeJugador', 'PersonatgeOrdinador'])
        num_personatge = 0  # Índex vàlid (encara que no cambiarà res en un DataFrame buit)
        resultado = escollirPersonatge(df.copy(), num_personatge)
        self.assertTrue(resultado.empty)
    
    def test_leaderboard(self):
        agregar_leaderboard('Pablo', 3.0125, 3)

        leaderboard = leer_leaderboard(3)

        self.assertEqual(leaderboard, [('Pablo', 3.0125)])

        os.remove('csv/leaderBoard_3.csv')


### TDD
class TestPreguntaUsuari(unittest.TestCase):
    def test_adivinar_personaje(self):
        # Cas on l'usuari adivina el personatge
        df = pd.DataFrame({'PersonatgeOrdinador': [False, False, True]})
        opcio = 2
        resultado = pregunta_usuari(df.copy(), 1, opcio)
        self.assertEqual(resultado, "Has endevinat el personatge!")

    def test_no_adivinar_personaje(self):
        # Cas on l'usuari no adivina el personatge
        df = pd.DataFrame({'PersonatgeOrdinador': [False, True, False]})
        opcio = 0
        resultado = pregunta_usuari(df.copy(), 1, opcio)
        self.assertEqual(resultado, "Ese no era el personaje :(")

### mock objects

class TestCase3(unittest.TestCase):
    @patch('pandas.DataFrame.drop')
    def test_case_3(self, mock_drop):
        # Dades de prova
        data = {'PersonatgeOrdinador': [True, False, True],
                'pell': ['blanc', 'moreno', 'blanc']}
        df = pd.DataFrame(data)

        # Configurar el DataFrame per les proves
        mock_drop.return_value = df

        # Cas de prova quan es 'blanc'
        result = pregunta_usuari(df, 3, 0)
        self.assertEqual(result, "Es blanc")

        # Verificar que truca a 'drop' amb els índex correctes
        mock_drop.assert_called_with(df[df['pell'] != 'blanc'].index, inplace=True)

        # Restableix el mock per al següent cas de prova
        mock_drop.reset_mock()

        # Cas de prova quan no es 'moreno'
        result = pregunta_usuari(df, 3, 1)
        self.assertEqual(result, "No es moreno")

        # Verificar que truca a 'drop' amb els índex correctes
        mock_drop.assert_called_with(df[df['pell'] == 'moreno'].index, inplace=True)

### Valors límit i frontera

class TestValorsLimit(unittest.TestCase):
    def test_personatges_valid(self):
        dificultat = NumeroPersonatges(3)
        self.assertEqual(dificultat, 30)

        dificultat = NumeroPersonatges(2)
        self.assertEqual(dificultat, 20)

        dificultat = NumeroPersonatges(1)
        self.assertEqual(dificultat, 10)

    def test_personatges_negatiu(self):
        dificultat = NumeroPersonatges(-1)
        self.assertEqual(dificultat, 0)
    
    def test_personatges_foralimit(self):
        dificultat = NumeroPersonatges(4)
        self.assertEqual(dificultat, 0)

### Pairwise Testing

class TestPairwiseTesting(unittest.TestCase):
    def test_pairwise_3_valores(self):
        '''
        pairwise 3				
            altura	color cabell	color ulls	edat
            alt	    ros	            blau	    avi
            alt	    moreno	        marro	    adult
            alt	    fosc	        verd	    nen
            mitja	fosc	        marro	    avi
            mitja	moreno	        blau	    nen
            mitja	ros	            verd	    adult
            baix	moreno	        verd	    avi
            baix	fosc	        blau	    adult
            baix	ros	            marro	    nen
        '''
        personatges = generaPersonatges(extractNombres(30))
        df = escollirPersonatge(personatges, 5)
        df_aux = copy.deepcopy(df)


        resultado = pregunta_usuari(df_aux, 9, 0)
        self.assertIn(resultado, ["Es alt", "No es alt"])
        resultado = pregunta_usuari(df_aux, 11, 0)
        self.assertIn(resultado, ["Té el cabell ros", "No té el cabell ros"])
        resultado = pregunta_usuari(df_aux, 8, 0)
        self.assertIn(resultado, ["Té els ulls blau", "No té els ulls blau"])
        resultado = pregunta_usuari(df_aux, 10, 0)
        self.assertIn(resultado, ["Es avi", "No es avi"])


        resultado = pregunta_usuari(df_aux, 9, 0)
        self.assertIn(resultado, ["Es alt", "No es alt"])
        resultado = pregunta_usuari(df_aux, 11, 1)
        self.assertIn(resultado, ["Té el cabell moreno", "No té el cabell moreno"])
        resultado = pregunta_usuari(df_aux, 8, 1)
        self.assertIn(resultado, ["Té els ulls marro", "No té els ulls marro"])
        resultado = pregunta_usuari(df_aux, 10, 1)
        self.assertIn(resultado, ["Es adult", "No es adult"])


        resultado = pregunta_usuari(df_aux, 9, 0)
        self.assertIn(resultado, ["Es alt", "No es alt"])
        resultado = pregunta_usuari(df_aux, 11, 2)
        self.assertIn(resultado, ["Té el cabell fosc", "No té el cabell fosc"])
        resultado = pregunta_usuari(df_aux, 8, 2)
        self.assertIn(resultado, ["Té els ulls verd", "No té els ulls verd"])
        resultado = pregunta_usuari(df_aux, 10, 2)
        self.assertIn(resultado, ["Es nen", "No es nen"])

        resultado = pregunta_usuari(df_aux, 9, 2)
        self.assertIn(resultado, ["Es mitja", "No es mitja"])
        resultado = pregunta_usuari(df_aux, 11, 2)
        self.assertIn(resultado, ["Té el cabell fosc", "No té el cabell fosc"])
        resultado = pregunta_usuari(df_aux, 8, 1)
        self.assertIn(resultado, ["Té els ulls marro", "No té els ulls marro"])
        resultado = pregunta_usuari(df_aux, 10, 0)
        self.assertIn(resultado, ["Es avi", "No es avi"])


        resultado = pregunta_usuari(df_aux, 9, 2)
        self.assertIn(resultado, ["Es mitja", "No es mitja"])
        resultado = pregunta_usuari(df_aux, 11, 1)
        self.assertIn(resultado, ["Té el cabell moreno", "No té el cabell moreno"])
        resultado = pregunta_usuari(df_aux, 8, 0)
        self.assertIn(resultado, ["Té els ulls blau", "No té els ulls blau"])
        resultado = pregunta_usuari(df_aux, 10, 2)
        self.assertIn(resultado, ["Es nen", "No es nen"])


        resultado = pregunta_usuari(df_aux, 9, 2)
        self.assertIn(resultado, ["Es mitja", "No es mitja"])
        resultado = pregunta_usuari(df_aux, 11, 0)
        self.assertIn(resultado, ["Té el cabell ros", "No té el cabell ros"])
        resultado = pregunta_usuari(df_aux, 8, 2)
        self.assertIn(resultado, ["Té els ulls verd", "No té els ulls verd"])
        resultado = pregunta_usuari(df_aux, 10, 1)
        self.assertIn(resultado, ["Es adult", "No es adult"])

        resultado = pregunta_usuari(df_aux, 9, 1)
        self.assertIn(resultado, ["Es baix", "No es baix"])
        resultado = pregunta_usuari(df_aux, 11, 1)
        self.assertIn(resultado, ["Té el cabell moreno", "No té el cabell moreno"])
        resultado = pregunta_usuari(df_aux, 8, 2)
        self.assertIn(resultado, ["Té els ulls verd", "No té els ulls verd"])
        resultado = pregunta_usuari(df_aux, 10, 0)
        self.assertIn(resultado, ["Es avi", "No es avi"])


        resultado = pregunta_usuari(df_aux, 9, 1)
        self.assertIn(resultado, ["Es baix", "No es baix"])
        resultado = pregunta_usuari(df_aux, 11, 2)
        self.assertIn(resultado, ["Té el cabell fosc", "No té el cabell fosc"])
        resultado = pregunta_usuari(df_aux, 8, 0)
        self.assertIn(resultado, ["Té els ulls blau", "No té els ulls blau"])
        resultado = pregunta_usuari(df_aux, 10, 1)
        self.assertIn(resultado, ["Es adult", "No es adult"])


        resultado = pregunta_usuari(df_aux, 9, 1)
        self.assertIn(resultado, ["Es baix", "No es baix"])
        resultado = pregunta_usuari(df_aux, 11, 0)
        self.assertIn(resultado, ["Té el cabell ros", "No té el cabell ros"])
        resultado = pregunta_usuari(df_aux, 8, 1)
        self.assertIn(resultado, ["Té els ulls marro", "No té els ulls marro"])
        resultado = pregunta_usuari(df_aux, 10, 2)
        self.assertIn(resultado, ["Es nen", "No es nen"])
    
    def test_pairwise_2_valores(self):
        '''
        pairwise 2				
            genere	pell	barba	tipus cos	gorro	ulleres
            home	moreno	si	    prim	    si	    no
            dona	blanc	no	    gros	    no	    si
        '''

        personatges = generaPersonatges(extractNombres(30))
        df = escollirPersonatge(personatges, 5)
        df_aux = copy.deepcopy(df)


        resultado = pregunta_usuari(df_aux, 2, 0)
        self.assertIn(resultado, ["Es home", "No es home"])
        resultado = pregunta_usuari(df_aux, 3, 1)
        self.assertIn(resultado, ["Es moreno", "No es moreno"])
        resultado = pregunta_usuari(df_aux, 4, 0)
        self.assertIn(resultado, ["Té barba", "No té barba"])
        resultado = pregunta_usuari(df_aux, 5, 1)
        self.assertIn(resultado, ["Es prim", "No es prim"])
        resultado = pregunta_usuari(df_aux, 6, 0)
        self.assertIn(resultado, ["Té gorro", "No té gorro"])
        resultado = pregunta_usuari(df_aux, 7, 1)
        self.assertIn(resultado, ["Té ulleres", "No té ulleres"])


        resultado = pregunta_usuari(df_aux, 2, 1)
        self.assertIn(resultado, ["Es dona", "No es dona"])
        resultado = pregunta_usuari(df_aux, 3, 0)
        self.assertIn(resultado, ["Es blanc", "No es blanc"])
        resultado = pregunta_usuari(df_aux, 4, 1)
        self.assertIn(resultado, ["Té barba", "No té barba"])
        resultado = pregunta_usuari(df_aux, 5, 0)
        self.assertIn(resultado, ["Es gros", "No es gros"])
        resultado = pregunta_usuari(df_aux, 6, 1)
        self.assertIn(resultado, ["Té gorro", "No té gorro"])
        resultado = pregunta_usuari(df_aux, 7, 0)
        self.assertIn(resultado, ["Té ulleres", "No té ulleres"])

### Coverage
class TestControlador(unittest.TestCase):
    def test_bucle_principal(self):
        df, df_bot = iniciar_juego(3)

        df, df_bot = seleccion(df, 5)

        esconder(df)

        archivos_en_csv = os.listdir('csv/')
        archivos_partida_usuari = [archivo for archivo in archivos_en_csv if archivo.startswith('partida_usuari')]
        
        if archivos_partida_usuari == []:
            df_bot.to_csv('csv/partida_guardada_bot.csv')
            df.to_csv(f'csv/partida_usuari_3.csv')

        salida, pregU, pregO = bucle_principal(df, df_bot, 1, 0, 3)
        self.assertEqual(salida, 3)

        salida, pregU, pregO = bucle_principal(df, df_bot, 0, 0, 3)
        self.assertEqual(salida, 0)
        df = pd.DataFrame({'PersonatgeOrdinador': [False, False, True]})
        resultado, pregU, pregO = bucle_principal(df, df.copy(), 1, 2, 3)
        self.assertEqual(resultado, 1)

        df = pd.DataFrame({'PersonatgeOrdinador': [False], 'PersonatgeJugador': [True]})
        resultado, pregU, pregO = bucle_principal(df, df.copy(), 1, 0, 3)
        self.assertEqual(resultado, 2)
    
    def test_final_juego(self):
        archivos_en_csv = os.listdir('csv/')
        archivos_partida_usuari = [archivo for archivo in archivos_en_csv if archivo.startswith('partida_usuari')]
        
        if archivos_partida_usuari == []:
            personatges = generaPersonatges(extractNombres(30))
            df = escollirPersonatge(personatges, 5)
            df_bot = copy.deepcopy(df)

            df_bot.to_csv('csv/partida_guardada_bot.csv')
            df.to_csv(f'csv/partida_usuari_3.csv')

        resultado = final_partida(['partida_usuari_3.csv'], 5, False, True, 'Juan', datetime.datetime.now(), 3)
        self.assertEqual(resultado, "L'ordinador ha guanyat la partida!")

        resultado = final_partida([], 0, True, False, 'Juan', datetime.datetime.now(), 2)
        self.assertEqual(resultado, "L'usuari ha guanyat la partida!")
        os.remove('csv/leaderBoard_2.csv')

        resultado = final_partida([], 5, False, False, 'Juan', datetime.datetime.now(), 3)
        self.assertEqual(resultado, "Partida guardada con éxito!")
    
    def test_leaderboard(self):
        agregar_leaderboard('Pablo', 3.0125, 3)

        leaderboard = scoreboard(3)

        self.assertEqual(leaderboard, [('Pablo', 3.0125)])

        os.remove('csv/leaderBoard_3.csv')

### Coverage i valors limits i frontera
class TestPreguntasOrdenador(unittest.TestCase):
    def test_coverage_ordenador(self):
        for i in range(0, 50):
            df, df_bot = iniciar_juego(3)

            df, df_bot = seleccion(df, 5)
            while True:
                pregO = pregunta_ordinador(df_bot)
                if pregO == "Has endevinat el personatge!":
                    break
            
            self.assertEqual(pregO, "Has endevinat el personatge!")


if __name__ == '__main__':
    unittest.main()