import numpy as np

A = np.array([
    [2,  1],
    [2, -1],
    [1, -2],
], dtype=float)

b = np.array([3, 1, -1], dtype=float)

solution, residuals, rnak, singular_values = np.linalg.lstsq(
    A, b, rcond=None
)

x1, x2 = solution

print(f"x1 = {x1:.6f}")
print(f"x2 = {x2:.6f}")

print("A @ solution =", A @ solution)
print("b =", b)

if np.allclose(A @ solution, b):
    print("공통해가 존재합니다.")
    print(f"공통해: ({x1:.0f}, {x2:.0f})")
else:
    print("세 방정식을 동시에 만족하는 정확한 공통해가 없습니다.")