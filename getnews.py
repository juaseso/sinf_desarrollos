##Scrapping web

import bs4, requests, re
from conn_conf import client


''' Inicialización de variables'''
noticias = []

'''Conexión a la BBDD'''
db = client.proyecto_sinf
articulos = db.noticias

'''URL fuente'''
url_base = "https://elpais.com"
url_internacional = "/internacional/"
regex = re.compile(r'//elpais.com')

print('---------Inicio descarga de datos---------\n\n')

req = requests.get(url_base+url_internacional)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text, "html.parser")

titulos = soup.select('.articulo-titulo')
for titulo in titulos:
	#Titular de la noticia
	titular = titulo.getText()
	print('Titular: '+titulo.getText())	

	#Enlace a la noticia e id de la misma
	enlace = titulo.select('a')[0].get('href')
	if not enlace.startswith('/internacional/'): 
		enlace = regex.sub('', enlace)
	print('Enlace a la noticia: '+enlace)

	#Fecha de la noticia
	fecha = titulo.select

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
			'diario':'elpais',
			'titular':titular, 
			'item_id': enlace, 
			'cuerpo': cuerpo, 
			'fecha': fecha
		}
		noticias.append(noticia)

print('\n\n ---------Fin descarga de datos---------')

numNoticias = len(noticias)
i = 1
for noticia in noticias: 
	print('Insertando '+str(i)+' de '+str(numNoticias)+' noticias...')
	articulos.insert_one(noticia)
	i = i + 1










