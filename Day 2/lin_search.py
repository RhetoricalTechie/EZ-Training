def lin_search(a):
    for i in range(len(a)):
        if a[i]==key:
            print(i)
            return True
    return False

size=int(input("Enter the size of list: "))
a=list(map(int,input().strip().split()))[:size]
print(a)
key=int(input("Enter the key element to search: "))
b=lin_search(a)
print(b)