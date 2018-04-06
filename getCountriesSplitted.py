file = open('allCountries.txt')

print('Dividiendo el fichero en un array de líneas')
lineas = file.readlines()
print('OK')

countries = {}

print('Leyendo lineas')
for linea in lineas : 
	linea = linea.split('\t')

	
	feature_code = linea[7]
	if feature_code == 'ADM2': 
		alternatenames = linea[3].split(',')

		for alternatename in alternatenames: 
			if len(alternatename) == 0:
				alternatenames.remove(alternatename)
			else:
				for letter in alternatename:
					if (ord(letter)>128):
						alternatenames.remove(alternatename)
						break

		country_code = linea[8]
		if country_code in countries: 
			alternatenames_list = countries[country_code] + alternatenames
		else: 
			alternatenames_list = alternatenames
		
		countries[country_code] = alternatenames_list

print('OK')

fichero = open('entrenamiento.csv', 'w')
print('Escribiendo el csv')
for cc in countries.keys(): 
	pais = str(countries[cc]).replace(',', '') + ', /' + cc +'\n'
	fichero.write(pais)
print('OK')


print('\n\n\nFIN DEL PROGRAMA')