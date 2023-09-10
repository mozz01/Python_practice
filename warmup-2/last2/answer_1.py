"""
  Takes (str str) input, 
  task: let the last two characters of str be a substring, then count how many times it occurs in str
"""
def last2(str):
  counter = 0
  new_str = str[:-2]  # Ignoring the last 2 characters so it's not included in the count

  found_index = new_str.find(str[-2:]) # Find at which index the substring ('str[-2:]') occurs
  while(found_index != -1):
    counter += 1
    new_str = new_str[found_index + 1:] # If substring found, only remove the first character
                                        # because the second could be a part of another substring
    found_index = new_str.find(str[-2:])

  return counter

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(last2('hixxhi') == 1)
  print(last2('xaxxaxaxx') == 1)
  print(last2('axxxaaxx') == 2)
