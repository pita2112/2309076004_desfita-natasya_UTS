import numpy as np
import matplotlib.pyplot as plt

# Fungsi resistansi
def R(T):
    return 5000 * np.exp(3500 * (1/T - 1/298))

# Turunan analitik
def dR_dT(T):
    return -3500/T**2 * R(T)

# Turunan numerik: selisih maju, mundur, tengah
def dR_dT_maju(T, h):
    return (R(T+h) - R(T)) / h

def dR_dT_mundur(T, h):
    return (R(T) - R(T-h)) / h

def dR_dT_tengah(T, h):
    return (R(T+h) - R(T-h)) / (2*h)

# Ekstrapolasi Richardson
def richardson(f, T, h):
    f1 = f(T, h)
    f2 = f(T, h/2)
    return (4*f2 - f1) / 3
  # Rentang suhu dan langkah
T = np.arange(250, 351, 10)
h = 1e-6

# Hitung nilai dR/dT untuk setiap metode
dR_dT_num_maju = dR_dT_maju(T, h)
dR_dT_num_mundur = dR_dT_mundur(T, h)
dR_dT_num_tengah = dR_dT_tengah(T, h)
dR_dT_analitik = dR_dT(T)
dR_dT_richardson = richardson(dR_dT_tengah, T, h)

# Hitung error relatif
error_maju = np.abs((dR_dT_num_maju - dR_dT_analitik) / dR_dT_analitik)
error_mundur = np.abs((dR_dT_num_mundur - dR_dT_analitik) / dR_dT_analitik)
error_tengah = np.abs((dR_dT_num_tengah - dR_dT_analitik) / dR_dT_analitik)
error_richardson = np.abs((dR_dT_richardson - dR_dT_analitik) / dR_dT_analitik)
# Plot hasil
plt.plot(T, dR_dT_analitik, label='Analitik')
plt.plot(T, dR_dT_num_maju, label='Selisih Maju')
plt.plot(T, dR_dT_num_mundur, label='Selisih Mundur')
plt.plot(T, dR_dT_num_tengah, label='Selisih Tengah')
plt.plot(T, dR_dT_richardson, label='Richardson')
plt.xlabel('Suhu (K)')
plt.ylabel('dR/dT')
plt.legend()
plt.show()

# Plot error relatif
plt.plot(T, error_maju, label='Selisih Maju')
plt.plot(T, error_mundur, label='Selisih Mundur')
plt.plot(T, error_tengah, label='Selisih Tengah')
plt.plot(T, error_richardson, label='Richardson')
plt.xlabel('Suhu (K)')
plt.ylabel('Error Relatif')
plt.legend()
plt.show()
