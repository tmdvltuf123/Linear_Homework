
import numpy as np


A = np.array([
    [2, 3],
    [3, -6]
], dtype=float)

# 특성다항식 계산
coefficients = np.poly(A)

print("===== 실습 7-1 =====")
print("ans =")
print("  ".join(f"{value:5.0f}" for value in coefficients))

# 고유값 계산
eigenvalues = np.linalg.eigvals(A)

# 고유값을 오름차순으로 정렬
eigenvalues = np.sort(eigenvalues)

print("\nans =")
for value in eigenvalues:
    print(f"{value:.0f}")




A = np.array([
    [3, 2],
    [3, -2]
], dtype=float)

# 고유값과 고유벡터 계산
eigenvalues, X = np.linalg.eig(A)

# 고유값을 내림차순으로 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

# 고유값을 대각행렬로 변환
lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

print("\n===== 실습 7-2 =====")
print("X =")
print(X)

print("\n#lambda =")
print(lamda)






A = np.array([
    [3, -1, -1],
    [-12, 0, 5],
    [4, -2, -1]
], dtype=float)

# 고유값과 고유벡터 계산
eigenvalues, X = np.linalg.eig(A)

# MATLAB 화면처럼 고유값을 2, 1, -1 순서로 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

# 고유값을 대각행렬로 변환
lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

print("\n===== 실습 7-3 =====")
print("X =")
print(X)
print("\n#lambda =")
print(lamda)




# (1) 상부삼각행렬 A
A = np.array([
    [0, 0, 0],
    [0, 2, 5],
    [0, 0, -1]
], dtype=float)

# A의 고유값 계산
eigenvalues_A = np.linalg.eigvals(A)

print("\n===== 실습 7-4  =====")
print("ans =")
for value in eigenvalues_A:
    print(f"{value:.0f}")


# (2) 하부삼각행렬 B
B = np.array([
    [4, 0, 0],
    [0, 0, 0],
    [1, 0, -3]
], dtype=float)

# B의 고유값 계산
eigenvalues_B = np.linalg.eigvals(B)

print("\n\nans =")
for value in eigenvalues_B:
    print(f"{value:.0f}")
