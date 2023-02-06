# Scripting
import datetime
import os
# Scripting is all about being efficient and are easier to read.
# Shorter pieces of code that allow us to do things we would otherwise have to do manually

# Unlike programs, scripts are one file and do not need to be compiled

# API's tend to use scripts.
# Scripts use less or no abstraction and are not as flexible as programs but they are much easier to read and write

# Scripts are almost always written in "high level" languages (easy to read)- Python, Bash, Ruby
# "low level" (harder to read)

# Why Python

# Open source
# Many libraries
# Easy to understand
# Large community
# Language interoperability (can talk to other languages, OS's and software).

# Why is scripting important for DevOps engineers?

# Automation -> of mundane tasks. Making life easier for Engineers by automating repetative tasks


# For scripts we need to use modules and libraries

# 7 core modules in Python
# Sys
#  Os
# Subprocesses
# Math
# Random
# DateTime
# JSON



#Sys module scripts (allows us to interact with python modules)

import sys

print(sys.version)


# os module script(interacts with the host OS, working with files)

print(os.getcwd()) # get current working directory

# os.chdir() #changes current directory

#os.mkdir("path") # make new directory


# Subprocesses module script

# Can be used to create and interact with subprocess being managed by our Python interpreter.

import subprocess

subprocess.run(["python", "hello_world.py"]) # first write python interpreter and the file or path, make sure that the initial file works properly


# Math module scripts
import math
pi = math.pi
pi_string = str(pi)
print("The value of pi is: " + pi_string)


# Random module script

import random

randum = random.randrange(1, 10)
print(randum)


# DateTime module scripts (gets date and time)
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate)


# JSON module script (human readable)
import json
x = {
    "name": "John",
    "age": 30,
    "city": "London",


}

y = json.dumps(x)#The dump() method is used when the Python objects have to be stored in a file.
#   json dumps -> returns a string representing a json object from an object. > json dumps -> returns a string representing a json object from a dict.
print(y) ## output from the terminal is -> {"name": "John", "age": 30, "city": "London"}









