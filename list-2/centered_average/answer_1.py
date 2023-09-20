"""
Takes (int nums[]) input, 
task: Return the centered average (CA)
  - CA = mean of array without one copy of the min(nums) and the max(nums)
  - Use int division
  - Assume len(nums) >= 3
"""

def centered_average(nums):
 return int( (sum(nums) - min(nums) - max(nums))/(len(nums) - 2) )

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(centered_average([1, 2, 3, 4, 100]) == 3)
  print(centered_average([1, 1, 5, 5, 10, 8, 7]) == 5)
  print(centered_average([-10, -4, -2, -4, -2, 0]) == -3)
  