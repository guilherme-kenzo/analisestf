#!/usr/bin/env python
# coding=utf-8

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
# arg1 = sys.argv[1]
metaList = []

try:
    if sys.argv[1] == '--help':
        print('Escreva o diretorio para download',  # por algum motivo está saindo o código e não os caractéres
              ' em que serao armazenados os documentos'
              'e, em seguida, a quantidade de arquivos para download'
              'ex: ./downloadacordao.py ~/Documentos/ 10 - '
              'realiza o download de 10 acórdãos aleatórios para a pasta ~/Documentos/')
        exit()

except IndexError:
    print('Escreva o diretorio para download',
          ' em que serao armazenados os documentos'
          'e, em seguida, a quantidade de arquivos para download'
          'ex: ./downloadacordao.py ~/Documentos/ 10 - '
          'realiza o download de 10 acórdãos aleatórios para a pasta ~/Documentos/')
    exit()

def getRandomList(listSize, initial, end):
    for i in range(1, listSize):          # Creates random list from initial to end
        randInt = random.randint(initial, end)
        list.append(randInt)


getRandomList(sys.argv[2], 800, 62000)


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
