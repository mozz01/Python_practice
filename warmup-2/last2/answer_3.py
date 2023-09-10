"""
  Takes (str str) input, 
  task: let the last two characters of str be a substring, then count how many times it occurs in str
"""
def last2(str):
  substring_count = 0
  trimmed_string = str[:-1]   # Only ignore the last character because the 2nd last
                              # could be a part of a matching substring
  for index in range(len(trimmed_string) - 1):  # range() will stop the loop before the last character in 'trimmed_string'
    comparison_str = trimmed_string[index:index+2]
    if(comparison_str == str[-2:]):
      substring_count += 1

  return substring_count

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(last2('hixxhi') == 1)
  print(last2('xaxxaxaxx') == 1)
  print(last2('axxxaaxx') == 2)
  print(last2('xxxx') == 2)
