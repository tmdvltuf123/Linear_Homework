import numpy as np

u = np.array([2, -5, -1])
v = np.array([-7, -4, 6])

# (1) 내적
dot_product = np.dot(u, v)

# (2) 길이의 제곱 
squared_norm_u = np.dot(u, u)

# (3) 거리의 제곱
difference = u - v
squared_distance = np.dot(difference, difference)

print("u ⋅ v =", dot_product )
print("||u||^2 =", squared_norm_u)
print("||u-v||^2 =", squared_distance)

