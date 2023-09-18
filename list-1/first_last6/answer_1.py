"""
Takes (int nums[]) input, 
task: return True if 6 appears as either the first or last element in the array.
"""
def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(first_last6([1, 2, 6]) == True)
  print(first_last6([6, 1, 2, 3]) == True)
  print(first_last6([13, 6, 1, 2, 3]) == False)
