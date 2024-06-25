class Details:
    def __init__(self,name,age): 
        self.name = name
        self.age = age

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details("Soutam",18)
obj1.desc()