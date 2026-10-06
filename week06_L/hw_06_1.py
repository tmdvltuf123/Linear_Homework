import numpy as np

np.set_printoptions(suppress=True, precision=2)

# 행렬 A
A = np.array([
    [1, 2, 3],
    [2, 5, 3],
    [1, 0, 8]
], dtype=float)

# 단위행렬 l
l = np.eye(3)

# 첨가행렬 [A l l]
Al = np.hstack((A, l))


def show_matrix(operation):
    """행 연산 과정 출력"""
    print(f"\n{operation}")
    print(Al)

print("초기 첨가행렬 [A l l]")
print(Al)

# 1단계: 첫 번째 열에서 1행 아래의 원소를 0으로 만든다.
Al[1] = (-2) * Al[0] + Al[1]
show_matrix("R2 <-- (-2)R1 + R2")

Al[2] = (-1) * Al[0] + Al[2]
show_matrix("R3 <-- (-1)R1 + R3")

# 2단계: 두 번째 열에서 피벗 아래의 원소를 0으로 만든다.
Al[2] = 2 * Al[1] + Al[2]
show_matrix("R3 <-- 2R2 + R3")

# 3단계: 세 번째 피벗을 1로 만든다.
Al[2] = (-1) * Al[2]
show_matrix("R3 <-- (-1)R3")

# 4단계: 세 번째 열에서 피벗 위의 원소를 0으로 만든다.
Al[1] = Al[1] + 3 * Al[2]
show_matrix("R2 <-- R2 + 3R3")

Al[0] = Al[0] - 3 * Al[2]
show_matrix("R1 <-- R1 - 3R3")

# 5단계: 두 번째 열에서 피벗 위의 원소를 0으로 만든다.
Al[0] = Al[0] - 2 * Al[1]
show_matrix("R1 <-- R1 -2R2")

# 오른쪽 부분이 A의 역행렬
A_inverse = Al[:, 3:]

print("\n최종 첨가행렬 [l l A^(-1)]")
print(Al)

print("\nA의 역행렬")
print(A_inverse)

# 역행렬 검산
print("\n검산: A x A^(-1)")
print(A @ A_inverse)


