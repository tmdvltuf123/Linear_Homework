from fractions import Fraction


def print_augmented(title, matrix):
    """첨가행렬 [A | |]를 출력하는 함수"""
    print(f"\n{title}")

    for row in matrix:
        left = "  ".join(f"{str(x):>4}" for x in row[:2])
        right = "  ".join(f"{str(x):>4}" for x in row[2:])
        print(f"[ {left} | {right} ]")


# 행렬 A 와 단위 행렬 |로 첨가행렬 구성
augmented = [
    [Fraction(3), Fraction(4), Fraction(1), Fraction(0)],
    [Fraction(2), Fraction(3), Fraction(0), Fraction(1)]
]

print_augmented("초기 첨가행렬 [A | |]", augmented)

# 1단계: R1을 3으로 나눔
# (1/3)R1 --> R1
augmented[0] = [
    value / 3 for value in augmented[0]
]

print_augmented("1단계: (1/3)R1 --> R1", augmented)

# 2단계: 첫 번쨰 열의 2를 0으로 만듦
# R2 - 2R1 --> R2
augmented[1] = [
    augmented[1][j] - 2 * augmented[0][j]
    for j in range(4)
]

print_augmented("2단계: R2 - 2R1 --> R2", augmented)

# 3단계: 두 번쨰 피벗을 1로 만듦
# 3R2 --> R2
augmented[1] = [
    3 * value for value in augmented[1]
]

print_augmented("3단계: 3R2 --> R2", augmented)

# 4단계: 첫 번쨰 행의 4/3 0으로 만듦
# R1 - (4/3)R2 --> R1
augmented[0] = [
    augmented[0][j] - Fraction(4, 3) * augmented[1][j]
    for j in range(4)
]

print_augmented("4단계: R1 - (4/3)R2 --> R1", augmented)

# 오른쪽 부분이 역행렬
A_inverse = [
    row[2:] for row in augmented
]

print("\nA의 역행렬:")
for row in A_inverse:
    print([str(value) for value in row])