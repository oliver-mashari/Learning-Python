# Import module from my_module 
# Example covers how to create a single module (my_module.py)
# Packages are essentially just directories with the __init__.py file

# import modules 
from my_module import my_func
# Import from main package
from MyMainPackage import some_main_script
# Import from sub package
from MyMainPackage.MySubPackage import my_sub_script

my_func()
# Calling functions from modules in package and sub-packages
some_main_script.main_report()
my_sub_script.sub_report()