import math
import statistics
import numpy as np
import pandas as pd
import scipy.stats  

# Exercício 1
X = [5.8, 1.4, 5.6, 0.0, 5.6, 1.3, 3.5, 6.6, 0.0, 6.3, 0.0, 6.9, 3.4, 4.1, 5.6, 6.7, 0.0, 3.4, 7.2, 7.8,
     2.3, 6.6, 9.4, 7.2, 6.2, 0.0, 0.2, 2.7, 5.7, 0.4, 3.6, 1.1, 6.4, 8.0, 4.1, 7.4, 4.1, 0.1, 0.0, 0.6,
     0.0, 0.3, 5.1, 8.7, 9.9, 7.6, 2.7, 6.2, 5.8, 4.6, 0.2, 4.3, 5.5, 8.1, 3.0, 0.7, 8.4, 9.6, 8.5, 0.0,
     5.0, 6.7, 5.0, 6.6, 5.1, 7.0, 9.3, 5.0, 8.6, 5.3, 9.8, 7.2, 0.8, 0.2, 0.1, 6.8, 0.3, 5.9, 8.5, 5.9,
     2.0]

X.sort()
print(f"X sorted: {X}")
N = len(X)

# a)
# Média aritmética simples
X_mean = statistics.mean(X)
# Mediana
X_median = statistics.median(X)
# Moda
X_mode = statistics.mode(X)
# Amplitude
X_amplitude = abs(max(X) - min(X))
# Quartis
X_quantiles = statistics.quantiles(X) # O cálculo foi verificado observando os valores ordenados
# Valor mínimo
X_min_value = min(X)
# Valor máximo
X_max_value = max(X)
# Cálculo do desvio médio:
X_dm = np.mean([abs(x - X_mean) for x in X])
# Cálculo do desvio padrão:
X_dp = math.sqrt(np.mean([(x - X_mean)**2 for x in X]))

# Exibindo Resultados:
print(f"X_mean: {X_mean}")
print(f"X_median: {X_median}")
print(f"X_mode: {X_mode}")
print(f"X_amplitude: {X_amplitude}")
print(f"X_quantiles: {X_quantiles}")
print(f"X_min_value: {X_min_value}")
print(f"X_max_value: {X_max_value}")
print(f"X_desvio_medio: {X_dm}")
print(f"X_desvio_padrao: {X_dp}")

# b)
qtd_entre_2dp = 0
# Cálculo de quantos elementos estão no intervalo média +- 2DP
for x in X:
    if (x >= X_mean - 2*X_dp) and (x <= X_mean + 2*X_dp):
        qtd_entre_2dp += 1

print(f"Quantidade de elementos entre Média - 2DP e Média + 2DP: {qtd_entre_2dp}")

media_menos_2dp = X_mean - X_dp * 2
media_mais_2dp = X_mean + X_dp * 2
print(f"Media menos 2dp: {media_menos_2dp}")
print(f"Media mais 2dp: {media_mais_2dp}")

# c)
# Criando as classes conforme especificadas no exercício
X_0_3 = np.array([x for x in X if x>= 0 and x < 3])
X_3_5 = np.array([x for x in X if x >= 3 and x < 5])
X_5_7 = np.array([x for x in X if x >= 5 and x < 7])
X_7_10 = np.array([x for x in X if x>= 7 and x < 10])

classes_arrays = [X_0_3, X_3_5, X_5_7, X_7_10]
class_labels = ["0 ⊢ 3", "3 ⊢ 5", "5 ⊢ 7", "7 ⊢ 10"]
pontos_medios = [1.5, 4.0, 6.0, 8.5]

# Amplitude de cada classe
print(f"len(X_0_3): {len(X_0_3)}")
print(f"len(X_3_5): {len(X_3_5)}")
print(f"len(X_5_7): {len(X_5_7)}")
print(f"len(X_7_10): {len(X_7_10)}")

# Média aritmética dos dados agrupados
X_K_mean = (1.5 * len(X_0_3) + 4 * len(X_3_5) + 6 * len(X_5_7) + 8.5 * len(X_7_10))/len(X)
print(f"X_K_mean: {X_K_mean}")

# É observável que a classe mediana é 5 -> 7
# É observável que as classes modais são 0 -> 3 e 5 -> 7

# Cálculo do Desvio Médio dos dados agrupados
X_K_dm = (abs(1.5-X_K_mean)*len(X_0_3) +
          abs(4-X_K_mean)*len(X_3_5) +
          abs(6-X_K_mean)*len(X_5_7) +
          abs(8.5-X_K_mean)*len(X_7_10))/N

print(f"X_K_dm: {X_K_dm}")

# Cálculo do Desvio Padrão dos dados agrupados
X_K_dp = math.sqrt((((1.5-X_K_mean)**2)*len(X_0_3) +
          ((4-X_K_mean)**2)*len(X_3_5) +
          ((6-X_K_mean)**2)*len(X_5_7) +
          ((8.5-X_K_mean)**2)*len(X_7_10))/N)

print(f"X_K_dp: {X_K_dp}")

# e)
# Seja Y o conjunto de dados tal que cada aluno recebeu 1 ponto a mais na nota final
Y_mean = X_mean + 1
Y_mode = X_mode + 1
Y_median = X_median + 1
Y_quantiles = [q + 1 for q in X_quantiles]
Y_dm = X_dm
Y_dp = X_dp
Y_max_value = X_max_value
Y_min_value = X_min_value
Y_amplitude = X_amplitude

# Exibindo os Resultados
print("--- Medidas de Posição (aumentam em 1) ---")
print(f"Y Média: {Y_mean:.4f}")
print(f"Y Mediana: {Y_median}")
print(f"Y Moda: {Y_mode}")
print(f"Y Quartis: {Y_quantiles}")
print(f"Y Valor Mínimo: {Y_min_value}")
print(f"Y Valor Máximo: {Y_max_value}\n")

print("--- Medidas de Dispersão (não se alteram) ---")
print(f"Y Amplitude: {Y_amplitude}")
print(f"Y Desvio Médio: {Y_dm:.4f}")
print(f"Y Desvio Padrão: {Y_dp:.4f}")
