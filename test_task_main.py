import os
import random
import time
from functools import reduce
from operator import mul

import memory_profiler

from task_main import chtenie_faila, poisk_min, poisk_max, vichislenie_summi, vichislenie_proizvedeniya


def test_poisk_min():
    kolvo_testov = 100
    for nomer_testa in range(0, kolvo_testov):
        chisla_dlya_file = []
        kolvo_chisel = 100
        nizhnyaya_granica_celih = -100000
        verhnyaya_granica_celih = 100000
        nizhnyaya_granica_veshestvennih = -100000.0
        verhnyaya_granica_veshestvennih = 100000.0
        for i in range(0, kolvo_chisel):
            if random.randint(0, 1) == 0:
                chislo = 'целое'
            else:
                chislo = 'вещественное'
            if chislo == 'целое':
                chislo = random.randint(nizhnyaya_granica_celih, verhnyaya_granica_celih)
                chisla_dlya_file.append(chislo)
            elif chislo == 'вещественное':
                chislo = random.uniform(nizhnyaya_granica_veshestvennih, verhnyaya_granica_veshestvennih)
                chisla_dlya_file.append(chislo)
        with open('числа для тестов.txt', 'w') as f:
            strochka = ''
            for i in range(0, len(chisla_dlya_file)):
                if i != len(chisla_dlya_file) - 1:
                    strochka += (str(chisla_dlya_file[i]) + ' ')
                else:
                    strochka += str(chisla_dlya_file[i])
            f.write(strochka)
        assert min(chisla_dlya_file) == poisk_min(chtenie_faila('числа для тестов.txt'))


def test_poisk_max():
    kolvo_testov = 100
    for nomer_testa in range(0, kolvo_testov):
        chisla_dlya_file = []
        kolvo_chisel = 100
        nizhnyaya_granica_celih = -100000
        verhnyaya_granica_celih = 100000
        nizhnyaya_granica_veshestvennih = -100000.0
        verhnyaya_granica_veshestvennih = 100000.0
        for i in range(0, kolvo_chisel):
            if random.randint(0, 1) == 0:
                chislo = 'целое'
            else:
                chislo = 'вещественное'
            if chislo == 'целое':
                chislo = random.randint(nizhnyaya_granica_celih, verhnyaya_granica_celih)
                chisla_dlya_file.append(chislo)
            elif chislo == 'вещественное':
                chislo = random.uniform(nizhnyaya_granica_veshestvennih, verhnyaya_granica_veshestvennih)
                chisla_dlya_file.append(chislo)
        with open('числа для тестов.txt', 'w') as f:
            strochka = ''
            for i in range(0, len(chisla_dlya_file)):
                if i != len(chisla_dlya_file) - 1:
                    strochka += (str(chisla_dlya_file[i]) + ' ')
                else:
                    strochka += str(chisla_dlya_file[i])
            f.write(strochka)
        assert max(chisla_dlya_file) == poisk_max(chtenie_faila('числа для тестов.txt'))


def test_vichislenie_summi():
    kolvo_testov = 100
    for nomer_testa in range(0, kolvo_testov):
        chisla_dlya_file = []
        kolvo_chisel = 100
        nizhnyaya_granica_celih = -100000
        verhnyaya_granica_celih = 100000
        nizhnyaya_granica_veshestvennih = -100000.0
        verhnyaya_granica_veshestvennih = 100000.0
        for i in range(0, kolvo_chisel):
            if random.randint(0, 1) == 0:
                chislo = 'целое'
            else:
                chislo = 'вещественное'
            if chislo == 'целое':
                chislo = random.randint(nizhnyaya_granica_celih, verhnyaya_granica_celih)
                chisla_dlya_file.append(chislo)
            elif chislo == 'вещественное':
                chislo = random.uniform(nizhnyaya_granica_veshestvennih, verhnyaya_granica_veshestvennih)
                chisla_dlya_file.append(chislo)
        with open('числа для тестов.txt', 'w') as f:
            strochka = ''
            for i in range(0, len(chisla_dlya_file)):
                if i != len(chisla_dlya_file) - 1:
                    strochka += (str(chisla_dlya_file[i]) + ' ')
                else:
                    strochka += str(chisla_dlya_file[i])
            f.write(strochka)
        assert sum(chisla_dlya_file) == vichislenie_summi(chtenie_faila('числа для тестов.txt'))


def test_vichislenie_proizvedeniya():
    kolvo_testov = 100
    for nomer_testa in range(0, kolvo_testov):
        chisla_dlya_file = []
        kolvo_chisel = 100
        nizhnyaya_granica_celih = -100000
        verhnyaya_granica_celih = 100000
        nizhnyaya_granica_veshestvennih = -100000.0
        verhnyaya_granica_veshestvennih = 100000.0
        for i in range(0, kolvo_chisel):
            if random.randint(0, 1) == 0:
                chislo = 'целое'
            else:
                chislo = 'вещественное'
            if chislo == 'целое':
                chislo = random.randint(nizhnyaya_granica_celih, verhnyaya_granica_celih)
                chisla_dlya_file.append(chislo)
            elif chislo == 'вещественное':
                chislo = random.uniform(nizhnyaya_granica_veshestvennih, verhnyaya_granica_veshestvennih)
                chisla_dlya_file.append(chislo)
        with open('числа для тестов.txt', 'w') as f:
            strochka = ''
            for i in range(0, len(chisla_dlya_file)):
                if i != len(chisla_dlya_file) - 1:
                    strochka += (str(chisla_dlya_file[i]) + ' ')
                else:
                    strochka += str(chisla_dlya_file[i])
            f.write(strochka)
        assert reduce(mul, chisla_dlya_file) == vichislenie_proizvedeniya(chtenie_faila('числа для тестов.txt'))


def test_skorosti():
    chisla_dlya_file = []
    kolvo_testov = 100
    nizhnyaya_granica_celih = -100000
    verhnyaya_granica_celih = 100000
    nizhnyaya_granica_veshestvennih = -100000.0
    verhnyaya_granica_veshestvennih = 100000.0
    print('\n')
    for nomer_testa in range(0, kolvo_testov):
        kolvo_chisel = 100
        for i in range(0, kolvo_chisel):
            if random.randint(0, 1) == 0:
                chislo = 'целое'
            else:
                chislo = 'вещественное'
            if chislo == 'целое':
                chislo = random.randint(nizhnyaya_granica_celih, verhnyaya_granica_celih)
                chisla_dlya_file.append(chislo)
            elif chislo == 'вещественное':
                chislo = random.uniform(nizhnyaya_granica_veshestvennih, verhnyaya_granica_veshestvennih)
                chisla_dlya_file.append(chislo)
        with open('числа для тестов.txt', 'w') as f:
            strochka = ''
            for i in range(0, len(chisla_dlya_file)):
                if i != len(chisla_dlya_file) - 1:
                    strochka += (str(chisla_dlya_file[i]) + ' ')
                else:
                    strochka += str(chisla_dlya_file[i])
            f.write(strochka)
        with open('числа для тестов.txt') as f:
            f.seek(0, os.SEEK_END)
            vremya_do_testa = time.time()
            strochka = chtenie_faila('числа для тестов.txt')
            poisk_min(strochka)
            poisk_max(strochka)
            vichislenie_summi(strochka)
            vichislenie_proizvedeniya(strochka)
            vremya_posle_testa = time.time()
            vremya_raboty_programmy = vremya_posle_testa - vremya_do_testa
            razmer_file = f.tell()
            print('Размер файла: ', razmer_file, 'Программа работала: ', vremya_raboty_programmy)


def test_pamyati():
    chisla_dlya_file = []
    kolvo_testov = 6
    nizhnyaya_granica_celih = -100000
    verhnyaya_granica_celih = 100000
    nizhnyaya_granica_veshestvennih = -100000.0
    verhnyaya_granica_veshestvennih = 100000.0
    print('\n')
    for nomer_testa in range(0, kolvo_testov):
        kolvo_chisel = 100
        for i in range(0, kolvo_chisel):
            if random.randint(0, 1) == 0:
                chislo = 'целое'
            else:
                chislo = 'вещественное'
            if chislo == 'целое':
                chislo = random.randint(nizhnyaya_granica_celih, verhnyaya_granica_celih)
                chisla_dlya_file.append(chislo)
            elif chislo == 'вещественное':
                chislo = random.uniform(nizhnyaya_granica_veshestvennih, verhnyaya_granica_veshestvennih)
                chisla_dlya_file.append(chislo)
        with open('числа для тестов.txt', 'w') as f:
            strochka = ''
            for i in range(0, len(chisla_dlya_file)):
                if i != len(chisla_dlya_file) - 1:
                    strochka += (str(chisla_dlya_file[i]) + ' ')
                else:
                    strochka += str(chisla_dlya_file[i])
            f.write(strochka)
        with open('числа для тестов.txt') as f:
            f.seek(0, os.SEEK_END)
            strochka = chtenie_faila('числа для тестов.txt')
            pamyat_poisk_min = max(memory_profiler.memory_usage((poisk_min, (strochka,), {})))
            pamyat_poisk_max = max(memory_profiler.memory_usage((poisk_max, (strochka,), {})))
            pamyat_vichislenie_summi = max(memory_profiler.memory_usage((vichislenie_summi, (strochka,), {})))
            pamyat_vichislenie_proizvedeniya = max(memory_profiler.memory_usage((vichislenie_proizvedeniya, (strochka,), {})))
            obschaya_pamyat = pamyat_poisk_min + pamyat_poisk_max + pamyat_vichislenie_summi + pamyat_vichislenie_proizvedeniya
            razmer_file = f.tell()
            print('Размер файла: ', razmer_file, 'Суммарное количество памяти, затраченное на работу всех функций основной программы: ', obschaya_pamyat)
