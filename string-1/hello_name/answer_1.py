"""
    Takes (str name) input, 
    task: Return a new string that's formatted like so: "Hello " + name "!"
"""
def hello_name(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    # Testing with different inputs and expected results
    print(hello_name('Bob') == 'Hello Bob!')
    print(hello_name('Alice') == 'Hello Alice!')
    print(hello_name('X') == 'Hello X!')
