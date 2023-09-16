"""
Takes (str a, str b) input, 
task: Return whether either string appears at the end of the other, not case sensitive
"""
def end_other(a, b):  
  a, b = a.lower(), b.lower()
  return a.endswith(b) or b.endswith(a)

if __name__ == '__main__':
  # Testing with different inputs and expected results
  print(end_other('Hiabc', 'abc') == True)
  print(end_other('AbC', 'HiaBc') == True)
  print(end_other('abc', 'abXabc') == True)