"""
  Takes (str str) input, 
  task: create a new string consisting of the input string's front repeated 3 times.
  The front represents the first 3 characters OR the entire string if it's less than 3 in length.
"""
def front3(str):
  return str[:3] * 3 if (len(str) >= 3) else str[:len(str)] * 3

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(front3('Java') == 'JavJavJav')
  print(front3('Chocolate') == 'ChoChoCho')
  print(front3('abc') == 'abcabcabc')
