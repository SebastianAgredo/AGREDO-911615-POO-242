class Person:
    def __init__(self, dni, name, lastname, age):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.age = age

class Student(Person):
    def __init__(self, dni, name, lastname, age, code):
        super().__init__(dni, name, lastname, age)
        self.code = code
        self.__subjects = [] 

    def __str__(self):
        return f"Nombre: {self.name}, Código: {self.code}, Asignaturas: {', '.join(self.__subjects) if self.__subjects else 'Sin asignaturas'}"

 
    def add_subject(self, subject):
        self.__subjects.append(subject)

class Professor(Person):
    def __init__(self, dni, name, lastname, age, device, desktop):
        super().__init__(dni, name, lastname, age)
        self.device = device
        self.desktop = desktop

    def __str__(self):
        return f"Nombre: {self.name}, Dispositivo: {self.device}, Puesto de trabajo: {self.desktop}"

student_1 = Student(1006073732, 'Sebastian', 'Agredo Sánchez', 23, 911615)


student_1.add_subject('Matemáticas')


print(student_1)
