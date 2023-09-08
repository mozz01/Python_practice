# "We sleep in if it is not a weekday or we're on vacation"
# if (NOT weekday OR vacation) THEN sleep_in is true

def sleep_in(weekday, vacation):
    return (not weekday or vacation)

def main():
    print(sleep_in(True, True) == True)
    print(sleep_in(True, False) == False)
    print(sleep_in(False, True) == True)
    print(sleep_in(False, False) == True)

if __name__ == "__main__":
    main()