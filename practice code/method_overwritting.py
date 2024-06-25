# class student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def info(self):
#         print(f"The name of the student is {self.name} and ID is {self.id}")
# class teacher(student):
#     def __init__(self,name,id,subject):
#         self.subject=subject
#         super().__init__(name,id)
#     def info(self):
#         print(f"The name of the student is {self.name} and ID is {self.id} and the teaching subject is {self.subject}")

# s1=student("soutam",17)
# s1.info()
# t1=teacher("Teacher",61,"math")
# t1.info()

class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
      return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
    #   self.radius = radius
      super().__init__(radius, radius)

    def area(self):
        return 3.14 *  super().area()
      
# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())
