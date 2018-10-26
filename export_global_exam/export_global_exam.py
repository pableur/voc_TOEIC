# -*- coding: utf-8 -*-
 
 # import libraries
import urllib2
from bs4 import BeautifulSoup
import os

# specify the url
#quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
#quote_page = 'file:///C:/Users/HTI/Desktop/TOEIC_Vocabulaire.htm'
urls=[]
"""
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-appels')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-les-ordinateurs')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-achats-et-ventes')

urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-droit-fiscalite')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-lentreprise-et-le-produit')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-gestion-de-lentreprise')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-la-commercialisation-et-la-publicite')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-ressources-humaines')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-la-vie-dentreprise')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-banque-finances')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-le-logement-et-les-biens-immobiliers')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-lusine')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-le-paiement')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-les-voyages-daffaires')
"""
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-les-loisirs')

#urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-manger-dehors')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-la-sante')
"""
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-la-meteo')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-la-conduite')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-les-industries')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-shopping')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-la-vie-etudiante')
"""
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-le-mouvement-vert')
urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-les-fetes')
#urls.append('https://global-exam.com/fr/blog/toeic/vocabulaire/toeic-vocabulaire-la-conduite-et-les-conditions-sur-la-route')

hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Encoding': 'windows-1259',
			'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
			'Connection': 'keep-alive'}

for quote_page in urls:
	print "extract from "+quote_page
	file = open(quote_page.split('/')[-1].split('.')[0]+".csv", "w")
	
	req = urllib2.Request(quote_page)
	
	#req.add_header('Referer', 'http://www.python.org/')
	# Customize the default User-Agent header value:
	for val in hdr:
		req.add_header(val,hdr[val])

	#print req.header_items()
	# query the website and return the html to the variable ‘page’
	page = urllib2.urlopen(req)
	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')
	#print soup
	# Take out the <div> of name and get its value
	table_data = soup.find('div',attrs={'class':'section-description'}).find('table')

	lignes= table_data.findAll('tr')

	for ligne in lignes:
		values=ligne.findAll('td')
		#print values[0].text[1:-1]+" : "+values[1].text[1:-1]
		if len(values)>=2:
			file.write( (values[0].text[1:-1].replace(';',',')+";"+values[1].text[1:-1].replace(';',',')+'\n').encode('utf8') )
		
		
	file.close()
