"""
  Takes (str str) input, 
  task: progressively concatenate str's substrings one character at a time, starting with str[0]
"""
def string_splosion(str):
  result = ""
  temp = ""
  for char in str:
    temp += char
    result += temp
  return result


if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(string_splosion('Code') == 'CCoCodCode')
  print(string_splosion('abc') == 'aababc')
  print(string_splosion('ab') == 'aab')
  print(string_splosion('There') == 'TThTheTherThere')
