"""
Takes (str str) input, 
task: return a new string where there's an additional duplicate character in place of each original character
"""
def double_char(str):
  result = ""
  for char in str:
    result += char * 2 
  return result

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(double_char('The') == 'TThhee')
  print(double_char('AAbb') == 'AAAAbbbb')
  print(double_char('Hi-There') == 'HHii--TThheerree')
