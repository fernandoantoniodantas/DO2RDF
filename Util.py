#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:54:24 2019

@author: Fernando
@author: Hermann

Esta classe atribui valores numéricos (parser) às informações do tipo string do diário oficial.
"""

class Util():
    
    def retornaMes(self, mes):
       
        if mes == 'JANEIRO' or mes == 'janeiro' or mes == 'Janeiro' :
            return '01'
            pass
        if mes == 'FEVEREIRO' or mes == 'fevereiro' or mes == 'Fevereiro':
            return '02'
            pass
        if ((mes == 'MARÇO') or (mes == 'março') or (mes == 'Março')):
            return '03'
            pass
        if mes == 'ABRIL' or mes == 'abril' or mes == 'Abril':
            return '04'
            pass
        if mes == 'MAIO' or mes == 'maio' or mes == 'Maio':
            return '05'
            pass
        if mes == 'JUNHO' or mes == 'junho' or mes == 'Junho':
            return '06'
            pass
        if mes == 'JULHO' or mes == 'julho' or mes == 'Julho':
            return '07'
            pass
        if mes == 'AGOSTO' or mes == 'agosto' or mes == 'Agosto':
            return '08'
            pass
        if mes == 'SETEMBRO' or mes == 'setembro' or mes == 'Setembro':
            return '09'
            pass
        if mes == 'OUTUBRO' or mes == 'outubro' or mes == 'Outubro':
            return '10'
            pass
        if mes == 'NOVEMBRO' or mes == 'novembro' or mes == 'Novembro':
            return '11'
            pass
        if mes == 'DEZEMBRO' or mes == 'dezembro' or mes == 'Dezembro':
            return '12'
            pass
        else:
            return 'XX'
            pass
    
    def retornaAcao(self, acao):
        if acao == 'NOMEAR':
            return 1
            pass
        if acao == 'EXONERAR':
            return 2
            pass
        else:
            return 9
            pass    
        
    def converteRomano(self, valor):
        if valor == 'XXVI':
            return 26
            pass
        if valor == 'XXVII':
            return 27
            pass
        if valor == 'XXVIII':
            return 28
            pass
        if valor == 'XXIX':
            return 29
            pass
        if valor == 'XXX':
            return 30
            pass
        if valor == 'XXXI':
            return 31
            pass
        if valor == 'XXXII':
            return 32
            pass
        if valor == 'XXXIII':
            return 33
            pass
        if valor == 'XXXIV':
            return 34
            pass
        if valor == 'XXXV':
            return 35
            pass
        if valor == 'XXXVI':
            return 36
            pass
        else:
            return 999999999
            pass    
                
        
 