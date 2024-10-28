import numpy as np

# Definisi matriks koefisien dan vektor konstanta
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]])
b = np.array([5, 3, 4])

# Fungsi eliminasi Gauss
def gauss_elimination(A, b):
    n = len(A)
    for i in range(n):
        # Cari elemen pivot terbesar pada kolom i ke bawah
        max_row = i + np.argmax(abs(A[i:, i]))
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Eliminasi elemen di bawah pivot
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, :] -= factor * A[i, :]
            b[j] -= factor * b[i]
          # Substitusi mundur
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

# Fungsi determinan dengan ekspansi kofaktor
def determinant(A):
    if len(A) == 1:
        return A[0, 0]
    det = 0
    for j in range(len(A)):
        det += (-1)**j * A[0, j] * determinant(np.delete(A, (0, j), axis=(0, 1)))
    return det
  # Fungsi metode Gauss-Jordan
def gauss_jordan(A, b):
    n = len(A)
    for i in range(n):
        # Cari elemen pivot terbesar pada kolom i ke bawah
        max_row = i + np.argmax(abs(A[i:, i]))
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Normalisasi baris
        A[i, :] /= A[i, i]
        b[i] /= A[i, i]

        # Eliminasi elemen di atas dan bawah pivot
        for j in range(n):
            if j != i:
                factor = A[j, i]
                A[j, :] -= factor * A[i, :]
                b[j] -= factor * b[i]
    return b
  # Fungsi invers matriks dengan metode adjoin
def inverse(A):
    det = np.linalg.det(A)
    if det == 0:
        return "Matriks tidak memiliki invers"
    adj = np.linalg.inv(A).T
    return adj / det

# Selesaikan sistem persamaan
x_gauss = gauss_elimination(A.copy(), b.copy())
det_A = determinant(A)
x_gauss_jordan = gauss_jordan(A.copy(), b.copy())
inv_A = inverse(A)
x_inv = np.dot(inv_A, b)

print("Solusi dengan metode Gauss:", x_gauss)
print("Determinan matriks A:", det_A)
print("Solusi dengan metode Gauss-Jordan:", x_gauss_jordan)
print("Invers matriks A:", inv_A)
print("Solusi dengan invers matriks:", x_inv)
