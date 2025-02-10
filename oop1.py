class Person:
    def __init__ (self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age


    def detail(self):
            print(self.name,"is a",self.gender)

teacher = person("Joe","Male")
teacher.detail()

accountant = person()
accountant.detail()
print(accountant.name)
