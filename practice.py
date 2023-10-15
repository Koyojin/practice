from itertools import combinations
n,m=map(int,input().split())
L=list(map(int,input().split()))
como=list(combinations(L,3))
R=[sum(i) for i in como]
K=[]
for i in R:
    if i<=m:
        K.append(i)
print(max(K))