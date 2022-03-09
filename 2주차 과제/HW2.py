number=list(map(int,input("정수 5개를 입력하세요: ").split()))

print("총합: ",sum(number))
print("가장 작은 값: ",min(number))
print("가장 큰 값: ",max(number))
print("평균: ",sum(number)/len(number))
