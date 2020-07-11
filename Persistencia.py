#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:41:26 2020

@author: Fernando
@author: Hermann

Esta classe é responsável por inserir os dados no Banco de Dados.
Módulos Importados:  
import psycopg2 # para o PostgreSQL
from UtilRegex import UtilRegex

Obs.: O dado "Matrícula" está com replace 'X' por não existir a consistencia desta informação nos atos do diário.
"""
import psycopg2 # para o PostgreSQL
from UtilRegex import UtilRegex

####### Database

class Persistencia():
    
    def insert(self, matricula, nome, dataResolucao, acao, dataEfeito, cargo, tipocargo, simbolo):
        matricula = matricula.replace('XXXXXXXXXXX', '')
        #dataEfeito = dataEfeito.replace('XX/XX/XXXX', '01/01/9999')
        simbolo = simbolo.replace('XXXX', '')
        utilreg = UtilRegex()
        dataResolucao = utilreg.converteData(dataResolucao)
        dataEfeito = utilreg.converteData(dataEfeito) 
        

        conn = psycopg2.connect(host='localhost', database='diario', user='postgres', password='020573')
        cur = conn.cursor()
        cur.execute("INSERT INTO dorj.atos (matricula, nome, datapublicacao, acao, dataefeito, cargo, tipocargo, simbolo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (matricula, nome, dataResolucao, acao, dataEfeito, cargo, tipocargo, simbolo))
        conn.commit()
        cur.close()
        conn.close()