#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:42:31 2019

@author: Fernando
@author: Hermann

Este é o módulo principal do sistema (main). A partie dele os demais módulos são executados. 
É neste a definição do root de armazenamento dos arquivos pdf para leitura do extrator.
Também são gerados 3 arquivos de auditoria: criticas.txt; arqres.txt e cargosXXXX.txt (utilizado para carga na tabela de cargos).
Módulos Importados: 
import os
import os.path
from tika import parser
from RioJaneiroLayoutFinal import RioJaneiroLayoutFinal
from Util import Util
from datetime import datetime
"""

#import xml.etree.ElementTree as et
#import xml.parsers.expat as expat
#from glob import glob
import os
import os.path
#import rdflib
#from rdflib.Graph import Graph
#from rdflib.sparql.bison import Parse
#from rdflib import Namespace, BNode, Literal

from tika import parser
from RioJaneiroLayoutFinal import RioJaneiroLayoutFinal
from Util import Util
from datetime import datetime

#g=rdflib.Graph()
util = Util()

a = []
data_e_hora = datetime.now()
data_e_hora = data_e_hora.strftime('%d/%m/%Y %H:%M:%S')

dataaudit = datetime.now()
dataaudit = dataaudit.strftime('%d-%m-%Y_%H:%M:%S')


audit = 'AUDIT_'+dataaudit+'.txt'

path = "/home/fernando/ProjetosHermann/DO/pdfFinal/copia/"
#path = "D:\Downloads\Fontes python\pdf"

files = []
for _, _, f in os.walk(path):
  for file in sorted(f):
      if '.pdf' in file:
          files.append(os.path.join(file))


criticas = open('criticas.txt', 'w', encoding='UTF-8')
arqres = open('arqres.txt', 'w', encoding='UTF-8')
arq1 = open(audit, 'w', encoding='UTF-8')

qtdarq = len(files)
contarq = 0

for f in files:
    file_data = parser.from_file('pdfFinal/copia/'+f)
    text = file_data['content']
    buffer = text
    contarq = contarq + 1
    perc = ((contarq*100)/qtdarq) 
    
    rio = RioJaneiroLayoutFinal()
    rio.resolucoes(buffer, f, arq1, criticas, contarq, data_e_hora, arqres, round(perc, 2))

arq1.close()


#contarq = 0
#arq2 = open('comissoes.txt', 'w', encoding='UTF-8')
#for f in files:
#    file_data = parser.from_file('pdf/'+f)
#    text = file_data['content']
#    buffer = text
#    contarq = contarq + 1
#    perc = ((contarq*100)/qtdarq) 
    
#    rio = RioJaneiroLayoutFinal()
#    rio.comissoes(buffer, f, arq, contarq, data_e_hora, arqres, round(perc, 2), arq2)

#arq2.close()  


criticas.close()
arqres.close()  























#print(len(a))


#a.sort()

#contador = 3347
#while contador < 4350:
#for _, _, file in os.walk('pdf/'):
#    print('Arq->'+file)


       

#    resol = "RESOLUÇÃO"
    
    #if not open(file, 'rb'):
    #    print("erro")
        #pdf = PdfFileReader(f)
        #information = pdf.getDocumentInfo()
        #number_pages = pdf.getNumPages()
        #print(number_pages)
    
    #if parser.from_file(file):
     #print("ok")
     #Ano XXXIII • N o 46 • Rio de Janeiro
        
#    trailer_pattern = re.compile('Ano\s(\w{3}|\w{4}|\w{5}|\w{6})\s•\sN\w\s(\d{3})')
#    trailer_edicao = trailer_pattern.search(buffer)
#    print("Ano->"+trailer_edicao.group(1))
#    print("Número->"+trailer_edicao.group(2))    
#    header_pattern = re.compile(r'(DECRETO RIO|RESOLUÇÃO)\s“P”\s..\s(\d+)\sDE\s(\d+)\sDE\s([A-Z]+)\sDE\s(\d+)\s*\n')
#    header_resol = header_pattern.search(buffer)        
#    while header_resol: 
#            diario = Diario()
#            print("====== Resol =======")
#             #print("Resolução #"+header_resol.group(1))
#            diario.codigo = header_resol.group(2)
#            print("Resolução -> ...{0}".format(diario.codigo))
#            if header_resol.group(3) and header_resol.group(4) and header_resol.group(5):
           #print("Data "+header_resol.group(2)+" de "+header_resol.group(3)+" de "+header_resol.group(4))
#               diario.dataPublicacao = header_resol.group(3)+"/"+util.retornaMes(header_resol.group(4))+"/"+header_resol.group(5) 
#               print("Data de Publicação -> ...{0}".format(diario.dataPublicacao))
#            else: print("Data invalida")
#            ind_headergestor = header_resol.end()
#            buffer = buffer[ind_headergestor:]
#            header_resol = header_pattern.search(buffer)
    #else: print("Trailer Inválido")
    #ind_headergestor = trailer_edicao.end()
    
#    print(contador)
#    contador = contador + 1
    #except IOError as e:
    #print("I/O error({0}): {1}".format(e.errno, e.strerror))     
