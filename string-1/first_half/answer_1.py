"""
Takes (str str) input, 
task:  Return str's first half, str has even length
"""
def first_half(str):
  return str[:int(len(str)/2)]

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(first_half('WooHoo') == 'Woo')
  print(first_half('HelloThere') == 'Hello')
  print(first_half('abcdef') == 'abc')
