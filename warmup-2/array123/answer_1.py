"""
  Takes (int[] nums) input, 
  task: return whether the sequence [1, 2, 3] is in nums
"""
def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i:i+3] == [1, 2, 3]:
      return True
  return False

  # for i in range(len(nums) - 2):
  #   if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
  #     return True
  # return False

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(array123([1, 1, 2, 3, 1]) == True)
  print(array123([1, 1, 2, 4, 1]) == False)
  print(array123([1, 1, 2, 1, 2, 3]) == True)
