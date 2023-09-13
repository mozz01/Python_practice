"""
Takes (str str) input, 
task:  Return str's first two characters, else return str 
"""
def first_two(str):
  return str[:2]

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(first_two('Hello') == 'He')
  print(first_two('abcdefg') == 'ab')
  print(first_two('ab') == 'ab')
  print(first_two('X') == 'X')
  print(first_two('') == '')