"""
    Takes (str name) input, 
    task: 
"""
def hello_name(name):
    return name

if __name__ == "__main__":
    # Testing with different inputs and expected results
    print(hello_name('Bob') == 'Hello Bob!')
    print(hello_name('Alice') == 'Hello Alice!')
    print(hello_name('X') == 'Hello X!')
  