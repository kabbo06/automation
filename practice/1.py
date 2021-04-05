r = int(input())
c = int(input())
row = 0
while row < r:
    col = 0
    while col < c:
        print('*', end=" ")
        col += 1
    print("")
    row += 1
