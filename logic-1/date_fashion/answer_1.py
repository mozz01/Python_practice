"""
Takes (int you, int date) input, 
task:  
  if        you >= 8 or date >= 8   return 2
  else if   you <= 2 or date <= 2   return 0
  else                              return 1
"""

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  return 1

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(date_fashion(5, 10) == 2)
  print(date_fashion(5, 2) == 0)
  print(date_fashion(5, 5) == 1)
  print(date_fashion(10, 2) == 0)
  print(date_fashion(2, 9) == 0)