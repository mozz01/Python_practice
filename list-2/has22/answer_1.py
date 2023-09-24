"""
Takes (int nums[]) input, 
task: Return whether there are two adjacent 2's in the array
Other ways:
  return any((nums[i] == 2 and nums[i+1] == 2) for i in range(len(nums) - 1))
  return any(([nums[i]] + [nums[i+1]] == [2, 2]) for i in range(len(nums) - 1))
"""

def has22(nums):
  return any((nums[i:i+2] == [2, 2]) for i in range(len(nums) - 1))

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(has22([1, 2, 2]) == True)
  print(has22([1, 2, 1, 2]) == False)
  print(has22([2, 1, 2]) == False)
  