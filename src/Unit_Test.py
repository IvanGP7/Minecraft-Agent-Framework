
from Acciones.insult_bot import *
from Acciones.dinamita import *
from Acciones.chatgpt import *

import unittest

class TestFunciones(unittest.TestCase):

#
# Test de dinamita 
# 
    def test_Dinamita(self):
        self.assertEqual(dinamita(10), (10 * 10 * 10))
        self.assertEqual(dinamita(7), (7 * 7 * 7))

#
# Test de la funcion insultos
# 
    def test_Insultos(self):
        self.assertEqual(print_lista_insultos(), 6)

        self.assertEqual(print_insult(2), 0)
        self.assertEqual(print_insult(60), 1)

        self.assertEqual(add_insulto("rata"), 0)
        self.assertEqual(add_insulto("rata"), 1)

        self.assertEqual(print_lista_insultos(), 7)

#
# Testear si funciona la conexión con ChatGPT
# 
    def test_ChatGPT(self):
        print("Test con ChatGPT:")
        print("Contexión ha sido: ")
        self.assertNotEqual(preguntar_a_chatgpt("Dime tu numero favorito"), '\0')


if __name__ == '__main__':
    unittest.main()