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
print("Погрешность прямого суммирования:", l.relative_error(exact_sum_for_sin, direct_sum_for_sin))

"""Task 4"""

sin_x=np.array(sin_x)
sorted_sin_x=sin_x[np.argsort(sin_x)]
exact_sum_for_sin=exact_sin_sum(k)
direct_sum_for_sin=l.direct_sum(sorted_sin_x)
Kahan_sum_for_sin=l.Kahan_sum(sorted_sin_x)
print("Погрешность суммирования по возрастанию:", l.relative_error(exact_sum_for_sin, direct_sum_for_sin))
print("Погрешность суммирования по Кэхэну:", l.relative_error(exact_sum_for_sin, Kahan_sum_for_sin))

sorted_sin_x=sin_x[np.argsort(np.absolute(sin_x))]
exact_sum_for_sin=exact_sin_sum(k)
direct_sum_for_sin=l.direct_sum(sorted_sin_x)
Kahan_sum_for_sin=l.Kahan_sum(sorted_sin_x)
print("Погрешность суммирования по возрастанию абсолютной величины:", l.relative_error(exact_sum_for_sin, direct_sum_for_sin))
print("Погрешность суммирования по Кэхэну абсолютной величины:", l.relative_error(exact_sum_for_sin, Kahan_sum_for_sin))


