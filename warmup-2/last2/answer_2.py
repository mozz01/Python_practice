"""
  Takes (str str) input, 
  task: let the last two characters of str be a substring, then count how many times it occurs in str
"""
def last2(str):
  substring_count = 0
  trimmed_string = str[:-2]
  comparison_str = ""

  for char in trimmed_string:   # Every combination of two consecutive characters in 'trimmed_string'
                                # will be compared against the last two characters of 'str'
    comparison_str += char
    if(comparison_str == str[-2:]):
      substring_count += 1
    comparison_str = char

  return substring_count

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(last2('hixxhi') == 1)
  print(last2('xaxxaxaxx') == 1)
  print(last2('axxxaaxx') == 2)
