l_range = int(input("Enter the lower range: "))
u_range = int(input("Enter the upper range: "))
size = int(input("Enter size of array: "))
array=[]
elements = []
even = []
for i in range(size):
    enter=int(input("Enter elements: "))
    elements.append(enter)
    print(elements)
for i in elements:
    if i%2==0:
        even.append(i)
print("even numbers are ", even)
power=[]
for i in even:
    for j in i:
        if i==2**j;
        power.append(i)
print("power numbers are", power)
    

#for size in range elements:
 #   if elements[i] >=l_range and elements[i] <=u_range:
  #      array.append(elements)
   #     print(array)