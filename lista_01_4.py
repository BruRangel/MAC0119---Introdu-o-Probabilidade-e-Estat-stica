import math
import statistics
import numpy as np
import pandas as pd
import scipy.stats

Homem = [15, 10, 8, 10, 15, 5, 15, 0, 2, 20]
Mulher = [3, 12, 5, 10, 8, 7, 10, 5, 10, 25]
Casal = [(h + m) for h, m in zip(Homem, Mulher)]
N = len(Casal)

Homem_mean = statistics.mean(Homem)
Mulher_mean = statistics.mean(Mulher)
Casal_mean = statistics.mean(Casal)
# a)
Homem_dp = math.sqrt(np.mean([(h - Homem_mean)**2 for h in Homem]))
Mulher_dp = math.sqrt(np.mean([(m - Mulher_mean)**2 for m in Mulher]))
# b)
Casal_dp = math.sqrt(np.mean([(c - Casal_mean)**2 for c in Casal]))
Casal_var = Casal_dp**2

# c)
Z_h = 0
Z_m = 0

sum_of_products = 0

for i in range(N):
    Z_h = (Homem[i] - Homem_mean)/Homem_dp
    Z_m = (Mulher[i] - Mulher_mean)/Mulher_dp
    sum_of_products += Z_h * Z_m

r = sum_of_products/N

print(f"Coeficiente de Correlação de Pearson: {r}")

# d)
new_Homem = [0.95 * h for h in Homem]
new_Mulher = [1 + m for m in Mulher]

new_Homem_mean = statistics.mean(new_Homem)
new_Mulher_mean = statistics.mean(new_Mulher)
new_Homem_dp = math.sqrt(np.mean([(h - new_Homem_mean)**2 for h in new_Homem]))
new_Mulher_dp = math.sqrt(np.mean([(m - new_Mulher_mean)**2 for m in new_Mulher]))

n_Z_h = 0
n_Z_m = 0

n_sum_of_products = 0

for i in range(N):
    Z_h = (new_Homem[i] - new_Homem_mean)/new_Homem_dp
    Z_m = (new_Mulher[i] - new_Mulher_mean)/new_Mulher_dp
    n_sum_of_products += n_Z_h * n_Z_m

n_r = sum_of_products/N

print(f"Novo coeficiente de Correlação de Pearson: {n_r}")

# Como pode ser observado, a aplicação de transformações lineares (com escalares não nulos)
# aos elementos de um conjunto de observações não muda o coeficiente de correlação.
