# Создайте класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически . Первая
# функция: создайте переменную и выведите её.Вторая функция:
# верните сумму 2-ух глобальных переменных.Третья функция:
# верните результат возведения первой динамической переменной
# во вторую динамическую переменную.Создайте объект класса.
# Напечатайте обе функции.Напечатайте переменную a
#
# class Example:
#     a=1
#     b=2
#
#     def __init__(self,t,k):
#         self.t = t
#         self.k = k
#
#     def perem(self):
#         self.c = 3
#         print(self.c)
#
#     def f1(self):
#         return self.a+ self.b
#
#     def f2(self):
#         return self.t**self.k
#
#
# ex=Example(2,3)
# print(ex.a)
# print(ex.f1())
# print(ex.f2())
# ex.perem()

# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических
# операций. А также функция, для ввод данных.

# class Kalkulator:
#     def __init__(self):
#         self.kalkul()
#
#     def f1(self):
#         return self.a + self.b
#
#     def f2(self):
#         return self.a-self.b
#
#     def f3(self):
#         return self.a* self.b
#
#     def f4(self):
#         if self.b == 0:
#             return 'Error'
#         else:
#             return self.a / self.b
#
#     def kalkul(self):
#         self.a = int(input())
#         self.b = int(input())
#
#
# while True:
#     print('+ , - , * , /, n-Выход')
#     x = input()
#     if x == 'n':
#         break
#     print('Num : ')
#     kal = Kalkulator()
#
#     if x =='+':
#         print(kal.f1())
#     if x == '-':
#         print(kal.f2())
#     if x == '*':
#         print(kal.f3())
#     if x == '/':
#         print(kal.f4())
