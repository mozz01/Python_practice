# Takes (int n) input, 
# task: if n <= 21 return the absolute difference between n and 21 (absDiff), but
# return 2 * absDiff if n > 21
def diff21(n):
  return (n - 21) * 2 if (n > 21) else 21 - n

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(diff21(-2) == 23)
  print(diff21(-1) == 22)
  print(diff21(0) == 21)
  print(diff21(1) == 20)
  print(diff21(2) == 19)
  print(diff21(22) == 2)
  print(diff21(23) == 4)
  print(diff21(31) == 20)
  print(diff21(19) == 2)
  print(diff21(10) == 11)
  print(diff21(21) == 0)