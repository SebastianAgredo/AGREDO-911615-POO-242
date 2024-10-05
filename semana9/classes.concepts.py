# class Person:
#     def __init__(self, name, lastName, age):
#         self.name = name
#         self.lastName = lastName
#         self.age = age
#         self.isMarriedWith = None
#         self.nationality = None



#     # def __repr__(self):
#     #     return f"Person(name={self.name}, lastName={self.lastName}, age = {self.age}, spouse={self.isMarriedWith}, nationality={self.nationality})"

#     def __str__(self):
#         return f"name={self.name}, spose={self.isMarriedWith.name}"


#     def get_married(self, person: 'Person'):
#         self.isMarriedWith = person
#         person.isMarriedWith = self



# person_1= Person(name='James', lastName='Rodriguez', age='33')
# person_2=Person(name='Luis', lastName='Diaz',age=25)
# person_3=Person(name='Catalina', lastName='Diaz',age=40)

# person_1.get_married(person_3)
# person_3.get_married(person_1)

# print(person_1)
# print(person_3)


# #por medio de una instacia punto lo que necesito

class Person:
    def __init__(self, name, lastName, age):
        self.__name = name
        self.__lastName = lastName
        self.__age = age

    def get_name(self):
        return self.__name

     def set_name(self,name):
        self.__name=name

    def get_lastName(self):
        return self.__lastName

    def set_lastName(self,lastName):
        self.__lastName=lastName

     def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

    def __repr__(self):
        return f"name={self.get_name()}, lastName={self.get_lastName()}, age={self.__age}"




person_1= Person(name='James', lastName='Rodriguez', age=33)
person_2= Person(name='Luis', lastName='Diaz',age=25)
person_3= Person(name='Catalina', lastName='Diaz',age=40)

person_1.set_age(30)

print(person_1)


#por medio de una instacia punto lo que necesito

