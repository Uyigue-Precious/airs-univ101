#Stagec -your first python script 
#Health Check
import sys
import platform
import os

print("Hello from AIRS UNIV-101!")
print("Python version:", platform.python_version()) # checks the version of python installed
print("Operating system:", platform.system())
print("Python is running from:", sys.executable)

print("=" * 44)

print("virtual environment active:", sys.prefix != sys.base_prefix)

print("python 3.12 or newer:", sys.version_info>=(3,11))

print("Python implementation:", platform.python_implementation()) #tells what type of python was installed eg Cpython

print(platform.architecture()[0]) #checks for  computer bit

print("working folder:", os.getcwd()) #get me the forder I am working from