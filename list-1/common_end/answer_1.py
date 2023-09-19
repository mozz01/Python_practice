"""
Takes (int a[], int b[]) input, 
task: Return true if both arrays share the same first or last element
"""
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(common_end([1, 2, 3], [7, 3]) == True)
  print(common_end([1, 2, 3], [7, 3, 2]) == False)
  print(common_end([1, 2, 3], [1, 3]) == True)
  