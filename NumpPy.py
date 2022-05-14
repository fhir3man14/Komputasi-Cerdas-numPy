#import library
import numpy as np
import matplotlib.pyplot as plt

#Membuat Array Numpy
listku = [1,2,3,4,5]
arrku = np.array([listku])
print(arrku)

#operasi aritmatika
arr_A = np.array([1,2,3,4,5])
arr_B = np.array([2,2,2,2,2])

print("Penjumlahan = ", arr_A + arr_B)
print("Pengurangan = ", arr_A - arr_B)
print("Perkalian = ", arr_A * arr_B)
print("Pembagian = ", arr_A / arr_B)
print("Perpangkatan = ", arr_A ** arr_B)

#operasi matematika
arrku = np.array([1,2,3,4,5])
print("Nilai minimal = ", arrku.min())
print("Nilai maksimal = ", arrku.max())
print("Nilai rata-rata = ", arrku.mean())
print("Total nilai = ", arrku.sum())
print("Standar Deviasi = ", arrku.std())
