a=int(input())
b=int(input())
c=int(input())
n = list(str(a*b*c))
m = [0 for _ in range(0, 10)]
for i in n:
    m[int(i)] += 1
for j in m:
    print(j)