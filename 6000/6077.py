#[기초-종합] 짝수 합 구하기(설명)
n=int(input())
sum=0
for i in range(n+1) :
    if i%2==0 : sum+=i
print(sum)