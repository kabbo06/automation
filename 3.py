def pattern(n):

    k = 0 
    for i in range(n, 0, -1):
        k += 1
        for j in range(1, i + 1):
            print("*",end=" ")
      
        print(" ")
 
if __name__ == "__main__":

    n = int(input("Enter a number: "))
    pattern(n)
