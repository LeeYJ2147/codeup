#[기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2
n=int(input())
sum=0
for i in range(n+1) :
    if i%2==0 : sum+=i
print(sum)