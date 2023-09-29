#Find XOR numbers for the given range
ll=int(input("Enter the lower limit: "))
ul=int(input("Enter the upper limit: "))
xor=0
for i in range(ll,ul):
    xor = (xor ^ i) ^ (xor ^ (ul-ll))
print(xor)
