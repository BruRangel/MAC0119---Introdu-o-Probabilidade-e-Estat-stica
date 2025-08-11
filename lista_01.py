import math
import statistics
import numpy as np
import scipy.stats

# Exercício 1
X = [5.8, 1.4, 5.6, 0.0, 5.6, 1.3, 3.5, 6.6, 0.0, 6.3, 0.0, 6.9, 3.4, 4.1, 5.6, 6.7, 0.0, 3.4, 7.2, 7.8,
     2.3, 6.6, 9.4, 7.2, 6.2, 0.0, 0.2, 2.7, 5.7, 0.4, 3.6, 1.1, 6.4, 8.0, 4.1, 7.4, 4.1, 0.1, 0.0, 0.6,
     0.0, 0.3, 5.1, 8.7, 9.9, 7.6, 2.7, 6.2, 5.8, 4.6, 0.2, 4.3, 5.5, 8.1, 3.0, 0.7, 8.4, 9.6, 8.5, 0.0,
     5.0, 6.7, 5.0, 6.6, 5.1, 7.0, 9.3, 5.0, 8.6, 5.3, 9.8, 7.2, 0.8, 0.2, 0.1, 6.8, 0.3, 5.9, 8.5, 5.9,
     2.0]

X.sort()
print(f"X sorted: {X}")

X_sum = sum(X)
X_len = len(X)
print(f"X_sum: {X_sum}")
print(f"X_len: {X_len}")
X_my_mean = X_sum/X_len

# a)
X_mean = statistics.mean(X)
X_median = statistics.median(X)
X_mode = statistics.mode(X)
X_amplitude = abs(max(X) - min(X))
X_quantiles = statistics.quantiles(X)
X_min_value = min(X)
X_max_value = max(X)
X_dm = np.mean([abs(x - X_mean) for x in X])
X_dp = math.sqrt(np.mean([(x - X_mean)**2 for x in X]))

print(f"X_mean: {X_mean}")
print(f"X_median: {X_median}")
print(f"X_mode: {X_mode}")
print(f"X_amplitude: {X_amplitude}")
print(f"X_quantiles: {X_quantiles}")
print(f"X_min_value: {X_min_value}")
print(f"X_max_value: {X_max_value}")
print(f"X_desvio_medio: {X_dm}")
print(f"X_desvio_padrao: {X_dp}")
print(f"X_my_mean: {X_my_mean}")

# b)
qtd_entre_2dp = 0

for x in X:
    if (x >= X_mean - 2*X_dp) and (x <= X_mean + 2*X_dp):
        qtd_entre_2dp += 1

print(f"Quantidade de elementos entre Média - 2DP e Média + 2DP: {qtd_entre_2dp}")
media_menos_2dp = X_mean - X_dp * 2
media_mais_2dp = X_mean + X_dp * 2
print(f"Media menos 2dp: {media_menos_2dp}")
print(f"Media mais 2dp: {media_mais_2dp}")

X_0_3 = np.array([x for x in X if x>= 0 and x < 3])
X_3_5 = np.array([x for x in X if x >= 3 and x < 5])
X_5_7 = np.array([x for x in X if x >= 5 and x < 7])
X_7_10 = np.array([x for x in X if x>= 7 and x < 10])

print(len(X_0_3))
print(len(X_3_5))
print(len(X_5_7))
print(len(X_7_10))

X_K_mean = (1.5 * len(X_0_3) + 4 * len(X_3_5) + 6 * len(X_5_7) + 8.5 * len(X_7_10))/81
print(f"X_K_mean: {X_K_mean}")
