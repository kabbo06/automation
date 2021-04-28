def linear_search(arr, x):

    for index, value in enumerate(arr):
        
        if value == x:

            return index
 
    else:

        return -1


if __name__ == "__main__":
  data = input("Please provide integer list elements like Ex: 2,4,8 ... \n")
  arr1 = list(data.split(','))
  arr2 = [int(arr1[i]) for i in range(len(arr1))]
  arr3 = sorted(arr2)

  x = int(input("Provide integer item or number to check in given list \n"))

  result = linear_search(arr3, x)

  if result != -1:
      print("Item is present at index", str(result))

  else:
      print("Item is not present in list")

