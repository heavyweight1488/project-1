def f(x):
    """Возведение параметра в квадрат"""
    return x**2
result = f(2)
print('task1:' + str(result))


def a(string):
    """Возврат параметра"""
    return string
result = "string"
print('task2:' + str(result))


def obligatory_optional(x, y, z, q = 1, w = 2):
    """ Функция принимает три обязательных и два необзятальных значения"""
    return None

print('task3: ' + str (obligatory_optional(4, 6, 8)))



def ReturnTheResultOfDivisionBy2(x):
    return x / 2


def ReturnTheResultOfMultiplyingBy4(y):
    return y * 4
"""Программа с двумя параметрами"""

def CallTheFirstFunction(x):
    result2 = ReturnTheResultOfDivisionBy2(x)
    result4 = ReturnTheResultOfMultiplyingBy4(result2)
    return result4
print('task4:' + str (CallTheFirstFunction(4)))


def conversion(string):
    """Преобразовавания строки в тип даннх float"""
    try:
        return float(string)
    except(ZeroDivisionError, ValueError):
        print('текст не является числом')
        
        
print('task 5:' + str (conversion("30.50")))

import modulenumber
print(modulenumber.cubed(5))
import modulenumber
print(modulenumber.box(12))
import modulenumber
print(modulenumber.privet())
from modulenumber import box
print(box(12))
from modulenumber import bonus
print(bonus(4))