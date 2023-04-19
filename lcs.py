# Tyler Eccles
# The University of Southern Mississippi, CSC413, Bo Li
# A program that calculates the LCS of x and y.
# Based on the pseudocode from the CLRS textbook, 4th edition.
# Pg. 397 of the hard-copy.
# includes output of sets from the textbook examples and exercise 14.4-1.

def print_lcs_matrix(b, c, x, y):
    m = len(x)
    n = len(y)
    print("   ", end="")
    for i in range(0, n):
        print("  " + str(y[i]), end="")
    print()

    print(" ", end="")
    for i in range(0, n+1):
        print(" 00", end="")
    print()

    for i in range(0, m):
        print(str(x[i]) + " 00", end=" ")
        for j in range(0, n):
            print(str(b[i][j]) + str(c[i][j]), end=" ")
        print("\n", end="")


def fill_array(m, n):
    arr = []
    for i in range(0, m):
        arr.append([])
        for j in range(0, n):
            arr[i].append(0)
    return arr


def lcs_len(x, y, m, n):
    b = fill_array(m, n)
    c = fill_array(m+1, n+1)
    for i in range(0, m):
        for j in range(0, n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "↖"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "←"
    return b, c


def print_lcs(b, x, i, j):
    if i == -1 or j == -1:
        return # the lcs has length 0
    if b[i][j] == "↖":
        print_lcs(b, x, i-1, j-1)
        print(x[i], end=" ")
    elif b[i][j] == "↑":
        print_lcs(b, x, i-1, j)
    else:
        print_lcs(b, x, i, j-1)


def get_lcs(x, y):
    b, c = lcs_len(x, y, len(x), len(y))
    print_lcs_matrix(b, c, x, y)
    print("The longest common subsequence is: ", end="")
    print_lcs(b, x, len(x) - 1, len(y) - 1)
    print()


# driver code
# output for Figure 14.8, Pg. 398
x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
y = ['B', 'D', 'C', 'A', 'B', 'A']
get_lcs(x, y)

# output for exercise 14.4-1
x = [1, 0, 0, 1, 0, 1, 0, 1]
y = [0, 1, 0, 1, 1, 0, 1, 1, 0]
get_lcs(x, y)

# Determine LCS for "ncaa tournament" and "north carolina"
x = "ncaa tournament"
y = "north carolina"
get_lcs(x, y)
