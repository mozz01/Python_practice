"""
Takes (str str) input, 
task: shift str's characters 2 positions to the left and wrap the front to the end so it keeps its original length
"""
def left2(str):
  return str[2:] + str[:2]

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(left2('Hello') == 'lloHe')
  print(left2('java') == 'vaja')
  print(left2('Hi') == 'Hi')
