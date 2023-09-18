"""
Takes (int nums[]) input, 
task: Return true if nums is not empty and the first and last elements are equal
"""
def same_first_last(nums):
  return bool(nums) and nums[0] == nums[-1]

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(same_first_last([1, 2, 3]) == False)
  print(same_first_last([1, 2, 3, 1]) == True)
  print(same_first_last([1, 2, 1]) == True)
  print(same_first_last([]) == False)
  