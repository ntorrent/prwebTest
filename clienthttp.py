#!/usr/bin/env python
# -*- coding. utf-8 -*-

from urllib.request import urlopen  # em permet treballar una url com si fos un fitxer (estil open())
import bs4

class ClientWeb(object):
    """Client web per la web de la EPS"""
    def __init__(self):
        super(ClientWeb, self).__init__()
        pass

    def descarregar_html(self):
        f = urlopen("http://www.eps.udl.cat/ca/") #"magic number": si canvio enllac cal canviar el codi: no fer-ho
        html = f.read()
        f.close()
        return html

    def buscar_activitats(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        activitats = arbre.find_all("div", "featured-links-item")
        return activitats

    def run(self):
        # amazing UML fet amb comentaris
        # descarregar-me la pagina html
        html = self.descarregar_html()
        # buscar activitats
        # imprimir resultat
        print(self.buscar_activitats(html))

if __name__ == "__main__":
    c = ClientWeb()
    c.run()
