#importing sys for the command-line arguments
import sys


#importing from the sayin library g the function hello
from saying import hello

#checking if the user has provided two arguments at the command line
if len(sys.argv) == 2:
  #printing the argument at location 1
    hello(sys.argv[1])
else:
    sys.exit
