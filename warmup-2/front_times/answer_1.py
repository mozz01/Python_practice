"""
  Takes (str str, int n) input, 
  task: return str's first 3 characters repeated n times, or str if it's shorter than 3 in length
"""
def front_times(str, n):
  return str * n if (len(str) < 3) else str[:3] * n 

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(front_times('Chocolate', 2) == 'ChoCho')
  print(front_times('Chocolate', 3) == 'ChoChoCho')
  print(front_times('Abc', 3) == 'AbcAbcAbc')
  print(front_times('', 3) == '')
  print(front_times('Abc', 0) == '')
  print(front_times('A', 4) == 'AAAA')
