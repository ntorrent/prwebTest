#!/usr/bin/env python3
# -*- coding. utf-8 -*-

from urllib.request import urlopen  # em permet treballar una url com si fos un fitxer (estil open())
import bs4

class ClientWeb(object):
    """Client web per la web de la EPS"""
    def __init__(self):
        super(ClientWeb, self).__init__()
        #pass

    def do_request(self):
        f = urlopen("https://api.openweathermap.org/data/2.5/weather?q=Lleida&units=metric&appid=29a70115e408d4c047827ab2851f7821") #"magic number": si canvio enllac cal canviar el codi: no fer-ho
        data = f.read()
        f.close()
        return data

    def process_weather(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        temp = arbre.find("temperature")
        weather = arbre.find("weather")
        print( temp["value"] + " and " + weather["value"] )
        return None

    def run(self):
        data = self.do_request()
        data = self. process_weather(data)

if __name__ == "__main__":
    c = ClientWeb()
    c.run()
