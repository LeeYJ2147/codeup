a, b, c = input().split()
min = int(a) if int(a)<int(b) else int(b)
print(min if min<int(c) else int(c))