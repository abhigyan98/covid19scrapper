import requests
import bs4
from flask import *
#import numpy as np
import plot
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import matplotlib.pyplot as plt

def test():
    url = "https://www.mohfw.gov.in/"
    htmlData=requests.get(url)
    bs = bs4.BeautifulSoup(htmlData.text,'html.parser')
    tableDiv = bs.find_all("div", class_="data-table table-responsive")[0]
    table = tableDiv.text
    tableList = table.split("\n")

    while "" in tableList: 
        tableList.remove("") 

    mainList = []
    for i in range(0,len(tableList)-1,5):
        testList = []
        testList.append(tableList[i])
        testList.append(tableList[i+1])
        testList.append(tableList[i+2])
        testList.append(tableList[i+3])
        testList.append(tableList[i+4])
        mainList.append(testList)

    #extract heading and delete the last2 list elements of mainlist 
    #which consists of total data and notes
    mainList=mainList[0:len(mainList)-2]
    return mainList

def siteCount():
    url = "https://www.mohfw.gov.in/"
    htmlData=requests.get(url)
    bs = bs4.BeautifulSoup(htmlData.text,'html.parser')
    tableDiv = bs.find_all("div", class_="site-stats-count")[0]
    table = tableDiv.text
    tableList2 = table.split("\n")
    while "" in tableList2: 
        tableList2.remove("") 
    #print(tableList2)
    return tableList2