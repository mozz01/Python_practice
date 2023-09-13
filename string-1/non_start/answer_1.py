"""
Takes (str a, str b) input, 
task: Remove the first character of both strings, then return their concatenation in order (a + b)
"""
def non_start(a, b):
  return a[1:] + b[1:]

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(non_start('Hello', 'There') == 'ellohere')
  print(non_start('java', 'code') == 'avaode')
  print(non_start('shotl', 'java') == 'hotlava')
