from conn_conf import client
db = client.proyecto_sinf
col = db.countries

file = open('allCountries.txt')

inserciones = 0
countries = []

print('Dividiendo el fichero en un array de líneas')
lineas = file.readlines()
print('OK')

print('Insertando en la bbdd')
for linea in lineas : 
	linea = linea.split('\t')
	country = {
		'geonameid': linea[0],
		'name': linea[1],
		'ansiname': linea[2],
		'alternatenames': linea[3],
		'latitude': linea[4],
		'longitude': linea[5],
		'feature_class': linea[6],
		'feature_code': linea[7],
		'country_code': linea[8],
		'cc2': linea[9],
		'admin1_code': linea[10],
		'admin2_code': linea[11],
		'admin3_code': linea[12],
		'admin4_code': linea[13],
		'population': linea[14],
		'elevation': linea[15],
		'gtopo30': linea[16],
		'timezone': linea[17],
		'modification_date': linea[18]
	}	
	inserciones = inserciones + 1
	col.insert_one(country)
	country = {}
print('OK')

print('Cantidad de registros insertados: ' + str(inserciones) )

print('\n\n\nFIN DEL PROGRAMA')
