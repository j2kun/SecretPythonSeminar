class Profile:
   pi = 3.14

   def __init__(self, theName, myAge):                                    
      self.name = theName
      self.age = myAge

   def growOlder(self):
      self.age += 1

   def greet(self, language):
      if language=="English":
         return "Greetings, %s" % self.name
      else:
         return "I don't speak freaky deaky dutch!"

   


# bad way
#p = Profile()
#p.age = 22

#with a constructor
# p = Profile() # this now raises an error
p = Profile('Jeremy', 25)
p.growOlder()


p.greet("Dutch")
p.pi
