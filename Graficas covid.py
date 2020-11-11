# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:51:37 2020

@author: Bryan Cuellar Moran
"""
from matplotlib import pyplot
from math import*
from numpy import*

Datos=["Coahuila","Nuevo Leon","CDMX","Totales"]
Muertes=[1938,2935,9479,14352]
colores=["blue","green","red","gray"]
Contagios=[19380,29305,94790,143520]
pyplot.title('Representacion de las muertes generadas por el Covid en tres estados')
pyplot.ylabel('MuertesxCovid')
pyplot.xlabel("Estados")
pyplot.grid()
pyplot.bar(Datos, height=Muertes, color=colores, width=0.5)
pyplot.show()

