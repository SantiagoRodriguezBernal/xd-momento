# COMMANDS
# (defvar name n)
# (= name n)
# (move n)
# (turn D)
# (face 0)
# (put X n)
# (pick X n)
# (move-dir n D)
# (run-dirs Ds)
# (move-face n 0)
# (skip)

# CONTROL STRUCTURES
# (if condition Block1 Block2)
# (loop condition Block)
# (repeat n Block)
# (defun name (Params)Block)

# CONDITIONS
# (facing-p 0)
# (can-put-p X n)
# (can-pick-p X n)
# (can-move-p D)
# (not cond)

import shell
linea = shell.lista_suprema

CONTADOR1 = 0
CONTADOR2 = 0
global SINTAXIS
SINTAXIS = True

variablesDec = []
constantesTurn = ["left", "right", "around"]
constantesFace = ["north", "south", "east", "west"]
constantesDir = ["front", "right", "left", "back"]
constantesPut = ["Ballons", "Chips"]
condiciones = [""]

n = 0


def defvar(linea, variablesDec, n):
    try:
        variablesDec += [str(linea[n+1])]
        if str(linea[n+2]).isnumeric() is False:
            return False
        if str(linea[n-1]) != "LPAREN":
            return False
        if str(linea[n+3]) != "RPAREN":
            return False
    except IndexError:
        return False


def equal(linea, variablesDec, n):
    try:
        variablesDec += [str(linea[n+1])]
        if str(linea[n+2]).isnumeric() is False:
            return False
        if str(linea[n-1]) != "LPAREN":
            return False
        if str(linea[n+3]) != "RPAREN":
            return False
    except IndexError:
        return False


def move(linea, variablesDec, n):
    try:
        if str(linea[n+1]).isnumeric() or str(linea[n+1]) in variablesDec:
            pass
        else:
            return False
        if str(linea[n-1]) != "LPAREN":
            return False
        if str(linea[n+2]) != "RPAREN":
            return False
    except IndexError:
        return False


def turn(linea, constantesTurn, n):
    try:
        if str(linea[n+2]) in constantesTurn:
            pass
        else:
            return False
        if str(linea[n-1]) != "LPAREN":
            return False
        if str(linea[n+3]) != "RPAREN":
            return False
        if str(linea[n+1]) != "TWO DOTS":
            return False
    except IndexError:
        return False


def face(linea, constantesFace, n):
    try:
        if str(linea[n+2]) in constantesFace:
            pass
        else:
            return False
        if str(linea[n-1]) != "LPAREN":
            return False
        if str(linea[n+3]) != "RPAREN":
            return False
        if str(linea[n+1]) != "TWO DOTS":
            return False
    except IndexError:
        return False


def put_pick(linea, constantesPut, n, variablesDec):
    try:
        if str(linea[n+1]) in constantesPut:
            if str(linea[n+2]).isnumeric() or str(linea[n+2]) in variablesDec:
                pass
            else:
                return False
        else:
            return False
        if str(linea[n-1]) != "LPAREN":
            return False
        if str(linea[n+3]) != "RPAREN":
            return False
    except IndexError:
        return False


def move_dir(linea, constantesDir, n, variablesDec):
    try:
        if str(linea[n+3]).isnumeric() or str(linea[n+3]) in variablesDec:
            if str(linea[n+5]) in constantesDir:
                pass
            else:
                return False
        else:
            return False
        if str(linea[n-1]) != "LPAREN":
            return False
        if str(linea[n+6]) != "RPAREN":
            return False
        if str(linea[n+4]) != "TWO DOTS":
            return False
    except IndexError:
        return False


def run_dirs(linea, constantesDir, n):
    try:
        if str(linea[n+3]) != "LPAREN":
            return False
        u = n + 4
        contadorDots = 0
        contadorDirec = 0
        for elem in linea[n+4:]:
            if str(elem) == "TWO DOTS":
                contadorDots += 1
            elif str(elem) in constantesDir:
                contadorDirec += 1
                if str(linea[u-1]) != "TWO DOTS":
                    return False
            elif str(elem) == "RPAREN":
                break
            else:
                return False
            u += 1
        if contadorDirec != contadorDots:
            return False
    except IndexError:
        return False


def move_face(linea, constantesFace, n):
    try:
        if str(linea[n+3]) in variablesDec or str(linea[n+3]).isnumeric():
            if str(linea[n+4]) == "TWO DOTS":
                if str(linea[n+5]) in constantesFace:
                    pass
                else:
                    return False
            else:
                return False
        else:
            return False
        if str(linea[n-1]) != "LPAREN":
            return False
        if str(linea[n+6]) != "RPAREN":
            return False
    except IndexError:
        return False


def skipfunc(linea, n):
    try:
        if str(linea[n-1]) != "LPAREN":
            return False
        if str(linea[n+1]) != "RPAREN":
            return False
    except IndexError:
        return False


for elemento in linea:

    if elemento.type == "LPAREN":
        CONTADOR1 += 1

    elif elemento.type == "RPAREN":
        CONTADOR2 += 1

    elif elemento.type == "defvar":
        if defvar(linea, variablesDec, n) is not None:
            SINTAXIS = False

    elif elemento.type == "EQUAL":
        if equal(linea, variablesDec, n) is not None:
            SINTAXIS = False

    elif elemento.type == "move" and str(linea[n-2]) != "can" and str(linea[n+2]) != "dir" and str(linea[n+2]) != "face":
        if move(linea, variablesDec, n) is not None:
            SINTAXIS = False

    elif elemento.type == "turn":
        if turn(linea, constantesTurn, n) is not None:
            SINTAXIS = False

    elif elemento.type == "face" and str(linea[n-1]) == "LPAREN":
        if face(linea, constantesFace, n) is not None:
            SINTAXIS = False

    # elif elemento.type == "put" or elemento.type == "pick":
        # if put_pick(linea, constantesPut, n, variablesDec) is not None:
            # SINTAXIS = False
        # TODO con parametros en variablesDec, de defun

    elif elemento.type == "move" and str(linea[n+1]) == "LINE" and str(linea[n+2]) == "dir":
        if move_dir(linea, constantesDir, n, variablesDec) is not None:
            SINTAXIS = False

    elif elemento.type == "run" and str(linea[n+1]) == "LINE" and str(linea[n+2]) == "dirs" and str(linea[n+3]) == "LPAREN":
        if run_dirs(linea, constantesDir, n) is not None:
            SINTAXIS = False

    elif elemento.type == "move" and str(linea[n+1]) == "LINE" and str(linea[n+2]) == "face":
        if move_face(linea, constantesFace, n) is not None:
            SINTAXIS = False

    elif elemento.type == "skip":
        if skipfunc(linea, n) is not None:
            SINTAXIS = False

    # elif elemento.type == "if":
        # TODO estructuras de control

    # else:
        # SINTAXIS = False

    n += 1


if SINTAXIS is True and CONTADOR1 == CONTADOR2:
    print("La sintaxis del archivo es correcta")

else:
    print("La sintaxis del archivo es incorrecta")

print(linea)
