import math
import statistics
import numpy as np
import pandas as pd
import scipy.stats

ANO = [2005, 2006, 2007, 2008, 2009]
X = [7.3, 7.5, 8.1, 8.6, 9.0]
Y = [23.6, 23.6, 25.5, 27.7, 29.4]
X_mean = 8.10
Y_mean = 25.96
X_dp = 0.64
Y_dp = 2.29
N = len(ANO)

Z_x = 0
Z_y = 0

sum_of_products = 0

for i in range(N):
    Z_x = (X[i] - X_mean)/X_dp
    Z_y = (Y[i] - Y_mean)/Y_dp
    sum_of_products += Z_x * Z_y

r = sum_of_products/N

print(f"Coeficiente de Correlação de Pearson: {r}")

# Podemos afirmar que existe uma forte correlação linear entre as variáveis, no entanto
# não podemos afirmar uma relação causal entre as mesmas. É provavel que tal correlação seja devida
# a outras variáveis, por exemplo, o tempo, e outras mais que não temos acesso nesses dados.
