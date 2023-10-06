a=[2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
b=[0]*len(a)
for i in a:
    if b[i]!=0:
        b[i]=b[i]+1
    else:
        b[i]=1
sum=b[0]
for i in range(len(b)-1):
    b[i]=sum
    sum=sum+b[i+1]
b[i+1]=sum
result=[0]*len(a)
for i in a:
    b[i]=b[i]-1
    result[b[i]]=i
print(result)
