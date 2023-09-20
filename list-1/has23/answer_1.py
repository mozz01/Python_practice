"""
Takes (int nums[]) input, 
task: Return whether there's a 2 or 3 in the array
"""

def has23(nums):
  return 2 in nums or 3 in nums

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(has23([2, 5]) == True)
  print(has23([4, 3]) == True)
  print(has23([4, 5]) == False)
  