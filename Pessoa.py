#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:52:22 2019

@author: Fernando
@author: Hermann

Classe para definiação de uma Pessoa. 
Classe implementa operações get e set.
"""

class Pessoa:

    #def __init__ (self, nome):
    #    self.nome = nome

    @property    
    def nome(self): #getter
        return self.__nome
        
    @nome.setter
    def nome(self, nome): #setter
        self.__nome = nome
        
        
        
        