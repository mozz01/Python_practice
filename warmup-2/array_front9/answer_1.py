"""
  Takes (int[] nums) input, 
  task: return whether 9 is one of the first 4 elements in nums
"""
def array_front9(nums):
  for i in range(len(nums)):
    if nums[i] == 9 and i < 4:
      return True
  return False

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(array_front9([1, 2, 9, 3, 4]) == True)
  print(array_front9([1, 2, 3, 4, 9]) == False)
  print(array_front9([1, 2, 3, 4, 5]) == False)
  print(array_front9([1, 9, 3]) == True)
  print(array_front9([9, 9, 1, 4, 5]) == True)
  print(array_front9([9]) == True)
  print(array_front9([2]) == False)
  print(array_front9([]) == False)