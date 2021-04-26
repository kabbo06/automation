def binary_search(arr, low, high, x):

    if high >= low:

       mid = (high + low) // 2
 
       if arr[mid] == x:
            return mid

       elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
       else:
            return binary_search(arr, mid + 1, high, x)
 
    else:

      return -1


if __name__ == "__main__":
  data = input("Please provide integer list elements like Ex: 2,4,8 ... \n")
  arr1 = list(data.split(','))
  arr2 = [int(arr1[i]) for i in range(len(arr1))]
  arr3 = sorted(arr2)

  x = int(input("Provide integer item or number to check in given list \n"))

  result = binary_search(arr3, 0, len(arr2) - 1, x)

  if result != -1:
      print("Item is present at index", str(result))

  else:
      print("Item is not present in list")

