# [기초-종합] 함께 문제 푸는 날(설명)(py)
day=1
a, b, c = input().split()
a=int(a); b=int(b); c=int(c)
while day%a + day%b + day%c :
    day+=1
print(day)