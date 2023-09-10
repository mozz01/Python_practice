"""
  Takes (str str, int n) input, 
  task: return str after removing the character at index n
"""
def missing_char(str, n):
  return str[:n] + str[n + 1:]

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(missing_char('kitten', 1) == 'ktten')
  print(missing_char('kitten', 0) == 'itten')
  print(missing_char('kitten', 4) == 'kittn')
  print(missing_char('k', 0) == '')