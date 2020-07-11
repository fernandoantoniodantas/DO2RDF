"""
Created on Sat Dec 18 14:30 2019

@@author: Fernando
@author: Hermann

Script que faz o download dos diários oficiais (PDFs) da prefeitura do Rio de Janeiro.
Este script segue a seguinte regra:
* Primeiro de janeiro de 2013 (contador em 1963)
* dia 27/02/2020 (contador em 4455)

"""


from pathlib import Path
import requests


counter = 4456
while counter < 4600:
    print(counter)    
    filename = Path('pdfFinal/'+str(counter)+'.'+'pdf')
    print(filename)
    url = 'http://doweb.rio.rj.gov.br/portal/edicoes/download/'+str(counter)
    print(url)
    response = requests.get(url)
    filename.write_bytes(response.content)
    counter = counter + 1