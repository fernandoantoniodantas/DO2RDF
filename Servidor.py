#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:52:22 2019

@author: Fernando
@author: Hermann
Classe que implementa um servidor público. Herda de PessoaFísica.
Classe implementa operações get e set.
"""


from PessoaFisica import PessoaFisica

class Servidor(PessoaFisica):
    
   
   @property
   def matricula(self):
       return self.__matricula
 
   @matricula.setter
   def matricula(self, matricula):
       self.__matricula = matricula         
        
   @property
   def cargo(self):
       return self.__cargo
 
   @cargo.setter
   def cargo(self, cargo):
       self.__cargo = cargo         
        
   @property
   def simbolo(self):
       return self.__simbolo
 
   @simbolo.setter
   def simbolo(self, simbolo):
       self.__simbolo = simbolo        

   @property
   def tipocargo(self):
       return self.__tipocargo
 
   @tipocargo.setter
   def tipocargo(self, tipocargo):
       self.__tipocargo = tipocargo         