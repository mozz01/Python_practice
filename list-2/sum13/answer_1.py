"""
Takes (int nums[]) input, 
task: 
  - Return the sum of the array elements or 0 if it's empty
  - don't count 13 and one element that comes after
"""

def sum13(nums):
  sum = 0 
  flag = False

  for i in range(len(nums)):
    if nums[i] == 13 or flag:
      flag = not flag
      continue
    sum += nums[i]

  return sum

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(sum13([1, 2, 2, 1]) == 6)
  print(sum13([1, 1]) == 2)
  print(sum13([1, 2, 2, 1, 13]) == 6)
  print(sum13([1, 13, 5, 1, 1]) == 3)
  