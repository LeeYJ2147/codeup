# [기초-종합] 수 나열하기3(py)
a, r, d, n = map(int, input().split())
for i in range(n-1) :
    a = a*r+d
print(a)