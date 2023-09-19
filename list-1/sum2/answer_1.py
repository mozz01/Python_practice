"""
Takes (int nums[]) input, 
task: Return the sum of the first 2 elements
"""

def sum2(nums):
  # return 0 if (len(nums) < 1) else sum(nums[i] for i in range(min(2, len(nums))))
  return sum(nums[i] for i in range(min(2, len(nums))))

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(sum2([1, 2, 3]) == 3)
  print(sum2([1, 1]) == 2)
  print(sum2([1, 1, 1, 1]) == 2)
  print(sum2([3]) == 3)
  print(sum2([]) == 0)
