#Leer archivo
f = open('archivo_ejemplo.in')
read = f.read()
array = read.split()

f = open("solution1.txt", "w")
toWrite = str.join(" ", [str(x) for x in array])
f.write(str(len(array)) + "\n" + toWrite)
f.close()