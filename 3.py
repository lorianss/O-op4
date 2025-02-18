#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

if __name__ == '__main__':
    try:
        n = int(input("Введите количество строк: "))
        m = int(input("Введите количество столбцов: "))

        d1 = int(input("Введите нижнюю границу диапазона: "))
        d2 = int(input("Введите верхнюю границу диапазона: "))

        matrix = []
        for i in range(0,n):
            matrix.append([])
            for j in range(0,m):
                matrix[i].append(randint(d1,d2))
        for i in matrix:
            print(*i)
    except:
        print("Введены неправильные значения")
