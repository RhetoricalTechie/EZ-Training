'''def generate_magic_square(n):
    magic_square = [[0] * n for x in range(n)]
    row, col = 0'''


n = int (input("Enter the order of the magic square that must be odd: "))
if (n%2==0):
    print("the order of the magic square must be odd.")
else:
    magic_square = generate_magic_square(n)
