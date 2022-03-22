import numpy as np

# 행렬 A를 출력하는 함수
def pprint(msg, A):
    print("----", msg, "----")
    (n,m) = A.shape 
    for i in range(0, n): 
        line = ""
        for j in range(0, m): 
            line += "{0:.2f}".format(A[i,j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")
    
# 가우스 소거법을 수행하는 함수
def gauss(A):
    (n,m) = A.shape # n * m
    for i in range(0, m-2):
        # 현재 i번째 열의 i번째 행을 제외한 아래 성분을 0으로 만들기
        for k in range(1, n):
            if k > i:
                c = A[k,i]/A[i,i]
                for j in range(i, m):
                    if i == j:
                        A[k,j] = 0
                    else:
                        A[k,j] -= c * A[i,j]
        pprint(str(i+1)+"번째 반복", A) # 중간 과정 출력

   # Ax=b의 해 반환
    x = np.zeros(m-1)
   # 마지막 행부터 계산 
    for i in range(n-1,-1,-1): 
        x[i] = A[i,m-1]
        for j in range(0,m-1):
            if j > i:
                x[i] -= x[j] * A[i,j]
        x[i] /= A[i,i]  
    return x  

# 주어진 연립선형방정식에 대한 첨가행렬
A = np.array([[2., 2., 4., 18.], [1., 3., 2., 13.], [3., 1., 3., 14.]])

pprint("주어진 문제", A) # 첨가행렬 출력
x = gauss(A) # 가우스 소거법 적용

# 출력 생성
(n,m) = A.shape
line = "해:\t"
for i in range(0, m-1):
    line += "{0:.2f}".format(x[i]) + "\t"
print(line)
