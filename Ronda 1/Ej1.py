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

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id

    def __str__(self) -> str:
        return "Libro {0}: {1}".format(self.id, self.puntos)



# librerias: Array de librerias
# diasMax: Dias restantes para escanear libros
# return: devulve la libreria con mayor puntos/dia
def mejorBiblioteca(bibliotecas, diasMax, poolLibros):
    puntosMax = 0
    puntos=0
    for biblio in bibliotecas:
        puntos = puntosPotencialesConsigueLibreria(biblio, diasMax, poolLibros)
        if puntosMax <= puntos:
            puntosMax = puntos
            mejor_biblio = biblio
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
    f.write(toWrite)
    f.close()


# Funcion que define los puntos que puede conseguir una libreria en funcion de los dias que quedan
def puntosPotencialesConsigueLibreria(libreria, diasDisponibles, poolLibros):
    poolInterno = set(poolLibros)
    diasDisponiblesDespuesRegistro = diasDisponibles - libreria.signupTime
    puntuacion = 0
    libroSeleccionado = 0

    quedanLibros = False
    #comprobar que queden libros de la biblioteca en el pool
    for libro in libreria.books:
        if libro in poolInterno:
            quedanLibros = True
    #quedanLibros = libreria.books in poolInterno

    # mientras queden dias para registrar libros, se cogen los libros y se registran aumentando la puntuacion
    while (diasDisponiblesDespuesRegistro > 0 and quedanLibros):
        librosDisponiblesDia = libreria.shipping

        while (librosDisponiblesDia > 0 and quedanLibros):

            if(libreria.books[libroSeleccionado] in poolInterno):
                puntuacion += int(libreria.books[libroSeleccionado].puntos)
                poolInterno.remove(libreria.books[libroSeleccionado])
                if libroSeleccionado < libreria.numBooks - 1:
                    libroSeleccionado += 1
                librosDisponiblesDia -= 1

            quedanLibros = False
            for libro in libreria.books:
                if libro in poolInterno:
                    quedanLibros = True

        diasDisponiblesDespuesRegistro -= 1


    return puntuacion


def escogeLibros(libreria, diasDisponibles,poolLibros):
    librosSeleccionados = []
    diasDisponiblesDespuesRegistro = diasDisponibles - libreria.signupTime
    libroSeleccionado = 0

    while (diasDisponiblesDespuesRegistro > 0):
        librosDisponiblesDia = libreria.shipping

        while (librosDisponiblesDia > 0 and libroSeleccionado < libreria.numBooks - 1 and libreria.books[libroSeleccionado] in poolLibros):
            librosSeleccionados.append(libreria.books[libroSeleccionado])
            poolLibros.discard(libreria.books[libroSeleccionado])
            libroSeleccionado += 1

            librosDisponiblesDia -= 1

        diasDisponiblesDespuesRegistro -= 1
    return librosSeleccionados


# Leer archivo
f = open('d_tough_choices.txt')
read = f.read()
array = read.split("\n")

diffBooks = int(array[0].split()[0])
numLibraries = int(array[0].split()[1])
numDays = int(array[0].split()[2])
score = array[1].split()
array = array[2:]
libraries = []
idCutreParaBibliotecas = 0
poolLibros = set()

for i in range(0, numLibraries + 1, +2):
    numBooks = array[i].split()[0]
    signupTime = array[i].split()[1]
    shipping = array[i].split()[2]
    books = array[(i + 1)].split()
    #print(books)
    lista_books = []

    for book in books:
        libro = Book(int(book), score[int(book) - 1])
        lista_books.append(libro)
        poolLibros.add(libro)

    #poolLibros.update(lista_books)
    lista_books.sort(reverse=True)
    libraries.append(Library(idCutreParaBibliotecas, numBooks, signupTime, shipping, lista_books))
    idCutreParaBibliotecas = idCutreParaBibliotecas + 1

#print(poolLibros)

###MAIN

libreriasOrdenadas = []
resultado = []

while numDays > 0 and len(libraries) > 0:
    libreriaEscogida = mejorBiblioteca(libraries, numDays,poolLibros)
    librosEscogidos = escogeLibros(libreriaEscogida, numDays,poolLibros)
    print(poolLibros)

    libreriasResultado = Library(libreriaEscogida.id, len(librosEscogidos), libreriaEscogida.signupTime,
                                 libreriaEscogida.shipping, librosEscogidos)

    resultado.append(libreriasResultado)
    # eliminamos lo que escogimos

    #print(libraries)

    libraries.remove(libreriaEscogida)
    numDays -= libreriaEscogida.signupTime


printToFile(resultado)
