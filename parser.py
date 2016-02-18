#!/usr/bin/python
# -*- coding: utf-8 -*-


from urllib2 import urlopen
import bs4 as BeautifulSoup
import re
import time
import os

MyFile = "result.csv"
if os.path.isfile(MyFile):
        os.remove(MyFile)
text_file = open(MyFile, "a")  

with open("db/url.txt","r") as file:
    for line in file:
	cat = titre = pays = prix = region = sousregion = appellation = designation = classification = producteur = couleur = alcool = sucre = ""
        url  = line.rstrip('\n')
	prix = 0
        html = urlopen(url)
        soup = BeautifulSoup.BeautifulSoup(html)
        titre = soup.findAll('h1',attrs={"class":"product-description-title"})[0].get_text().replace('\n','').encode('utf-8').strip()
        prix = re.findall('\d+\,\d+', soup.findAll('p',attrs={"class":"price"})[0].get_text().encode('utf-8').strip())[0].replace(',','.')
        cat = url.split("/")[6]      
        for detail in soup.findAll('div',attrs={"id":"details"}):
            subs = detail.__str__()
	    subsoup = BeautifulSoup.BeautifulSoup(subs)

	    for li in subsoup.findAll('li'):
		desc = li.findAll('div',attrs={"class":"left"})[0].get_text().encode('utf-8').strip()
		data = li.findAll('div',attrs={"class":"right"})[0].get_text().encode('utf-8').strip()

		if(desc == "Pays" ):
			pays = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();	
		if(desc == "Région" ):
			region = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();	
		if(desc == "Sous-région" ):
			sousregion = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();	
		if(desc == "Appellation" ):
			appellation = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();	
		if(desc == "Classification" ):
			classification = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();	
		if(desc == "Désignation réglementée" ):
			designation = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();	
		if(desc == "Producteur" ):
			producteur = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();
			producteur = producteur.replace('Tous les produits de ce producteur','')
		if(desc == "couleur" ):
			couleur = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();	
		if(desc == "Degré d'alcool" ):
			alcool = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();
			#alcool = re.findall('\d+\,\d+',alcool)
		if(desc == "Taux de sucre" ):
			sucre = li.findAll('div',attrs={"class":"right"})[0].get_text().replace('\n','').encode('utf-8').strip();	


        text_file.write("\"\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"\"\n" % (url,cat,titre,prix,pays,region,sousregion,appellation,designation,classification,producteur,couleur,alcool,sucre))

	print "\"\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"\"" % (url,cat,titre,prix,pays,region,sousregion,appellation,designation,classification,producteur,couleur,alcool,sucre)
	time.sleep(1)

text_file.close()	
