"""
Takes (str a, str b) input, 
task: Return a new string by concatenating strings a and b in this order: a, b, b, a
"""
def make_abba(a, b):
  return a + b + b + a

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(make_abba('Hi', 'Bye') == 'HiByeByeHi')
  print(make_abba('Yo', 'Alice') == 'YoAliceAliceYo')
  print(make_abba('What', 'Up') == 'WhatUpUpWhat')
  