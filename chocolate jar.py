N=int(input())
chocolates=list(map(int, input().strip().split()))
total=0
for jar in chocolates:
    if jar%3!=0:
        total+=jar
    else:
        total+=jar
print(total)
