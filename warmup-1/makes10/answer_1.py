# Takes (int a, int b) input, 
# task: if either a or b == 10 OR if their sum is 10 return true
def makes10(a, b):
  return (a == 10 or b == 10 or a + b == 10) 

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(makes10(9, 10) == True)
  print(makes10(9, 9) == False)
  print(makes10(1, 9) == True)
  print(makes10(10, 1) == True)
  print(makes10(10, 0) == True)
  print(makes10(5, 5) == True)
  print(makes10(-1, 11) == True)
  print(makes10(3, 9) == False)
  print(makes10(-8, -2) == False)
  print(makes10(-10, 9) == False)