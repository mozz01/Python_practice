"""
Takes (int nums[]) input, 
task: 
- Return the sum of the numbers in the array
- Ignore sections between 6 and 7, ends included
- Every 6 will be followed by at least one 7
"""

def sum67(nums):
  flag = False
  sum = 0

  for number in nums:
    if number == 6 and not flag:
      flag = True
      continue
    if number == 7 and flag:
      flag = False
      continue
    if not flag:
      sum += number
    
  return sum

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(sum67([1, 2, 2]) == 5)
  print(sum67([1, 2, 2, 6, 99, 99, 7]) == 5)
  print(sum67([1, 1, 6, 7, 2]) == 4)
  print(sum67([1, 1, 6, 99, 99, 7, 2, 6, 10, 7, 1]) == 5)
  print(sum67([]) == 0)
  print(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) == 2)
  print(sum67([2, 2, 6, 7, 7]) == 11)
  print(sum67([11, 6, 7, 11]) == 22)
  