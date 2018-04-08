##Scrapping web
from conn_conf import client
import bs4, requests, re

''' Inicialización de variables'''
noticias = []

'''Conexión a la BBDD'''
db = client.proyecto_sinf
colArticulos = db.noticias

'''URL fuente'''
url_base = "https://elpais.com"
url_internacional = "/internacional/"
regex = re.compile(r'//elpais.com')

print('---------Inicio descarga de datos---------\n\n')

req = requests.get(url_base+url_internacional)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text, "html.parser")

articulos = soup.select('div .articulo__interior')
for articulo in articulos:
	titulo = articulo.select('.articulo-titulo')[0]
	
	#Titular de la noticia
	titular = titulo.getText()
	print('Titular: '+titulo.getText())	

	#Enlace a la noticia e id de la misma
	enlace = titulo.select('a')[0].get('href')
	if not enlace.startswith('/internacional/'): 
		enlace = regex.sub('', enlace)
	print('Enlace a la noticia: '+enlace)

	#Fecha de la noticia
	fecha = articulo.select('meta[itemprop=datePublished]')[0].get('content').split('T')[0]

	#Cuerpo de la noticia
	reqNoticia = requests.get(url_base+enlace)
	req.raise_for_status()
	soupNoticia = bs4.BeautifulSoup(reqNoticia.text, "html.parser")
	parrafos = soupNoticia.select('#cuerpo_noticia p')
	cuerpo = ""
	for parrafo in parrafos:
		cuerpo = cuerpo + parrafo.getText()

	print('Cuerpo de la noticia: '+ cuerpo[:25]+'[...]')

	if not cuerpo == "" :
		noticia = {
			'diario' : 'elpais',
			'titular' : titular, 
			'item_id' : enlace, 
			'cuerpo' : cuerpo, 
			'fecha' : fecha, 
			'n_analisis' : 0, 
			'pais_resultado' : ""
		}
		noticias.append(noticia)

print('\n\n ---------Fin descarga de datos---------')

numNoticias = len(noticias)
i = 0
for noticia in noticias: 
	if colArticulos.find({"item_id": noticia['item_id'] }).count() == 0 :
		colArticulos.insert_one(noticia)
		i = i + 1
		
print('Insertadas '+str(i)+' de '+str(numNoticias)+' noticias descargadas. ')
print('\n\n ---------Fin la inserción de datos---------')








