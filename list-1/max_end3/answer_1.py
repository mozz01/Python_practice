"""
Takes (int nums[]) input, 
task: Compare the first and last elements of nums for the largest value and return the entire array of that element
"""

def max_end3(nums):
  return [max(nums[0], nums[-1])] * 3

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(max_end3([1, 2, 3]) == [3, 3, 3])
  print(max_end3([11, 5, 9]) == [11, 11, 11])
  print(max_end3([2, 11, 3]) == [3, 3, 3])
