class Rectangle :
 
    Length = float (input ("Enter the Length of Rectangle :- "))
    Width = float (input ("Enter the Width of Rectangle :- "))
 
    def Area_Rectangle (self) :
        Area = self.Length * self.Width
        print ("\nArea of Rectangle is :- ",Area)

Re = Rectangle ()
Re.Area_Rectangle()