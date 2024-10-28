import math
import numpy as np
import matplotlib.pyplot as plt

# Fungsi frekuensi resonansi
def f(R, L=0.5, C=10e-6, f0=1000):
    return (1/(2*math.pi)) * math.sqrt(1/(L*C) - (R*2)/(4*L*2)) - f0

# Turunan dari fungsi frekuensi resonansi terhadap R
def df_dR(R, L=0.5, C=10e-6):
    return -(R/(4*math.pi*L)) * math.sqrt(1/(L*C) - (R*2)/(4*L*2))
  
  # Metode Biseksi
def bisection(a, b, tol, max_iter):
    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return None
  # Metode Newton-Raphson
def newton_raphson(x0, tol, max_iter):
    for i in range(max_iter):
        x1 = x0 - f(x0) / df_dR(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

# Parameter
tol = 0.1
max_iter = 100
a = 0
b = 100
x0 = 50

# Hitung akar menggunakan metode biseksi
root_bisection = bisection(a, b, tol, max_iter)

# Visualisasi
R = np.linspace(0, 100, 1000)
f_values = [f(r) for r in R]

plt.plot(R, f_values)
plt.axhline(y=0, color='k', linestyle='--')
plt.xlabel('R')
plt.ylabel('f(R)')
plt.title('Grafik Fungsi f(R)')
plt.grid(True)
plt.show()

# Cetak hasil
print("Akar menggunakan metode biseksi:", root_bisection)
print("Akar menggunakan metode Newton-Raphson:", root_newton)

