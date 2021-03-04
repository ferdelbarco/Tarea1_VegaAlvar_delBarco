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
    assert check_char_aux('aa') == 'ERROR_1: Se ingresó más de un caracter'
    # se verifica el caso de aa
    # el cual deberia dar el ERROR_1
    # por lo que assert compara lo ingresado


def test_errorc():  # se define una funcion
    # se prueba el caso del punto c del enunciado
    assert check_char_aux('&%') == 'ERROR_2:Digitos no son parte del rango A-Z'
    # se verifica el caso de &%
    # el cual deberia dar el ERROR_2
    # por lo que assert compara lo ingresado


def test_errord():  # se define una funcion
    # se prueba el caso del punto d del enunciado
    assert check_char_aux(4.5) == 'ERROR_3: No se ingresó un caracter o string'
    # se verifica el caso de 4.5 un flotante
    # el cual deberia dar el ERROR_3
    # por lo que assert compara lo ingresado


def test_caps():  # se define una funcion
    for i in string.ascii_letters:  # cada ciclo se le asigna un valor
        # nuevo de a-z y luego de A-Z a la variable "i"
        x = i.lower()  # se signa una variable "x" que tiene
        # el mismo caracter que alberga "i", pero en minuscula
        if i == x:  # si "i" y "x" tienen el mismo caracter
            x = x.upper()  # "x" pasa a ser mayuscula
        assert caps_switch(i) == x  # se comprueba que
        # caps_switch cambia el tamano de letra
