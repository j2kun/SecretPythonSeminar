from unittest import test


# greet: string -> string
# return a string which greets the user whose name is input
def greet(name):
   return "Hello, " + name 



# test(expected, actual)
test("Hello, ", greet(""))
test("Hello, Jeremy", greet("Jeremy"))
test("Hello, liae!", greet("liae!"))



#listA = [1,2,3,4]
#for element in listA:
#   print(element + 1)
#
#listA[2]


# add1: [int] -> [int]
# create a new list which adds1 to each element of the input list
def add1(myList):
   outputList = []

   for x in myList:
      outputList.append(x+1)

   return outputList


test([], add1([]))
test([2], add1([1]))
test([-4,11,1000], add1([-5,10,999]))



# largestSquareLessThan: int -> int
# find the largest square less than the input
# the input must be at least 1
def largestSquareLessThan(n):
   theNumber = 0

   while (theNumber+1)**2 < n:
      theNumber = theNumber + 1

   return theNumber ** 2
   


test(1, largestSquareLessThan(4))
test(0, largestSquareLessThan(1))
test(16, largestSquareLessThan(17))
test(256, largestSquareLessThan(260))
