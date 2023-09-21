"""
Takes (int nums[]) input, 
task: Return the first and last elements of nums in an array
"""

def make_ends(nums):
  return [nums[0]] + [nums[-1]]

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(make_ends([1, 2, 3]) == [1, 3])
  print(make_ends([1, 2, 3, 4]) == [1, 4])
  print(make_ends([7, 4, 6, 2]) == [7, 2])
  