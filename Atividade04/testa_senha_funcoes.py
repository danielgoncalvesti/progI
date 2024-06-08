# testa_senha_funcoes.py

import unittest
from senha_funcoes import tem_digito, tem_letra, tem_caracter_especial, tem_letra_maiuscula, tem_letra_minuscula

class TestaSenhaFuncoes(unittest.TestCase):

    def testa_tem_digito(self):
        self.assertTrue(tem_digito('abc713'))
        self.assertFalse(tem_digito('abcdef'))
        self.assertTrue(tem_digito('1'))
        self.assertFalse(tem_digito(''))

    def testa_tem_letra(self):
        self.assertTrue(tem_letra('abc713'))
        self.assertTrue(tem_letra('abcdef'))
        self.assertFalse(tem_letra('71346'))
        self.assertFalse(tem_letra(''))

    def testa_tem_caracter_especial(self):
        self.assertTrue(tem_caracter_especial('abc!713'))
        self.assertTrue(tem_caracter_especial('abcdef@'))
        self.assertFalse(tem_caracter_especial('abc713'))
        self.assertFalse(tem_caracter_especial(''))

    def testa_tem_letra_maiuscula(self):
        self.assertTrue(tem_letra_maiuscula('Abc713'))
        self.assertFalse(tem_letra_maiuscula('abc713'))
        self.assertTrue(tem_letra_maiuscula('A'))
        self.assertFalse(tem_letra_maiuscula(''))

    def testa_tem_letra_minuscula(self):
        self.assertTrue(tem_letra_minuscula('Abc713'))
        self.assertTrue(tem_letra_minuscula('abc713'))
        self.assertFalse(tem_letra_minuscula('ABC713'))
        self.assertFalse(tem_letra_minuscula(''))

if __name__ == '__main__':
    unittest.main()
