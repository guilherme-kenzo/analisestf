#!/usr/bin/env python
import csv
import random
import urllib
import sys
# import re
# from collections import defaultdict
import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

list = []


url = 'http://redir.stf.jus.br/paginadorpub/paginador.jsp?docTP=AC&docID='
arg1 = sys.argv[1]
metaList = []

if arg1 == '--help':
    print('Escreva o diretorio para download',
          ' em que serao armazenados os documentos')
    exit()

def getRandomList(listSize,init, end):
    for i in range(1, listSize):          # Creates random list from 821 to 600000
        randInt = random.randint(init, end)
        list.append(randInt)


getRandomList(300, 800, 62000)


def metadataColector(a):
    parser.set_document(a)
    pdfMetaData = doc.info[0]
    return pdfMetaData['Title']

def returnMetaTuple(whichStr):
    for i in metaList:
        if i == whichStr:
            print i

for file in list:               # iterates over random list to download files
    print file
    fileStr = str(file)
    pdfName = fileStr + '.pdf'
    try:
        fileName, header = urllib.urlretrieve(url + fileStr, arg1 + pdfName)
        print('Downloading ' + fileName)
    except:
        print("Download Problem - aborting download")
        break
    # print(header)               

    parser = PDFParser(open(arg1 + pdfName, 'rb'))
    doc = PDFDocument(parser)
    pdfTitle = metadataColector(doc)

    metaList += [(fileStr, pdfTitle)]

    with open('file.csv', 'w') as op:
        a = csv.writer(op, delimiter=', ',
        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data = metaList
        a.writerows(data)

print metaList[0]
