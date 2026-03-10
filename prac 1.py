def generate_magic_square(n):
    square = [[0]*n for _ in range(n)]

    i = 0
    j = n // 2

    for num in range(1, n*n + 1):
        square[i][j] = num
        new_i = (i - 1) % n
        new_j = (j + 1) % n

        if square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i = new_i
            j = new_j

    return square


def rotate_90(square):
    n = len(square)
    return [[square[n - j - 1][i] for j in range(n)] for i in range(n)]


def reflect(square):
    return [row[::-1] for row in square]


def print_square(square, title):
    print(f"\n{title}")
    for row in square:
        for val in row:
            print(f"{val:3}", end=" ")
        print()


n = int(input("Enter odd size of magic square: "))

if n % 2 == 0:
    print("Error: Only odd numbers are allowed")
else:
    base = generate_magic_square(n)

    print_square(base, "Solution 1 ")

    r90 = rotate_90(base)
    print_square(r90, "Solution 2 ")

    r180 = rotate_90(r90)
    print_square(r180, "Solution 3 ")

    r270 = rotate_90(r180)
    print_square(r270, "Solution 4 ")

    refl = reflect(base)
    print_square(refl, "Solution 5 ")