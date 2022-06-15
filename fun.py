# def sum_chisel():
#     m=range(5)
#     print(sum(m))
# sum_chisel()

# def is_year_leap(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# print(is_year_leap(int(input('Введите год  '))))
# import math
#
#
# def square(a):
#     return a*4, a**2,math.sqrt(2)*a
#
#
# print(square(int(input('Введите сторону квадрата '))))

# def season(number):
#     if number == 1 or number==2 or number==12:
#         print('зима')
#     elif number == 3 or number==4 or number ==5:
#         print('Весна')
#     elif number == 6 or number ==7 or number ==8:
#         print('Лето')
#     else:
#         print('осень')
#
#
# n = int(input('ведите номер месяца '))
#
# season(n)

# def is_prime(ch):
#     d=2
#     while ch % d !=0:
#         d+=1
#     return d == ch
#
#
# ch = int(input('Введите число  '))
# print(is_prime(ch))

# import random
# n=10
# a=[0]*n
#
# for i in range(n):
#     a[i]=random.randint(1,100)
#
# def summa_mas(a):
#     s=0
#     for i in range(n):
#         s+=a[i]
#         return s/n
#
#
# print(a)
# print(summa_mas(a))

# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

# a = int(input('Введите число a  '))
# b = int(input('Введите число b  '))
# c = str(input('Введите математическую операцию  '))
#
#
# def oper():
#     if c == '+':
#         print(a+b)
#     elif c== '-':
#         print(a-b)
#     elif c=='*':
#         print(a*b)
#     elif c=='/':
#         try:
#             a/b
#         except ZeroDivisionError:
#             print('На 0 делить нельзя')
#         else:
#             print(a/b)
#
#
# oper()





