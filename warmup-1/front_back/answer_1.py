"""
  Takes (str str) input, 
  task: return str after swaping the first and last characters
"""
def front_back(str):
  length = len(str)
  
  if(length > 1):
    front = str[0]
    end = str[length - 1]
    new_str = str[1:length - 1]
    return end + new_str + front
  
  return str

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(front_back('code') == 'eodc')
  print(front_back('a') == 'a')
  print(front_back('ab') == 'ba')
  print(front_back('') == '')
  print(front_back('aavJ') == 'Java')
  print(front_back('abc') == 'cba')
  print(front_back('Hello World!') == '!ello WorldH')