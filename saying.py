#importing the package cowsay
import cowsay

'''definining a function called main and hello and goodbye which will say hello and
goodbye in the form of images or ASCII characters
'''
def main():
    hello("hello, world")
    goodbye("goodbye, world")

def hello(name):
    return cowsay.cow(name)

def goodbye(name):
    return cowsay.trex(name)

# the variable name is set by python to be main when you run a file from the cli
if __name__ == "__main__":
    main()
