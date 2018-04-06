import shelve

shelfFile = shelve.open('mydata') 
file = open('allCountries.txt')

print('Dividiendo el fichero en un array de líneas')
lineas = file.readlines()
print('OK')

shelfFile['arraylineas'] = lineas

shelfFile.close()
