class Library:
    def __init__(self, numBooks, signupTime, shipping, books):
        self.numBooks = numBooks
        self.signupTime = signupTime
        self.shipping = shipping
        self.books = books

    def __str__(self) -> str:
        return "Libros {0} tiempo registro {1} tiempo envio {2} libros {3}".format(self.numBooks, self.signupTime,
                                                                                   self.shipping, self.books)


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
    libraries.append(Library(numBooks, signupTime, shipping, books))
    print(i)
    print(numLibraries)

for i in libraries:
    print("{0}\r\n".format(i))
