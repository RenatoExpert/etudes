#!/usr/bin/env python
# coding: utf-8

# # Fourier Series
# This is a demonstration about fourier series.
# We are going to test in the following steps:
# 1. Define generic formulas
# 2. Define a periodic (original) function: of(x)
# 3. Calculate the fourier series version of that function: ff(x)
# 4. Choose a range of values to test, and process these values on both functions
# 5. Plot them to compare results

# In[1]:


# 0. Install needed libraries

get_ipython().run_line_magic('pip', 'install matplotlib numpy --quiet')


# In[2]:


# 1. Define Generic Formulas
import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin

integral_factor = 10000
N_factor = 10000

def integral (expression, xo, xf):
    delta = xf - xo
    dx = delta / integral_factor
    acc = 0
    for i in range(0, integral_factor + 1):
        x = xo + (i * dx)
        acc += expression(x) * dx
    return acc

def test_integral ():
    acceptable_error = 1
    expr = lambda x: x
    result = integral(expr, 0, 100)
    expected = 5000
    error = abs(expected - result)
    assert error < acceptable_error, f"Integral test not passed\n\texpected: {expected}\n\tresult: {result}"

test_integral()

def k (n, P, x):
    result = 2 * pi * x * n / P
    return result

def factor_n (p1, p2, of, n, cos_or_sin):
    P = p2 - p1
    integral_expression = lambda x: of(x) * cos_or_sin(k(n, P, x))
    integral_result = integral(integral_expression, p1, p2)
    multiplier = 2 / P
    result = multiplier * integral_result
    return result

def get_an (p1, p2, of, n):
    return factor_n (p1, p2, of, n, cos)

def get_a_zero (p1, p2, f):
    integral_expression = lambda x: f(x)
    integral_result = integral(integral_expression, p1, p2)
    P = p2 - p1
    multiplier = 1 / P
    result = multiplier * integral_result
    print(f" a0 -> multiplier: {multiplier} , integral: {integral_result} , P: {P}")
    return result 

def get_bn (p1, p2, of, n):
    return factor_n (p1, p2, of, n, sin)

def get_coeficients (f, p1, p2):
    a_zero = get_a_zero(p1, p2, f)
    an = []
    bn = []
    for N in range(1, N_factor):
        an.append(get_an(p1, p2, f, N))
        bn.append(get_bn(p1, p2, f, N))
    return ( a_zero, an, bn )

def fourier_series (x, a0, an, bn, P):
    total = a0
    for N in range(0, N_factor - 1):
        angle = k(N + 1, P, x)
        a_part = an[N] * cos(angle)
        b_part = bn[N] * sin(angle)
        partial_sum = a_part + b_part
        total += partial_sum
    return total

def convert_to_periodic (x, p1, p2):
    P = p2 - p1
    x_periodic = p1 + ((x - p1) % P)
    return x_periodic


# In[ ]:


p1 = 0
p2 = 3
P = p2 - p1

def myfunction (x):
    px = convert_to_periodic(x, p1, p2)
    #return (3 * (px ** 3)) - (px ** 2 * 3) + 7 + sin(px)
    #return 5 if x > 2 else 10 * x ** 2
    return x**2

( a0, an, bn ) = get_coeficients(myfunction, p1, p2)


# In[ ]:


x_range = [ x / 10 for x in range(0, 1000) ]
y_range = [ myfunction(x) for x in x_range ]
f_range = [ fourier_series (x, a0, an, bn, P) for x in x_range ]


# In[ ]:


plt.plot(x_range, y_range, label="f(x)")
plt.plot(x_range, f_range, label="fourier")
plt.show()


# In[ ]:




