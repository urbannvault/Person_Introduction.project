class Person():
    def __init__(self, name, age, gender):
        self.name=name 
        self.age= age 
        self.gender= gender
        
    def introduce(self):
        print(f"Hello my name is {self.name}. I'm {self.age} years old and I'm {self.gender}")
        
person1=Person("Innocent", 28, "male")
person1.introduce()

person2=Person("Jessicah", 21, "female")
person2.introduce() 