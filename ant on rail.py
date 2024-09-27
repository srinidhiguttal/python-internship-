def count_return_to_origin(N,A):
 position=0
 count=0
 for i in range(N):
 position+=A[i]
 if position==0:
 count+=1
 return count
N=int(input())
A=list(map(int,input().split()))
print(count_return_to_origin(N,A))
