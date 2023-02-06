# This module is used to work with files and folders

import os

# 1. Create a directory

# Directory

directory = "test_dir"

# Parrent directory

parent_dir = "C:/Users/matya" #

# Path

path = os.path.join(parent_dir, directory)

# Create the DIR
# os.mkdir(path)
# print("Directory '% s' created " % directory)

# 2. Make a file in the new directory

filename = "testfile.txt"

filepath = os.path.join(path, filename)

# Write to the new file

with open(os.path.join(path, filename), "w") as file1:
    toFile = "Content of my new file"
    file1.write(toFile)

print("File" + filename + " created in " + directory + " folder")



