"""
Takes (int nums[]) input, 
task: Return the sum of nums elements: nums[0] + nums[1] + nums[2]
"""
def sum3(nums):
  return sum(nums)

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(sum3([1, 2, 3]) == 6)
  print(sum3([5, 11, 2]) == 18)
  print(sum3([7, 0, 0]) == 7)
  