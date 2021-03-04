import re  # Se importan expresiones regulares


def check_char_aux(_char):  # se define la funcion check_char_aux
    if isinstance(_char, str):  # si la variable _char ingresada es un string
        # isinstance devuelve true y se pasa a la siguiente linea de codigo
        if len(_char) == 1 and _char.isalpha():  # Si el largo del string
            # es igual a uno y todos los caracteres son letras
            return 0  # se retorna cero
        elif _char.isalpha():  # si lo anterior no se cumple pero _char sigue
            # siendo un string se verifica si todos sus elementos son letras
            return 'ERROR_1: Se ingresó más de un caracter'
            # si es asi, se retorna 1, como error unico para cuando
            # se ha ingresado mas de un caracter.
        elif not _char.isalpha():  # se busca si dentro del string aparece
            # cualquier otro tipo de caracteres que no sean letras.
            return 'ERROR_2:Digitos no son parte del rango A-Z'
            # se retorna un Error unico, para cuando
            # se ingrasa un string con uno o mas caracteres fuera del rango a-z
    else:  # si no se ingresa un string en la variable _char
        return 'ERROR_3: No se ingresó un caracter o string'
        # se retorna un Error unico para cuando se ingresa una
        # variable de tipo int, class, array, float, etc.


def caps_switch(_char):
    # se define la funcion caps_switch
    # que recibe una variable llamada _char
    error = check_char_aux(_char)  # se llama a la funcion check_char
    # y se asigna el parametro "error" a lo que retorne la funcion check_char
    if error == 0:  # si el valor asignado a "error" es igual a 0
        # se procede con el if
        if re.search("[a-z]", _char):  # se utiliza una expresion regular
            # buscar si el caracter ingresado en _char esta en miniscula
            _char = _char.upper()  # el caracter cambia a mayuscula con .upper
        else:  # si  la variable posee un caracter en mayuscula
            _char = _char.lower()  # se cambia a uno en minuscula con .lower
    else:  # si el valor de "error" no es 0
        return error  # se retorna alguno de los 3 errores unicos
        # que la funcion check_chr_aux retornaba
    return _char  # si no sucediera nada de lo anterior se retorna _char
