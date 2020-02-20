class Library:
    def __init__(self, books, signupTime, shipping):
        self.books = books
        self.signupTime = signupTime
        self.shipping = shipping


# Leer archivo
f = open('a_example.txt')
read = f.read()
array = read.split("\n")

diffBooks = array[0].split()[0]
numLibraries = array[0].split()[1]
numDays = array[0].split()[2]
score = array[1]

for i in range(0, numLibraries - 1):
