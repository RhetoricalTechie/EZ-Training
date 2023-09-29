#Print XOR of all numbers Big O(n)
'''n=int(input("enter the number:"))
xor=0
for i in range(1,n+1):
    xor = xor ^ i
print(xor)'''

#Big O(1)
n =int(input("Enter the number:"))
if n%4==0:
    print("XOR value is:",n)
elif n%4==1:
    print("XOR value is:",1)
elif n%4==2:
    print("XOR value is:",n+1)
elif n%4==3:
    print("XOR value is:",0)
else:
    print("Error")