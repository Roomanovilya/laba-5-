'''
Лабораторная работа №5
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной
и графической форме в виде отчета по лабораторной работе.
F(1) = 1; G(1) = 1;
F(n) = (-1)n*(F(n–1) /(2n)! – G(n–1))
G(n) = F(n–1) + 2*G(n–1), при n >=2
'''

import timeit
import matplotlib.pyplot as plt

n=int(input('введите число n до которого нужно вычислять функцию = '))
n1= range(2, n)

# Глобальные переменные
lG = 1
lF = 1
step = 1
last_fac = 1

def dynamic_fac(n):
    global last_fac
    last_fac *=n 
    return last_fac

# Функция для рекурсивного вычисления факториала
def fac_rec(n):
    if n == 1:
        return 1
    else:
        return n * fac_rec(n-1)

# Функция для итеративного вычисления факториала
def fac_iterat(n):
    result = 1
    for i in range(2,n+1,1):
        result *= i
    return result

# F
def dynamic_F(n):
    global lF, step
    if n == 1:
        return 1
    else:
        step *= -1
        lF = step * (dynamic_F(n-1) / dynamic_fac(2 * n) - dynamic_G(n-1))
        return lF

# G
def dynamic_G(n):
    global lG
    if n == 1:
        return 1
    else:
        lG = dynamic_F(n-1) + 2 * dynamic_G(n-1)
        return lG
    
rec_times = []
iterat_times = []

def time(func, n):
    return timeit.timeit(lambda: func(n), number=1000)


for n in n1:
    rec_times.append(time(fac_rec, n))
    iterat_times.append(time(fac_iterat, n))

# Табличка
print(f"{'n':<10}{'Рекурсивное время (мс)':<25}{'Итерационное время (мс)':<25}")
for i, n in enumerate(n1):
    print(f"{n:<10}{rec_times[i]:<25}{iterat_times[i]:<25}")

# График
plt.plot(n1, rec_times, label='Рекурсивно')
plt.plot(n1, iterat_times, label='Итерационно')
plt.xlabel('n')
plt.ylabel('Время (мс)')
plt.legend()
plt.title('Сравнение времени вычисления функции факториала')
plt.show()
