import pytest

from main import check_char_aux
from main import caps_switch


def test_mytest():
    assert check_char_aux('a') == 0
    assert check_char_aux('b') == 0
    assert check_char_aux('c') == 0
    assert check_char_aux('d') == 0
    assert check_char_aux('e') == 0
    assert check_char_aux('f') == 0
    assert check_char_aux('g') == 0
    assert check_char_aux('h') == 0
    assert check_char_aux('i') == 0
    assert check_char_aux('j') == 0
    assert check_char_aux('k') == 0
    assert check_char_aux('l') == 0
    assert check_char_aux('m') == 0
    assert check_char_aux('n') == 0
    assert check_char_aux('o') == 0
    assert check_char_aux('p') == 0
    assert check_char_aux('q') == 0
    assert check_char_aux('r') == 0
    assert check_char_aux('s') == 0
    assert check_char_aux('t') == 0
    assert check_char_aux('u') == 0
    assert check_char_aux('v') == 0
    assert check_char_aux('w') == 0
    assert check_char_aux('x') == 0
    assert check_char_aux('y') == 0
    assert check_char_aux('z') == 0

    assert check_char_aux('A') == 0
    assert check_char_aux('B') == 0
    assert check_char_aux('C') == 0
    assert check_char_aux('D') == 0
    assert check_char_aux('E') == 0
    assert check_char_aux('F') == 0
    assert check_char_aux('G') == 0
    assert check_char_aux('H') == 0
    assert check_char_aux('I') == 0
    assert check_char_aux('J') == 0
    assert check_char_aux('K') == 0
    assert check_char_aux('L') == 0
    assert check_char_aux('M') == 0
    assert check_char_aux('N') == 0
    assert check_char_aux('O') == 0
    assert check_char_aux('P') == 0
    assert check_char_aux('Q') == 0
    assert check_char_aux('R') == 0
    assert check_char_aux('S') == 0
    assert check_char_aux('T') == 0
    assert check_char_aux('U') == 0
    assert check_char_aux('V') == 0
    assert check_char_aux('W') == 0
    assert check_char_aux('X') == 0
    assert check_char_aux('Y') == 0
    assert check_char_aux('Z') == 0


def test_errorB():
    assert check_char_aux('aa') == 1


def test_errorC():
    assert check_char_aux('%&') == 2


def test_errorD():
    assert check_char_aux(4.5) == 3


def test_caps():
    assert caps_switch('a') == 'A'
    assert caps_switch('b') == 'B'
    assert caps_switch('c') == 'C'
    assert caps_switch('d') == 'D'
    assert caps_switch('e') == 'E'
    assert caps_switch('f') == 'F'
    assert caps_switch('g') == 'G'
    assert caps_switch('h') == 'H'
    assert caps_switch('i') == 'I'
    assert caps_switch('j') == 'J'
    assert caps_switch('k') == 'K'
    assert caps_switch('l') == 'L'
    assert caps_switch('m') == 'M'
    assert caps_switch('n') == 'N'
    assert caps_switch('o') == 'O'
    assert caps_switch('p') == 'P'
    assert caps_switch('q') == 'Q'
    assert caps_switch('r') == 'R'
    assert caps_switch('s') == 'S'
    assert caps_switch('t') == 'T'
    assert caps_switch('u') == 'U'
    assert caps_switch('v') == 'V'
    assert caps_switch('w') == 'W'
    assert caps_switch('x') == 'X'
    assert caps_switch('y') == 'Y'
    assert caps_switch('z') == 'Z'
