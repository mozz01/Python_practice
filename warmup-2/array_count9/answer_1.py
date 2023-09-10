"""
  Takes (int[] nums) input, 
  task: return the number of 9's in nums
"""
def array_count9(nums):
  count = 0
  for integer in nums:
    if (integer == 9):
      count += 1
  return count

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(array_count9([1, 2, 9]) == 1)
  print(array_count9([1, 9, 9]) == 2)
  print(array_count9([1, 9, 9, 3, 9]) == 3)
