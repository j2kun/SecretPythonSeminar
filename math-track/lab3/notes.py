

# examples of variable scope inside and outside functions

y = 9
print(y)

def greet(name):
   # global y

   y = 21
   if name == "Jeremy":
      x = y + 7
   else:
      return "Greetings, " + name

   return x+1

print(greet("Jeremy"))
print(y)


for i in range(100):
   x = i+2

print(x)



# nested for loops and the break statement

def myFactorial():
   myList = []
   for i in range(10):
      iFactorial = 1
      for j in range(1,i+1):
         if j >= 7:
            # return myList  # this would end the function!
            break # instead, break just ends the loop
         iFactorial = iFactorial * j

      myList.append(iFactorial)
   
   return myList

print(myFactorial())


L = [1,2,3,4,5]

for x in L:
   print(x)
   print(L)
   if x != 7:
      L.append(7)



# common list paradigms

# square all the numbers in L
def square(L):
   squaresList = []

   for number in L:
      squaresList.append(number * number)

   return squaresList


# list comprehension
L = [1,2,3,4]

squares = [x*x for x in L]

grid = [[1,1], [1,2], [1,3], [1,4], [2,1], [2,2], [2,3], [2,4]]

def pairs(numRows, numCols):
   myList = []

   for i in range(numRows):
      row = [[i,j] for j in range(numCols)]
      myList.append(row)

      #row = []

      #for j in range(numCols):
      #   row.append([i,j])
      #
      #myList.append(row)

   return myList

print(pairs(4,5))

grid = [[i,j] for i in range(5) for j in range(6)]

# translates to this nesting of loops
#for i in range(5):
#   for j in range(6):
#      ...

# square all the numbers in L
def square(L):
   squaresList = []

   for number in L:
      if number % 2 == 0:
         squaresList.append(number * number)

   return squaresList

evenSquares = [x*x for x in L if x % 2 == 0]


if __name__ == "__main__":
   print("JUMP FOR JOY")
