"""
  Takes (str str) input, 
  task: return every other character in str, starting with str[0]
"""
def string_bits(str):
  return str[::2]

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(string_bits('Hello') == 'Hlo')
  print(string_bits('Hi') == 'H')
  print(string_bits('Heeololeo') == 'Hello')
  print(string_bits('pi') == 'p')
  print(string_bits('HiHiHi') == 'HHH')
  print(string_bits('') == '')
  print(string_bits('hxaxpxpxy') == 'happy')
