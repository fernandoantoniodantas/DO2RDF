#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:32:58 2020

@author: Fernando
@author: Hermann


Classe que implementa os componentes de um ato público.
"""
from Servidor import Servidor

class Ato(Servidor):
    
        
   # def __init__(self, nome, numero):
   #    super().__init__(nome)
   #    self.numero = numero

    @property    
    def numero(self): #getter
        return self.__numero
        
    @numero.setter
    def numero(self, numero): #setter
        self.__numero = numero
        
    @property    
    def diaResolucao(self): #getter
        return self.__diaResolucao
        
    @diaResolucao.setter
    def diaResolucao(self, diaResolucao): #setter
        self.__diaResolucao = diaResolucao
        
    @property    
    def mesResolucao(self): #getter
        return self.__mesResolucao
        
    @mesResolucao.setter
    def mesResolucao(self, mesResolucao): #setter
        self.__mesResolucao = mesResolucao

    @property    
    def anoResolucao(self): #getter
        return self.__anoResolucao
        
    @anoResolucao.setter
    def anoResolucao(self, anoResolucao): #setter
        self.__anoResolucao = anoResolucao        

    @property    
    def dataResolucao(self): #getter
        return self.__dataResolucao
        
    @dataResolucao.setter
    def dataResolucao(self, dataResolucao): #setter
        self.__dataResolucao = dataResolucao


    @property    
    def dia(self): #getter
        return self.__dia
        
    @dia.setter
    def dia(self, dia): #setter
        self.__dia = dia
        
    @property    
    def mes(self): #getter
        return self.__mes
        
    @mes.setter
    def mes(self, mes): #setter
        self.__mes = mes

    @property    
    def ano(self): #getter
        return self.__ano
        
    @ano.setter
    def ano(self, ano): #setter
        self.__ano = ano
        
    @property    
    def dataEfeito(self): #getter
        return self.__dataEfeito
        
    @dataEfeito.setter
    def dataEfeito(self, dataEfeito): #setter
        self.__dataEfeito = dataEfeito