"""
  Takes (str str, int n) input, 
  task: return str repeated n times
"""
def string_times(str, n):
  return str * n

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(string_times('Hi', 2) == 'HiHi')
  print(string_times('Hi', 1) == 'Hi')
  print(string_times('Hi', 3) == 'HiHiHi')
  print(string_times('Hi', 0) == '')
  print(string_times('', 3) == '')
  