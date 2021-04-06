def pattern(n):
     
    for i in range(0, n):
     
        for j in range(0, i+1):
            print("*",end=" ")
      
        print(" ")
 
if __name__ == "__main__":

    n = int(input("Enter a number: "))
    pattern(n)
