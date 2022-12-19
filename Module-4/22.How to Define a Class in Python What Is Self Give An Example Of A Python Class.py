class Python :

    Name = input ("Enter Your Name :- ")

    school = input ("Enter Your school name :- ")
 
    def printdata (self):
        print (f"Your School name is {self.school}")

 
pt = Python ()

print(f"Your name is :{pt.Name}")
pt.printdata()