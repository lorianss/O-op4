#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n1 = input("Введите первое число: ")
    n2 = input("Введите второе число: ")
    try:
        print(f"Результат: {float(n1)+float(n2)}")
    except:
        print(f"Результат: {str(n1)+str(n2)}")

