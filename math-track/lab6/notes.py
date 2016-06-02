
class JeremysException(Exception):
   pass


def f():
   try:
      g()
   except JeremysException as myException:
      print("Got Jeremy's exception! Here's is the data: %s" % myException)

def g():
   try:
      return h()
   except ZeroDivisionError:
      print("You got a zero division, butthole!")
      return 7

def h():
   raise JeremysException("Jeremy doesn't like you")
   return 4

def divide(a, b):
   if b == 3:
      raise DivideByThreeException()
   else:  
      return a/b

f()

'''x = input("Enter a number: ")
while True:
   try:
      usersNum = int(x)
      break
   except:
      x = input("Your input was not a number. Try again: ")

print("Your number is %d" % usersNum)
'''

class SquaresIter:
   def __init__(self):
      self.state = 1

   def __iter__(self):
      return self

   def __next__(self):
      if self.state > 100:
         raise StopIteration

      value = self.state
      self.state = self.state + 1
      return value**2


class Vector():
   def __init__(self, coords):
      self.coords = coords

   def __iter__(self):
      return iter(self.coords)


for entry in Vector([1,2,3]):
   print(entry + 1)



def squaresList(upToN):
   state = 1
   while state < upToN:
      yield state ** 2
      state += 1


