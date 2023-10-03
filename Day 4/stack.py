from collections import deque
l = deque()
n = int(input("Enter number of elements: "))
for i in range(n):
    l.append(int(input("enter an element: ")))
print(l)
for i in range(n):
    print(l.pop(0))

print(l)