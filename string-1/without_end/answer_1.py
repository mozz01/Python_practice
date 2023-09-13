"""
Takes (str str) input, 
task:  Return str but without the front and end characters, str length >= 2
"""
def without_end(str):
  return str[1:-1]

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(without_end('Hello') == 'ell')
  print(without_end('java') == 'av')
  print(without_end('coding') == 'odin')
