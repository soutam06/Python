#Calculate the Area and the Circumference of Circles using OOP
 
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        A =(3.14*pow(self.radius,2))  
        print(f"The Area of is {A}")   
    def Circumfernce(self):
        
        C = '{0:.3f}'.format(3.14*2*self.radius)

        print(f"The Circumference of is {C}")
    
#To make a object Please Pass the value of Radius to the class
c1=Circle(5)
c1.Area()
c1.Circumfernce()