import math
import numpy as np

def mc_loren(num, iter):
    res = 0
    for i in range(1, iter):
        pre=(math.factorial(2 * i) * (num ** i)) / ((1 - 2 * i) * (math.factorial(i) ** 2) * (4 ** i))
        if i % 2 == 0:
            res += pre
        else:
            res -= pre
    return res


class MyNumber(object):
    def __init__(self, zeta):
        """Конструктор принимает zeta, но обьект соответствует числу x=1+zeta."""
        self.zeta=zeta
    def __str__(self):
        """На экран выводится значение x, которое может быть менее точно,
        чем храниемое значение."""
        return "{}".format(self.to_float())
    def from_float(x):
        """Создает число со значением, равным x."""
        return MyNumber(x-1)
    def to_float(self):
        """Преобразует число в формат с плавающей запятой"""
        return self.zeta+1
    def __mul__(self, other):
        """Перезагрузка операции умножения."""
        return MyNumber(self.zeta+other.zeta+self.zeta*other.zeta)
    def sqrt(self):
        if (self.zeta < 1):
            beta = mc_loren(self.zeta, 30)
            return MyNumber(beta)
        else:
            beta = math.sqrt(self.zeta+1)
            return MyNumber.from_float(beta)

def f_sqrt_sqr(x=MyNumber.from_float(np.pi), n=52):
    for k in range(n): x = x.sqrt()
    for k in range(n): x = x*x
    return x

float_num=2.44567
print("Число с плавающей запятой:", float_num)
num=MyNumber.from_float(float_num)
print("Наше представление числа: ", num)
print("Квадрат в арифметике с плавающей запятой:", float_num*float_num)
print("Квадрат в нашем представлении:           ", num*num)
n=52
print("Число до преобразований: ", num)
new_num=f_sqrt_sqr(num)
print("Число после преобразований: ", new_num)
delta = num.to_float() - new_num.to_float()
eps = np.abs(delta) / num.to_float()
print("Разница: ", eps)