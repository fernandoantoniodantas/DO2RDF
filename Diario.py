#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:19:56 2019

@author: Fernando
@author: Hermann

Classe que herda caracterśiricas de Entidade (órgão público).
Responsável pelas definições de um Diário Oficial.
"""
from Entidade import Entidade

class Diario(Entidade):
    
   # def __init__ (self, nome):
   #     self.data = data
   #     self.esfera = esfera #1-Federal, 2-Estadual, 3-municipal
   #     self.governo = governo #Define o Governo (Estado do Rio de Janeiro)
   
   #Código é uma sequencia presente nos atos do Diário  
   #Ação é referente a "1 - portaria de nomeacao, 2 - portaria de exonercao, 18 - Sem efeito a nomeacao, 28 - Sem efeito a exoneracao"
   
   
   @property
   def ano(self):
       return self.__ano
   
   @ano.setter
   def ano(self, ano):
       self.__ano = ano


   @property
   def codigo(self):
       return self.__codigo
 
   @codigo.setter
   def codigo(self, codigo):
       self.__codigo = codigo   
   


   @property
   def anoromano(self):
       return self.__anoromano
 
   @anoromano.setter
   def anoromano(self, anoromano):
       self.__anoromano = anoromano
 
   @property
   def datadiario(self):
       return self.__datadiario
 
   @datadiario.setter
   def datadiario(self, datadiario):
       self.__datadiario = datadiario
      
   @property
   def tipo(self):
       return self.__tipo
 
   @tipo.setter
   def tipo(self, tipo):
       self.__tipo = tipo
    
   @property
   def arquivo(self):
       return self.__arquivo
 
   @arquivo.setter
   def arquivo(self, arquivo):
       self.__arquivo = arquivo

   @property
   def nomearquivo(self):
       return self.__nomearquivo
 
   @nomearquivo.setter
   def nomearquivo(self, nomearquivo):
       self.__nomearquivo = nomearquivo
   
   @property
   def datagravacao(self):
       return self.__datagravacao
 
   @datagravacao.setter
   def datagravacao(self, datagravacao):
       self.__datagravacao = datagravacao
    