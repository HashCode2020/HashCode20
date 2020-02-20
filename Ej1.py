class Library:
    def __init__(self, books, signupTime, shipping):
        self.books = books
        self.signupTime = signupTime
        self.shipping = shipping



#Funcion que define los puntos que puede conseguir una libreria en funcion de los dias que quedan
def puntosPotencialesConsigueLibreria(libreria, diasDisponibles):
    diasDisponiblesDespuesRegistro = diasDisponibles - libreria.signupTime
    puntuacion = 0
    libroSeleccionado = 0

    #mientras queden dias para registrar libros, se cogen los libros y se registran aumentando la puntuacion
    while(diasDisponiblesDespuesRegistro > 0):
        librosDisponiblesDia = libreria.shipping

        while(librosDisponiblesDia > 0):
            puntuacion += libreria.books[libroSeleccionado]
            libroSeleccionado += 1
            librosDisponiblesDia -= 1

        diasDisponiblesDespuesRegistro -= 1

    return puntuacion


# Leer archivo
f = open('a_example.txt')
read = f.read()
array = read.split("\n")

diffBooks = array[0].split()[0]
numLibraries = array[0].split()[1]
numDays = array[0].split()[2]
score = array[1]

for i in range(0, numLibraries - 1):
