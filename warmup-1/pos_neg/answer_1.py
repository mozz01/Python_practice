"""
  Takes (int a, int b, bool negative) input, 
  task: return True if (a < 0 and b > 0) OR (a > 0 and b < 0), 
  if negative then return True only if (a < 0 and b < 0)
"""
def pos_neg(a, b, negative):
  a_neg = a < 0
  b_neg = b < 0
  
  return a_neg and b_neg if (negative) else (not (a_neg and b_neg)) and (a_neg or b_neg)
  
  # result = False
  # if (negative):
  #   result = a_neg and b_neg
  # else:
  #   result = (not (a_neg and b_neg)) and (a_neg or b_neg)
  # return result

if __name__ == "__main__":
  # Testing with different inputs and expected results
  # Logic XOR: ~[a_neg ^ b_neg] ^ [a_neg v b_neg]
  print(pos_neg(-1, -1, False) == False)
  print(pos_neg(1, -1, False) == True)
  print(pos_neg(-1, 1, False) == True)
  print(pos_neg(1, 1, False) == False)

  # Logic AND
  print(pos_neg(-1, -1, True) == True)
  print(pos_neg(1, -1, True) == False)
  print(pos_neg(-1, 1, True) == False)
  print(pos_neg(1, 1, True) == False)

