import numpy as np
def relative_error(x0, x): return np.abs(x0-x)/np.abs(x0)
eps=np.finfo(np.double).eps
print("Машинная точность:",eps)

def f_div_mult(x, d=np.pi, n=52):
    for k in range(n): x=x/d
    for k in range(n): x=x*d
    return x

x0=np.logspace(-4,4,100,dtype=np.double)
x=f_div_mult(x0)
err=relative_error(x0, x)
print("Ошибки",err[:4],"...")

def f_sqrt_sqr(x, n=52):
    for k in range(n): x=np.sqrt(x)
    for k in range(n): x=x*x
    return x

x=f_sqrt_sqr(x0)
err=relative_error(x0, x)
print("Ошибки",err[:4],"...")