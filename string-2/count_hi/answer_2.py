"""
Takes (str str) input, 
task: return the number of substrings "hi" found in str
"""
def count_hi(str):
  return sum(1 for i in range(len(str)) if (str[i:i+2] == "hi"))

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(count_hi('abc hi ho') == 1)
  print(count_hi('ABChi hi') == 2)
  print(count_hi('hihi') == 2)
  print(count_hi('') == 0)
  print(count_hi('h') == 0)
  print(count_hi('hi') == 1)
  print(count_hi('Hi is no HI on ahI') == 0)
  print(count_hi('hiHIhi') == 2)
