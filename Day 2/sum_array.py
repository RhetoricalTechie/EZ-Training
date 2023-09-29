def sum(a):
    add=0
    for i in a:
        add=add+i
    return(add)

limit=int(input())
a = list(map(int,input().strip().split())) [:limit]
b=sum(a)
print(b)