class Library:
    def __init__(self, id, numBooks, signupTime, shipping, books):
        self.id = id
        self.numBooks = int(numBooks)
        self.signupTime = int(signupTime)
        self.shipping = int(shipping)
        self.books = books

    def __str__(self) -> str:
        return "Biblio: {0} Libros {1} tiempo registro {2} tiempo envio {3} libros {4}".format(self.id, self.numBooks,
                                                                                               self.signupTime,
                                                                                               self.shipping,
                                                                                               len(self.books))


class Book:
    def __init__(self, id, puntos):
        self.id = id
        self.puntos = int(puntos)

    def __lt__(self, other):
        return self.puntos < other.puntos

    def __gt__(self, other):
        return self.puntos > other.puntos

    def __str__(self) -> str:
        return "Libro {0}: {1}".format(self.id, self.puntos)


# librerias: Array de librerias
# diasMax: Dias restantes para escanear libros
# return: devulve la libreria con mayor puntos/dia
def mejorBiblioteca(bibliotecas, diasMax):
    puntosMax = 0;
    puntos=0
    for biblio in bibliotecas:
        puntos = puntosPotencialesConsigueLibreria(biblio, diasMax)
        if puntosMax <= puntos:
            puntosMax = puntos
            mejor_biblio = biblio;

    return mejor_biblio



#Funcion que define los puntos que puede conseguir una libreria en funcion de los dias que quedan
def printToFile(bibliotecas):
    documento = []
    print("Longitud de bibliotecas es: ", len(bibliotecas))
    documento.append(str(len(bibliotecas)))
    for i in bibliotecas:
        documento.append(str(i.id) + " " + str(len(i.books)))
        strLibros = ""
        for j in i.books:
            strLibros = strLibros + " " + str(j.id)
        documento.append(strLibros[1:])

    f = open("solution1.txt", "w")
    toWrite = str.join("\n", [str(x) for x in documento])
    f.write( toWrite)
    f.close()


# Funcion que define los puntos que puede conseguir una libreria en funcion de los dias que quedan
def puntosPotencialesConsigueLibreria(libreria, diasDisponibles):
    diasDisponiblesDespuesRegistro = diasDisponibles - libreria.signupTime
    puntuacion = 0
    libroSeleccionado = 0

    #mientras queden dias para registrar libros, se cogen los libros y se registran aumentando la puntuacion
    while(diasDisponiblesDespuesRegistro > 0):
        librosDisponiblesDia = libreria.shipping

        while (librosDisponiblesDia > 0):
            puntuacion += int(libreria.books[libroSeleccionado].puntos)
            if libroSeleccionado < libreria.numBooks - 1:
                libroSeleccionado += 1
            librosDisponiblesDia -= 1

        diasDisponiblesDespuesRegistro -= 1

    return puntuacion


def escogeLibros(libreria, diasDisponibles):
    librosSeleccionados=[]
    diasDisponiblesDespuesRegistro = diasDisponibles - libreria.signupTime
    libroSeleccionado = 0

    while (diasDisponiblesDespuesRegistro > 0):
        librosDisponiblesDia = libreria.shipping

        while (librosDisponiblesDia > 0 and libroSeleccionado < libreria.numBooks - 1):
            librosSeleccionados.append(libreria.books[libroSeleccionado])
            libroSeleccionado += 1


            librosDisponiblesDia -= 1

        diasDisponiblesDespuesRegistro -= 1
    return librosSeleccionados


# Leer archivo
f = open('f_libraries_of_the_world.txt')
read = f.read()
array = read.split("\n")

diffBooks = int(array[0].split()[0])
numLibraries = int(array[0].split()[1])
numDays = int(array[0].split()[2])
score = array[1].split()
array = array[2:]
libraries = []
idCutreParaBibliotecas = 0

for i in range(0, numLibraries + 1, +2):
    numBooks = array[i].split()[0]
    signupTime = array[i].split()[1]
    shipping = array[i].split()[2]
    books = array[(i + 1)].split()
    lista_books = []

    for book in books:
        lista_books.append(Book(int(book), score[int(book) - 1]))

    lista_books.sort(reverse=True)
    libraries.append(Library(idCutreParaBibliotecas, numBooks, signupTime, shipping, lista_books))
    idCutreParaBibliotecas = idCutreParaBibliotecas + 1

printToFile(libraries)


###MAIN

libreriasOrdenadas = []
resultado = []

while numDays>0 and len(libraries) > 0:

    libreriaEscogida = mejorBiblioteca(libraries, numDays)
    librosEscogidos = escogeLibros(libreriaEscogida, numDays)


    libreriasResultado = Library(libreriaEscogida.id, len(librosEscogidos), libreriaEscogida.signupTime,
                                 libreriaEscogida.shipping, librosEscogidos)

    resultado.append(libreriasResultado)
    #eliminamos lo que escogimos

    print(libraries)

    libraries.remove(libreriaEscogida)
    numDays -= libreriaEscogida.signupTime




print(libreriasOrdenadas)
printToFile(resultado)
#print(books)
