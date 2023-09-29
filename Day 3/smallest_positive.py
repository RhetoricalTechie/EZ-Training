array = list(map(int,input().strip().split()))
for i in range(len(array)):
    if i in array:
        continue
    else:
        print("missing number is: ", i)
        break