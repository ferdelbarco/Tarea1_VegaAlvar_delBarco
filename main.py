import re


def check_char_aux(_char):
    if isinstance(_char, str):
        if len(_char) == 1 and _char.isalpha():
            return 0
        elif _char.isalpha():
            return 1
        elif not _char.isalpha():
            return 2
    else:
        return 3


def check_char(_char):
    try:
        _char = int(_char)
        _char = float(_char)

        return 'Usted ha ingresado un parametro que no es un caracter o string'

    except ValueError:
        if len(_char) == 1:
            if re.search("[a-z]", _char.lower()):
                return '0'
            elif re.search("[A-Z]", _char):
                return '0'
            else:
                return 'Usted ha ingresado uno o mas caracteres que no son parte del rango A-Z'
        else:
            if re.search("\\W", _char):
                return 'Usted ha ingresado uno o mas caracteres que no son parte del rango A-Z'
            elif re.search("[0-9]", _char):
                return 'Usted ha ingresado uno o mas caracteres que no son parte del rango A-Z'
            else:
                return 'Usted ha ingresado mas de un caracter'


def caps_switch(_char):
    error = check_char(_char)
    if error == '0':
        if re.search("[a-z]", _char):
            _char = _char.upper()
        else:
            _char = _char.lower()
    else:
        return error

    return _char


print(caps_switch('a5'))
print(caps_switch('B'))
