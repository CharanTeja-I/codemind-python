r,c=map(int,input().split())
a=[]
s=0
for i in range(r):
    lst = list(map(int, input().split()))
    a.append(lst)
for i in range(r):
    s+=sum(a[i])
print(s)