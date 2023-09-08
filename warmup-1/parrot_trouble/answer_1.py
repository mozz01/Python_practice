# Takes (bool talking, int hour) input, 
# task: if talking and (hour < 7 or hour > 20) return true
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

if __name__ == "__main__":
    # Testing with different inputs and expected results
    print(parrot_trouble(True, 6) == True)
    print(parrot_trouble(True, 7) == False)
    print(parrot_trouble(False, 6) == False)
    print(parrot_trouble(True, 20) == False)
    print(parrot_trouble(True, 21) == True)