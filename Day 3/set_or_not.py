# For the given number n, check the K-th bit is a set or not
# set = 1 & not set = 0
n =10 
k = 2
# Formula = n&(1<<k-1)
result = n&(1<<(k-1))

if result == 0:
    print("The number is a SET")
    
else:
    print("The number is NOT SET")
