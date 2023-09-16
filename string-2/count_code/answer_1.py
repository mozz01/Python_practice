"""
Takes (str str) input, 
task: Return true if 'co' + any letter + 'e' appears in the given string
"""
def count_code(str):
  count = 0
  for i in range(len(str) - 3):
    if ( str[i:i+2] == 'co' and (str[i+2].isalpha()) and (str[i+3] == 'e') ):
      count += 1
  return count

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(count_code('aaacodebbb') == 1)
  print(count_code('codexxcode') == 2)
  print(count_code('cozexxcope') == 2)
