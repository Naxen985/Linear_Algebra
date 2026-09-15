def add_square_matrices(A, B):
# 같은 크기의 두 정방행렬을 더하여 새로운 행렬을 반환한다
  
  n = len(A)

  # 두 행렬의 행 개수 확인
  if n == 0 or len(B) != n:
    raise ValueError("두 행렬은 비어있지 않고 크기가 같아야 합니다.")
  
  # 각 행의 원소 개수가 n개인지 확인: n * n 정방행렬 검사
  if any(len(row) != n for row in A):
    raise ValueError("A는 정방행렬이어야 합니다.")
  
  
  if any(len(row) != n for row in B):
    raise ValueError("B는 A와 같은 크기의 정방행렬이어야 합니다.")

  # 결과를 저장할 n * n 행렬을 0으로 초기화
  C = [[0 for _ in range(n)] for _ in range(n)]

  # 같은 위치의 원소끼리 덧셈
  for i in range(n):      # 행 인덱스
    for j in range(n):    # 열 인덱스
      C[i][j] = A[i][j] + B[i][j]

  return C
  
  # 두 정방행렬의 정의
  A = [
      [1, 2],
      [3, 4]
  ]

  B = [
      [5, 6],
      [7, 8]
  ]

  # 행렬 덧셈
  C = add_square_matrices(A, B)

  # 결과 출력
  print("A + B =")
  for row in C:
    print(row)


# 행렬 곱셈
# A: 4행 3열 행렬
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# B: 3행 2열 행렬
B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# 행렬의 크기
rows_a = len(A)     # A의 행 개수: 4
cols_a = len(A[0])  # A의 열 개수: 3
rows_b = len(B)     # B의 행 개수: 3
cols_b = len(B[0])  # B의 열 개수: 2

# 행렬 곱셈 가능 여부 확인
if cols_a != rows_b:
  raise ValueError("A의 열 개수과 B의 행개수가 같아야 합니다.")

# 결과 행렬 C: 4행 2열, 모든 원소를 0으로 초기화
C = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

# 행렬 곱셈
for i in range(rows_a):
  for j in range(cols_b):
    for k in range(cols_a):
      C[i][j] += A[i][k] * B[k][j]

# 결과 출력
print("A x b =")
for row in C:
  print(row)


# 행렬 trace 구하기 1
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))

print("대각합:", diagonal_sum)


# 행렬 trace 구하기 2
import numpy as np

martix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("대각합:", np.trace(matrix))