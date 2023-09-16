"""
Takes (str str) input, 
task: Return true if the number of occurrences of "cat" and "dog" in the given string are equal
"""
def cat_dog(str):
  return sum(1 for i in range(len(str)) if (str[i:i+3] == "cat")) == sum(1 for i in range(len(str)) if (str[i:i+3] == "dog"))

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(cat_dog('catdog') == True)
  print(cat_dog('catcat') == False)
  print(cat_dog('1cat1cadodog') == True)
  print(cat_dog('') == True)
  print(cat_dog('c') == True)
  print(cat_dog('ca') == True)
  print(cat_dog('cat') == False)
  print(cat_dog('dog') == False)