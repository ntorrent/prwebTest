#!/usr/bin/env python3
# -*- coding. utf-8 -*-

from urllib.request import urlopen  # em permet treballar una url com si fos un fitxer (estil open())
import bs4
import json #es part del core de python
import pprint

class ClientWeb(object):
    """Client web per la web de la EPS"""
    def __init__(self):
        super(ClientWeb, self).__init__()
        #pass

    def do_request(self):
        f = urlopen("https://api.openweathermap.org/data/2.5/weather?q=Lleida&units=metric&appid=29a70115e408d4c047827ab2851f7821&mode=json") #"magic number": si canvio enllac cal canviar el codi: no fer-ho ; abans hem utilitzat &mode=xml ; puc afegir &lang=ca
        data = f.read()
        f.close()
        return data
    """
    def process_weather(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        temp = arbre.find("temperature")
        weather = arbre.find("weather")
        print( temp["value"] + " and " + weather["value"] )
        return None
    """

    def process_weather(self, html):
        #dic = xmltodict.parse(html)
        dic = json.loads(html)
        pprint.pprint(dic) # imprimir el diccionari de manera mes entenedora
        """ A ell li surt el que jo en una llista amb la clau 'list'. Potser es perque ho te en catala
        temp = dic['list'][0]['main']['temp']
        weath = dic['list'][0]['weather'][0]['description']
        """
        temp = dic['main']['temp']
        weath = dic['weather'][0]['description']
        return (str(temp)+" and "+str(weath))

    def run(self):
        data = self.do_request()
        data = self. process_weather(data)
        print(data)

if __name__ == "__main__":
    c = ClientWeb()
    c.run()
