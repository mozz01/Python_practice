"""
Takes (str str) input, 
task: Given a string of length 2 or more, return a new string that is 3 copies of str's last 2 characters 
"""
def extra_end(str):
  return str[-2:] * 3

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(extra_end('Hello') == 'lololo')
  print(extra_end('ab') == 'ababab')
  print(extra_end('Hi') == 'HiHiHi')