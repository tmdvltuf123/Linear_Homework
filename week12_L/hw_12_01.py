import numpy as np

u = np.array([[2], [-5], [-1]])
v = np.array([[3], [2], [-3]])

# .T: 전치, @: 행렬곱, .item(): 숫자 하나 추출
u_dot_v = (u.T @ v).item()
v_dot_u = (v.T @ u).item()

print("u ⋅ v =", u_dot_v)  # -1
print("v ⋅ u =", v_dot_u)  # -1
print("교환법칙 확인:", u_dot_v == v_dot_u)  # True
