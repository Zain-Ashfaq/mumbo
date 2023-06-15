# Basics of scripting in Python

# Libraries and Modules - Modules smaller, libraries bigger

# Seven "core" modules in Python

# import sys
#
# # Get Python version
# print(sys.version)
#
# import os
#
# # Get current working directory
# print(os.getcwd())

import subprocess

# Runs an external file when executed
# subprocess.run(["python", "hello_world.py"])

import math

pi = math.pi
pi_string = str(pi)
print("the value of pi is ", pi_string)

import random

random = random.randrange(1,10)
print(random)

import datetime

whatisthedate = datetime.datetime.now()
print(whatisthedate)

import json

x = {
    "name":"John",
    "age":30,
    "city":{"Merseyside":"Liverpool"}
}

y = json.dumps(x)

print(y)
print(type(y))
print(type(x))