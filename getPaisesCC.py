##Scrapping web
from conn_conf import client
import bs4, requests, re


''' Inicialización de variables'''
listaPaises = []

'''Conexión a la BBDD'''
db = client.proyecto_sinf
paises = db.paises


'''URL fuente'''
url_base = "http://utils.mucattu.com/iso_3166-1.html"

print('---------Inicio descarga de datos---------\n\n')

req = requests.get(url_base)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text, "html.parser")

rows = soup.select('#table2 tr')
for row in rows:
	#Obtener fila
	fila = row.select('td')
	alfa2 = fila[0].getText()
	nombrePais = fila[1].getText()
	numerico = fila[2].getText()
	alfa3 = fila[3].getText()

	pais = {
		'alfa2':		alfa2, 
		'nombrePais': 	nombrePais, 
		'numerico': 	numerico, 
		'alfa3': 		alfa3
	}

	listaPaises.append(pais)

print('\n\n ---------Fin descarga de datos---------')

numPaises = len(listaPaises)
i = 1
for pais in listaPaises: 
	print('Insertando '+str(i)+' de '+str(numPaises)+' países...')
	paises.insert_one(pais)
	i = i + 1










