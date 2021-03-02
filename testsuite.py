from main import check_char_aux  # se importan funciones del main
from main import caps_switch  # se importan funciones del main
import string  # se importa secuencia de caracteres


def test_mytest():  # se define una funcion para probar check_char_aux
    for i in string.ascii_letters:  # se crea un ciclo
        # se asigna a "i" una letra mayuscula o miniscula
        assert check_char_aux(i) == 0  # se verifica que cada una de las letras
        # en el codigo de check_char_aux de 0


def test_errorb():  # se define una funcion
    # se prueba el caso del punto b del enunciado
    assert check_char_aux('&%') == 1  # se verifica el caso de &%
    # el cual deberia dar 2, pero se pide un caso negativo
    # por lo que assert se compara con 1 en lugar de 2


def test_errorc():  # se define una funcion
    # se prueba el caso del punto c del enunciado
    assert check_char_aux('aa') == 2  # se verifica el caso de aa
    # el cual deberia dar 1, pero se pide un caso negativo
    # por lo que assert se compara con 2 en lugar de 1


def test_errord():  # se define una funcion
    # se prueba el caso del punto d del enunciado
    assert check_char_aux('a') == 3  # se verifica el caso de a
    # el cual deberia dar 0, pero se pide un caso negativo
    # por lo que assert se compara con 3 en lugar de 0


def test_caps():  # se define una funcion
    for i in string.ascii_letters:  # cada ciclo se le asigna un valor
        # nuevo de a-z y luego de A-Z a la variable "i"
        x = i.lower()  # se signa una variable "x" que tiene
        # el mismo caracter que alberga "i", pero en minuscula
        if i == x:  # si "i" y "x" tienen el mismo caracter
            x = x.upper()  # "x" pasa a ser mayuscula
        assert caps_switch(i) == x  # se comprueba que
        # caps_switch cambia el tamano de letra
