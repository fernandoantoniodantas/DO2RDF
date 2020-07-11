#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 08:35:01 2020

@author: Fernando
@author: Hermann

Esta classe implementa os componentes de uma comissão. Comissões são grupos de trabalho 
responsáveis por executar uma determinada atividade temporária.
"""

from Ato import Ato

class Comissoes(Ato):
    
    @property    
    def nomeComissao(self): #getter
        return self.__nomeComissao
        
    @nomeComissao.setter
    def nomeComissao(self, nomeComissao): #setter
        self.__nomeComissao = nomeComissao

    @property    
    def validade(self): #getter
        return self.__validade
        
    @validade.setter
    def validade(self, validade): #setter
        self.__validade = validade

    @property    
    def convenio(self): #getter
        return self.__convenio
        
    @convenio.setter
    def convenio(self, convenio): #setter
        self.__convenio = convenio
        
        
    @property    
    def orgao(self): #getter
        return self.__orgao
        
    @orgao.setter
    def orgao(self, orgao): #setter
        self.__orgao = orgao
        