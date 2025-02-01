def countOddEven(arr):
    countOdd = 0
    countEven = 0
    for num in arr:
      
        # checking if the element is even
        if num % 2 == 0:
            countEven += 1
        else:
          
            # if not even, it must be odd
            countOdd += 1
    return countOdd, countEven

if __name__ == "__main__":
  arr = [2, 3, 4, 5, 6]
  ans = countOddEven(arr)
  print(ans[0], ans[1])