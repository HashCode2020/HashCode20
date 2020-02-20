class Library:
    def __init__(self, numBooks, signupTime, shipping, books):
        self.numBooks = numBooks
        self.signupTime = signupTime
        self.shipping = shipping
        self.books = books

    def __str__(self) -> str:
        return "Libros {0} tiempo registro {1} tiempo envio {2} libros {3}".format(self.numBooks, self.signupTime,
                                                                                   self.shipping, len(self.books))
class Book:
    def __init__(self, id, puntos):
        self.id = id
        self.puntos = puntos

    def __str__(self) -> str:
        return "Libro {0}: {1}".format(self.id, self.puntos)

# librerias: Array de librerias
# diasMax: Dias restantes para escanear libros
# return: devulve la libreria con mayor puntos/dia
def mejorBiblioteca(bibliotecas, diasMax):
    puntosMax = 0;
    mejorBiblio = 0;
    for biblio in bibliotecas:
        puntos = puntosPotencialesConsigueLibreria(biblio, diasMax)
        if puntosMax < puntos:
            puntosMAx = puntos
            mejor_biblio = biblio;

    return mejorBiblio





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

diffBooks = int(array[0].split()[0])
numLibraries = int(array[0].split()[1])
numDays = int(array[0].split()[2])
score = array[1]
array = array[2:]
libraries = []

for i in range(0, numLibraries+1, +2):
    numBooks = array[i].split()[0]
    signupTime = array[i].split()[1]
    shipping = array[i].split()[2]
    books = array[(i + 1)]
    lista_books = []

    for book in books:
        if book != ' ':
            lista_books.append(Book(int(book), score[int(book)-1]))

    libraries.append(Library(numBooks, signupTime, shipping, lista_books))

for i in libraries:
    print("{0}\r\n".format(i))
