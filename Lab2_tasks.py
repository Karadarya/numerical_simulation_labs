import numpy as np
import lab2 as l

"""Task 3"""

k=10
sin_x=[np.sin(i) for i in range(1, k+1)]

def exact_sin_sum(k):
    return 1.0/2 * (np.sin(k) - np.cos(k)/np.tan(1.0/2) + 1/np.tan(1.0/2))

exact_sum_for_sin=exact_sin_sum(k)
#print(exact_sum_for_sin)
direct_sum_for_sin=l.direct_sum(sin_x)
#print(direct_sum_for_sin)
print("Задание 3")
print("Погрешность прямого суммирования:", l.relative_error(exact_sum_for_sin, direct_sum_for_sin))

"""Task 4"""

sin_x=np.array(sin_x)
sorted_sin_x=sin_x[np.argsort(sin_x)]
exact_sum_for_sin=exact_sin_sum(k)
direct_sum_for_sin=l.direct_sum(sorted_sin_x)
Kahan_sum_for_sin=l.Kahan_sum(sorted_sin_x)
print("\nЗадание 4")
print("Погрешность суммирования по возрастанию:", l.relative_error(exact_sum_for_sin, direct_sum_for_sin))
print("Погрешность суммирования по Кэхэну:", l.relative_error(exact_sum_for_sin, Kahan_sum_for_sin))

sorted_sin_x=sin_x[np.argsort(np.absolute(sin_x))]
exact_sum_for_sin=exact_sin_sum(k)
direct_sum_for_sin=l.direct_sum(sorted_sin_x)
Kahan_sum_for_sin=l.Kahan_sum(sorted_sin_x)
print("Погрешность суммирования по возрастанию абсолютной величины:", l.relative_error(exact_sum_for_sin, direct_sum_for_sin))
print("Погрешность суммирования по Кэхэну абсолютной величины:", l.relative_error(exact_sum_for_sin, Kahan_sum_for_sin))


"""Task 6"""
def kahan_mean(x):
    return l.Kahan_sum(x) / len(x)

def oneline_first(x):
    n=1
    sum=x[0]
    e=0
    for i in range(1, len(x)-1):
        n+=1
        old_sum=sum
        if (n>1): old_a=sum/(n-1)
        sum=old_sum+x[i]
        aver=sum/n
        delta=old_a-aver
        e=e+(x[i]-old_a)**2+delta
    n += 1
    old_a = sum / (n - 1)
    extra=((x[n-1] - old_a)**2)/n
    print("n=", n)
    d=e/n+extra
    return d

"""def oneline_first_var(x):
    m=x[0]
    cur_aver=m
    sum=x[0]
    m2=0
    for n in range (1, len(x)) :
        #old_m=m
        old_aver=cur_aver
        sum=sum+x[n]
        cur_aver=sum/(n+1)
        delta=cur_aver-old_aver
        m=(m*(n)+x[n])/(n+1)
        #delta_m=m-old_m
        #res_m=m-delta_m
        m2=(m2*(n)+((x[n]-(m-delta)))**2)/(n+1)
    return m2"""


mean=1e6 # среднее
delta=1e-5 # величина отклонения от среднего

def samples(N_over_two):
    """Генерирует выборку из 2*N_over_two значений с данным средним и среднеквадратическим
    отклонением."""
    x=np.full((2*N_over_two,), mean, dtype=np.double)
    x[:N_over_two]+=delta
    x[N_over_two:]-=delta
    return np.random.permutation(x)

x = samples(1000000)

print("\nЗадание 6")
print("Дисперсия близкая к машинной точности, первая оценка дисперсии, однопроходная первая оценка дисперсии:")
print(l.exact_variance(delta), l.direct_first_var(x), oneline_first(x))
print()
print("Размер выборки:\t\t", len(x))
print("Среднее значение:\t", l.exact_mean(mean))
print("Оценка дисперсии:\t", l.exact_variance(delta))
print()
print("Ошибка среднего для встроенной функции:\t\t", l.relative_error(l.exact_mean(mean), np.mean(x)))
print("Ошибка дисперсии для встроенной функции:\t", l.relative_error(l.exact_variance(delta), np.var(x)))
print()
print("Ошибка среднего для последовательного суммирования:", l.relative_error(l.exact_mean(mean), l.direct_mean(x)))
print()
print("Ошибка первой оценки дисперсии для последовательного суммирования:\t",
l.relative_error(l.exact_variance(delta), l.direct_first_var(x)))

print("Ошибка моей оценки дисперсии для последовательного суммирования:\t",
l.relative_error(l.exact_variance(delta), oneline_first(x)))

