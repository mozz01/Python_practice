"""
Takes (int cigars, bool is_weekend) input, 
task: Return if 40 <= cigars <= 60 
          OR if is_weekend and 40 <= cigars
"""

def cigar_party(cigars, is_weekend):
  return cigars >= 40 and (is_weekend or cigars <= 60)


if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(cigar_party(30, False) == False)
  print(cigar_party(50, False) == True)
  print(cigar_party(70, True) == True)
  
  print(cigar_party(59, False) == True)
  print(cigar_party(60, False) == True)
  print(cigar_party(61, False) == False)
  print(cigar_party(41, False) == True)
  print(cigar_party(40, False) == True)
  print(cigar_party(39, False) == False)
  
  print(cigar_party(59, True) == True)
  print(cigar_party(60, True) == True)
  print(cigar_party(61, True) == True)
  print(cigar_party(41, True) == True)
  print(cigar_party(40, True) == True)
  print(cigar_party(39, True) == False)
  