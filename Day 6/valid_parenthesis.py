'''a = int(input("Enter the number of parenthesis: "))
b = list(map(str,input().strip().split())) [:a]
stack = []
print(b)
if len(b)%2==0:
    for i in b:
        if '''

def is_valid_parentheses(s):
    stack = []

    
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False

    return stack == []


test_string = "([{}])"
result = is_valid_parentheses(test_string)

if result:
    print(f'The string "{test_string}" has valid parentheses.')
else:
    print(f'The string "{test_string}" does not have valid parentheses.')


pre_defined= [  "(","[","{","}","]",")"  ]

inp= int(input("Enter number of combinations: "))

