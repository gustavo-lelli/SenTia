import numpy as np

d = int(input())

# Leitura das bases
B1 = np.array([list(map(float, input().split())) for _ in range(d)])
B2 = np.array([list(map(float, input().split())) for _ in range(d)])

# Leitura do vetor v na base B1
v_B1 = np.array(list(map(float, input().split())))

# Cálculo da matriz de transformação de B1 para B2
B1_inv = np.linalg.inv(B1)
T = np.dot(B2, B1_inv)

# Cálculo da nova representação de v na base B2[^1^][1]
v_B2 = np.dot(T, v_B1)

print(" ".join(f"{coord:.4f}" for coord in v_B2))
