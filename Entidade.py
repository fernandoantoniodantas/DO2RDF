#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:41:22 2019

@author: Fernando
@author: Hermann

Classe que implementa uma Entidade (órgão público).

"""

class Entidade():
   
   @property
   def id(self):
       return self.__id
 
   @id.setter
   def id(self, id):
       self.__id = id    
    
   @property
   def descricao(self):
       return self.__descricao
   
   @descricao.setter
   def descricao(self, descricao):
       self.__descricao = descricao
       
   @property
   def esfera(self):
       return self.__esfera
 
   @esfera.setter
   def esfera(self, esfera):
       self.__esfera = esfera
       
       
       