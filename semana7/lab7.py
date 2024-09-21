def class_person(name, lastname, id, age, role)
    return {
        "name": name,
        "lastname": lastname,
        "id": id,
        "role": role
    }

def show_object(object_)
    print(object_)

def add_person():
    name = input("Digite su nombre:\n")
    lastname = input("Digite su apellido:\n")
    id = input(int("Digite su id:\n"))
    age = input(int("Digite su edad:\n"))
    role = input(int("Digite su rol:\n"))

# Agregar personas a la lista
# Usar un bucle para agregar hasta el usuario
# Imprimir el contenido listado