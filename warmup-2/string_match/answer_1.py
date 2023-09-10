"""
  Takes (str a, str b) input, 
  task: return how many two-character substrings both string a and b share
"""
def string_match(a, b):
  a_substrings = set()
  b_substrings = set()

  for i in range(len(a) - 1):
    a_substrings.add(a[i:i+2])
  
  for i in range(len(b) - 1):
    b_substrings.add(b[i:i+2])
  
  return len(a_substrings.intersection(b_substrings))

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(string_match('xxcaazz', 'xxbaaz') == 3)
  print(string_match('abc', 'abc') == 2)
  print(string_match('abc', 'axc') == 0)
  print(string_match('aabbccdd', 'abbbxxd') == 2) # Corrected from 1 to 2. Matches: 'ab' and 'bb'
  print(string_match('aaxxaaxx', 'iaxxai') == 3)
  print(string_match('iaxxai', 'aaxxaaxx') == 3)
  print(string_match('h', 'hello') == 0)
  print(string_match('', 'hello') == 0)
  print(string_match('he', 'hello') == 1)
  print(string_match('hello', 'he') == 1)
