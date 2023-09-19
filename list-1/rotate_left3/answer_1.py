"""
Takes (int nums[]) input, 
task: Return nums with its elements shifted one position to the left.

These also work:
  [nums[1]] + [nums[2]] + [nums[0]]
  OR
  nums[1:] + [nums[0]]
"""

def rotate_left3(nums):
  return [nums[i] for i in range(1, len(nums))] + [nums[0]]

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(rotate_left3([1, 2, 3]) == [2, 3, 1])
  print(rotate_left3([5, 11, 9]) == [11, 9, 5])
  print(rotate_left3([7, 0, 0]) == [0, 0, 7])
