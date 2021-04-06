def pattern(r, c):
  row = 0
  while row < r:
      col = 0
      while col < c:
          print('*', end=" ")
          col += 1
      print("")
      row += 1

if __name__ == "__main__":
    r = int(input("Please enter 'row' number: "))
    c = int(input("Please enter 'column' number: "))
    pattern(r,c)

