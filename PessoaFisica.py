#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:58:28 2019

@author: Fernando
@author: Hermann

Classe que implementa uma pessoa física. Herda caractísticas de Pessoa.
Classe implementa operações get e set.
"""

from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    
   #def __init__(self, CPF, nome, dataNascimento):
   #    super().__init__(nome)
   #    self.CPF = CPF
   #    self.dataNascimento = dataNascimento
    
   @property
   def CPF(self):
       return self.__CPF
   
   @CPF.setter 
   def CPF(self, CPF):
       self.__CPF = CPF
       
   @property
   def dataNascimento(self):
       return self__.dataNascimento
    
   @dataNascimento.setter
   def dataNascimento(self, dataNascimento):
       self.__dataNascimento = dataNascimento
              
       
           