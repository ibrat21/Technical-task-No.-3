def chtenie_faila(n):
    with open(n) as f:
        for strochka in f:
            return strochka


def poisk_min(strochka):
    strochka = strochka.split(' ')
    for i in range(0, len(strochka)):
        if strochka[i].find('.') == -1:
            strochka[i] = int(strochka[i])
        else:
            strochka[i] = float(strochka[i])
    strochka.sort()
    return strochka[0]


def poisk_max(strochka):
    strochka = strochka.split(' ')
    for i in range(0, len(strochka)):
        if strochka[i].find('.') == -1:
            strochka[i] = int(strochka[i])
        else:
            strochka[i] = float(strochka[i])
    strochka.sort()
    return strochka[-1]


def vichislenie_summi(strochka):
    strochka = strochka.split(' ')
    summa = 0
    for i in range(0, len(strochka)):
        if strochka[i].find('.') == -1:
            strochka[i] = int(strochka[i])
        else:
            strochka[i] = float(strochka[i])
        summa += strochka[i]
    return summa


def vichislenie_proizvedeniya(strochka):
    strochka = strochka.split(' ')
    proizvedenie = 1
    for i in range(0, len(strochka)):
        if strochka[i].find('.') == -1:
            strochka[i] = int(strochka[i])
        else:
            strochka[i] = float(strochka[i])
        proizvedenie *= strochka[i]
    return proizvedenie
