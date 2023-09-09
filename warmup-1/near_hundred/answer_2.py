"""
  Takes (int n) input, 
  task: return true if n is within 10 units away from either 100 or 200
  so accepted n values are within the ranges 90 <= n <= 110 and 190 <= n <= 210
  100 - 90 = 10, 100 - 110 = -10, 200 - 210 = -10
  abs(target - n) <= acceptable_range
"""
def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200 - n) <= 10

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(near_hundred(93) == True)
  print(near_hundred(90) == True)
  print(near_hundred(89) == False)
  print(near_hundred(110) == True)
  print(near_hundred(100) == True)
  print(near_hundred(101) == True)
  print(near_hundred(111) == False)
  print(near_hundred(206) == True)
  print(near_hundred(193) == True)
  print(near_hundred(211) == False)
  print(near_hundred(501) == False)
  print(near_hundred(0) == False)
  print(near_hundred(1) == False)
  print(near_hundred(-101) == False)
  print(near_hundred(-93) == False)
  print(near_hundred(9) == False)
  print(near_hundred(10) == False)
  print(near_hundred(11) == False)
  print(near_hundred(55) == False)