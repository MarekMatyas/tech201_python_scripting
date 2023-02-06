import os
import subprocess

# Python doesn't actually run shell commands

# Instead we can use Python to run shell scripts files

script_dir = os.path.dirname(__file__) #Store the path to the current file (__file__)

script_absolute_path = os.path.join(script_dir + "scripts.sh")

subprocess.call(["sh", script_absolute_path])
