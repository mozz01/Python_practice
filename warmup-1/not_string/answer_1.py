"""
  Takes (str str) input, 
  task: if str doesn't start with "not" then add "not " 
  to the beginning and return it, else return the input string  
"""
def not_string(str):
  return str if (str[0:3] == "not") else "not " + str

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(not_string("candy") == "not candy")
  print(not_string("x") == "not x")
  print(not_string("not bad") == "not bad")
  print(not_string("nothing") == "nothing")
  print(not_string("nobody") == "not nobody")
  print(not_string("is not") == "not is not")
  print(not_string("not") == "not")
  print(not_string("") == "not ")
