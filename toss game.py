str1=input('Enter the string')
iscont=False
head=0
tail=0
for i in range(0,len(str1)):
    if(str1[i:i+3]=='HHH'):
        iscont=True
        head+=1
    elif(str1[i]=='H'):
        head+=1
    else:
        tail+=1
if(iscont):
    print(head*2)
else:
    print((head-tail)*2)
    
        
