def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def main():
    print(monkey_trouble(True, True) == True)
    print(monkey_trouble(True, False) == False)
    print(monkey_trouble(False, True) == False)
    print(monkey_trouble(False, False) == True)

if __name__ == "__main__":
    main()