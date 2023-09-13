"""
Takes (str a, str b) input, 
task:  Determine which string is shorter and which is longer, then return a new string in this format: short + long + short
"""
def combo_string(a, b):
  return b + a + b if(len(a) > len(b)) else a + b + a

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(combo_string('Hello', 'hi') == 'hiHellohi')
  print(combo_string('hi', 'Hello') == 'hiHellohi')
  print(combo_string('aaa', 'b') == 'baaab')
