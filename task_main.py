import re


def chtenie_faila(n):
    strochka = ''
    with open(n) as f:
        for strochka_faila in f:
            strochka += strochka_faila
    return strochka


def poisk_min(strochka):
    strochka.strip()
    strochka = strochka.replace('\n', ' ')
    strochka = re.sub(r'\s+', ' ', strochka)
    strochka = strochka.split(' ')
    for i in range(0, len(strochka)):
        if strochka[i].find('.') == -1:
            strochka[i] = int(strochka[i])
        else:
            strochka[i] = float(strochka[i])
    strochka.sort()
    return strochka[0]


def poisk_max(strochka):
    strochka.strip()
    strochka = strochka.replace('\n', ' ')
    strochka = re.sub(r'\s+', ' ', strochka)
    strochka = strochka.split(' ')
    for i in range(0, len(strochka)):
        if strochka[i].find('.') == -1:
            strochka[i] = int(strochka[i])
        else:
            strochka[i] = float(strochka[i])
    strochka.sort()
    return strochka[-1]


def vichislenie_summi(strochka):
    strochka.strip()
    strochka = strochka.replace('\n', ' ')
    strochka = re.sub(r'\s+', ' ', strochka)
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
    strochka.strip()
    strochka = strochka.replace('\n', ' ')
    strochka = re.sub(r'\s+', ' ', strochka)
    strochka = strochka.split(' ')
    proizvedenie = 1
    for i in range(0, len(strochka)):
        if strochka[i].find('.') == -1:
            strochka[i] = int(strochka[i])
        else:
            strochka[i] = float(strochka[i])
        proizvedenie *= strochka[i]
    return proizvedenie
