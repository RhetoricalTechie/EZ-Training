arr=[1,5,1,2,3,2,3]
num=0
for i in arr:
    #XOR operation on all elements will eliminate all duplicates
    num=num^i
print("Number that occurs only once is:",num)