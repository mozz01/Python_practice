"""
Takes (int nums[]) input, 
task: Return the number of even integers in nums
"""

def count_evens(nums):
  return sum(1 for i in nums if i % 2 == 0)

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(count_evens([2, 1, 2, 3, 4]) == 3)
  print(count_evens([2, 2, 0]) == 3)
  print(count_evens([1, 3, 5]) == 0)
  