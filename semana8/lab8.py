from faker import Faker 
fake = Faker()

class Person:
    def __init__(self, dni, name, lastName):  
        self.dni = dni
        self.name = name
        self.lastName = lastName

    def __repr__(self):
        return f"Person (DNI={self.dni}, Nombre={self.name}, Apellido={self.lastName})"

def generate_people(count):
    people = []
    for _ in range(count):
        dni=fake.ssn()
        name=fake.first_name()
        lastName=fake.last_name()
    
        person = Person(dni, name, lastName)
        people.append(person)
    return people

def get_people(people_list):
    for person in people_list:
        print(person)

number=int(input("Por favor ingrese el numero de personas a agregar:\n"))
array_people = generate_people(number)
get_people(array_people)



