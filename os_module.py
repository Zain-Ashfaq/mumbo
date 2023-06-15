# Using os to do things

import os

# Echo to terminal
# os.system('echo Hello world')

# make and change directories

# create a directory

# Directory name
directory = "test_dir"
#
# Parent name
parent_dir = "D:/Zain Sparta Global/tech241"

# Path
path = os.path.join(parent_dir,directory)

# Create DIR

# os.mkdir(path)

# Putting a file in the new dir

filename = "testfile.txt"

filepath = os.path.join(path,filename)

with open(filepath, "w") as file1:
    toFile = "Contents of file is written here"
    file1.write(toFile)

print(f"file {filename} created in {directory} folder")