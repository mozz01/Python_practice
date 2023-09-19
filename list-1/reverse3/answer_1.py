"""
Takes (int nums[]) input, 
task: return the reverse of nums
"""

def reverse3(nums):
  return nums[-1::-1]

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(reverse3([1, 2, 3]) == [3, 2, 1])
  print(reverse3([5, 11, 9]) == [9, 11, 5])
  print(reverse3([7, 0, 0]) == [0, 0, 7])
