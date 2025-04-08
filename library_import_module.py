"""
> Pypi
Pypi is the repository for the open source third-party python packages 

LIBRARIES IN PYTHON

• INTERNAL

The internal libraries are known as Standard Libraries or built-in libraries for python 
ex-Math,random

• EXTERNAL

Many Libraries are available in Pypi that are created other people and are open source So we can easily use them
ex- qr code generator/ bar code generator etc

We Can install them using pip install. Pip is installed when we install Python Distribution.
It is used with the command line to download package repository. from pypi repository 
"""

"""
Example of external library: qr code generator 

First we have to install this library into pc by using command 
pip install qrcode
"""

"""
pip install qrcode
import qrcode

img=qrcode.make('Kode Gurukul')
type(img) 
img.save("Kode.png")

"""     

"""
Example of internal library : using "random" library
"""
import random as r 

save=r.random()
print(save)

save2=r.randint(5,9)
print(save2)

""" import random : This is normal importing of module"""
""" import random as r : This is called alias method """
""" from random import randint : importing specific function """
""" from random import* : It will import all the functions"""

""" import * is not most in use because random contain randint also
math contains randint so computer gets confused in that scenario """

"""
The module is a simple py script.
Any files with py extension with some functions is known as module."""
 
""" The collection of all module is package """
 
"""
Suppose we create 2 module (mod 1 name : calculate & mod2: bank details)

In first module we have created function with print statement 
We can call that function in second module by simply importing that 1st module name """

""" import calculate 
calculate.function_name() """

""" To find all functions of module """
import math
import random

print(dir(math))
print("\n")
print(dir(random))


