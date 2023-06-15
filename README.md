# Basics of scripting in Python


In Python, libraries and modules are essential components that allow developers to extend the functionality of their programs. Modules are smaller units of code that can be imported into a script, while libraries encompass a collection of related modules.
## Seven "core" modules in Python

Python provides a wide range of modules to handle various tasks. Here is a brief explanation of each of the seven commonly used "core" modules:
## sys

The sys module provides access to various system-specific parameters and functions. It allows you to interact with the Python interpreter and retrieve information about the system, such as the Python version being used.

```python

import sys

# Get Python version
print(sys.version)
```
## os

The os module provides a way to interact with the operating system. It allows you to perform operations related to the file system, such as getting the current working directory, navigating directories, and executing system commands.

```python

import os

# Get current working directory
print(os.getcwd())
```

## subprocess

The subprocess module enables the execution of external programs or commands from within a Python script. It provides functions to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

```python

import subprocess

# Runs an external file when executed
subprocess.run(["python", "hello_world.py"])
```
## math

The math module provides mathematical functions and constants. It includes functions for basic arithmetic operations, trigonometry, logarithms, exponentiation, and more. It also defines several mathematical constants, such as pi.

```python

import math

pi = math.pi
pi_string = str(pi)
print("The value of pi is", pi_string)
```
## random

The random module allows you to generate random numbers and make random selections. It provides functions to generate random integers, floating-point numbers, and random selections from sequences.

```python

import random

random_number = random.randrange(1, 10)
print(random_number)
```
## datetime

The datetime module supplies classes for working with dates, times, and time intervals. It enables you to create, manipulate, format, and perform calculations with dates and times. The datetime class from this module is commonly used to represent and work with dates and times.

```python

import datetime

current_date = datetime.datetime.now()
print(current_date)
```
## json

The json module provides functions to work with JavaScript Object Notation (JSON) data. It allows you to encode Python objects into JSON strings and decode JSON strings into Python objects. This module is commonly used for serializing and deserializing data when working with APIs or storing data in a structured format.

``` python

import json

x = {
    "name": "John",
    "age": 30,
    "city":{"Merseyside":"Liverpool"}
}

y = json.dumps(x)

print(y)
print(type(y))
print(type(x))
```

## Echo to terminal

```python

# os.system('echo Hello world')
```

This line demonstrates how to use os.system to execute a command in the terminal. In this case, it's an echo command that prints "Hello world".
Make and change directories
## Create a directory

```python

# Directory name
directory = "test_dir"

# Parent name
parent_dir = "D:/Zain Sparta Global/tech241"

# Path
path = os.path.join(parent_dir, directory)

# Create DIR
# os.mkdir(path)
```
These lines show how to create a new directory using os.mkdir. It specifies the directory name (test_dir) and the parent directory (D:/Zain Sparta Global/tech241), then uses os.path.join to create the complete path. Uncommenting the line os.mkdir(path) would actually create the directory.

## Putting a file in the new directory

``` python

filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    toFile = "Contents of file is written here"
    file1.write(toFile)
    
print(f"file {filename} created in {directory} folder")
```
These lines demonstrate how to create a file within the newly created directory. It defines the filename (testfile.txt) and uses os.path.join to create the complete file path. Then, it uses open to open the file in write mode, writes the contents (Contents of file is written here), and finally prints a message confirming the creation of the file in the specified folder.

```python
import os
import subprocess
```
The code above imports the necessary modules, os and subprocess.

```python

# Stores the file path to the current file
script_dir = os.path.dirname(__file__)

# Stores the filepath to the script you want to run
script_absolute_path = os.path.join(script_dir + "/shell_script.sh")
print(script_absolute_path)
```
In these lines, the script retrieves the file path to the current file using os.path.dirname(__file__). Then, it constructs the absolute path to the script that needs to be executed by combining the script_dir and the script name (shell_script.sh). The os.path.join function is used for this purpose. Finally, it prints the script_absolute_path to the console.

```python

# Calls the shell and runs it
subprocess.call(['sh', script_absolute_path])
```
This line uses subprocess.call to execute a shell script. It calls the shell and runs the script specified by script_absolute_path. The script is executed using the sh command.

The code demonstrates how to obtain the file path to the current script, construct the absolute path to a shell script, and execute it using subprocess.call.
