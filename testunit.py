"""My own implimentation of unittest module with minimum functionality."""


import classes
import types

def testfun(baseclassname):
  c, base, a, classdir = [], [], [], []
  attr = dir(classes) 						#returns a list of attributes, methods etc. from the main module called

  for i in attr:
    if type(getattr(classes,i))==types.ClassType:		#checks whether element in list is a class type
      c.append(i)						#and if it is, append it to a list,c.
								#c contains a list of all the class names in the module called.
  for i in c:
    base = getattr(classes,i).__bases__				#gets the __bases__ i.e the address of the base class fom each element in c (if any).
    if getattr(classes,baseclassname) in base:			#checks whether the base class address is in the bases of the class and...
      a.append(i)						#append it to the list a.

  for i in a:
    classdir = dir(getattr(classes,i))				#for each class that extends the main class (in this case ABC), saves it into a list
    for j in classdir:						#and for each element of the list, 
      if type(getattr(getattr(classes,i),j)) == types.MethodType:#checks whether the attribute is a function method
        if j[:4]=='test':					#if it is a functin then checks whether the function starts with 'test'
          getattr(getattr(classes,i)(),j)()

testfun()

