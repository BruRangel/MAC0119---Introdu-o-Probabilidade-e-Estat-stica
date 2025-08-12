import math
import statistics
import numpy as np
import pandas as pd
import scipy.stats  

X = [3, 2, 0, 4, 4, 5]
Y = [10, 12, 8, 8, 6, 4]

N = len(X)

X_mean = statistics.mean(X)
Y_mean = statistics.mean(Y)
X_dp = math.sqrt(np.mean([(x - X_mean)**2 for x in X]))
Y_dp = math.sqrt(np.mean([(y - Y_mean)**2 for y in Y]))

# Exibindo resultados:
print(f"X_mean: {X_mean}")
print(f"Y_mean: {Y_mean}")
print(f"X_dp: {X_dp}")
print(f"Y_dp: {Y_dp}")

Z_x = 0
Z_y = 0

sum_of_products = 0

for i in range(N):
    Z_x = (X[i] - X_mean)/X_dp
    Z_y = (Y[i] - Y_mean)/Y_dp
    sum_of_products += Z_x * Z_y

r = sum_of_products/N

print(f"Coeficiente de Correlação de Pearson: {r}")
