#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:37:12 2019

@author: Fernando
@author: Hermann

Classe utilitária para os padrões Regex.

"""

from Util import Util
import re

class UtilRegex():
    

        
   @property
   def diasSemanas(self):
       return str('(\sQuinta-feira,\s\|\s)')


   def numeroResolucao(self, Detalhe):
       numero_pattern = re.compile(u'(?P<numero>[0-9]+)')
       numeros = numero_pattern.search(Detalhe) 
       if (numeros):
           vlr = numeros.group('numero')
       else: vlr = '00'
       return vlr
   
   def diaResolucao(self, Detalhe):
       dia_pattern = re.compile(u'DE\s*(?P<dia>[0-9]+)\s*DE')
       dia = dia_pattern.search(Detalhe) 
       if (dia):
           vlr = dia.group('dia')
       else: vlr = '00'
       return vlr

   def mesResolucao(self, Detalhe):
       mes_pattern = re.compile(u'DE\s*(?P<mes>JANEIRO|FEVEREIRO|MARÇO|ABRIL|MAIO|JUNHO|JULHO|AGOSTO|SETEMBRO|OUTUBRO|NOVEMBRO|DEZEMBRO)\s*DE')
       mes = mes_pattern.search(Detalhe) 
       if (mes):
           util = Util()
           vlr = mes.group('mes')
           vlr = util.retornaMes(vlr)
       else: vlr = '00'
       return vlr

   def anoResolucao(self, Detalhe):
       ano_pattern = re.compile(u'(JANEIRO|FEVEREIRO|MARÇO|ABRIL|MAIO|JUNHO|JULHO|AGOSTO|SETEMBRO|OUTUBRO|NOVEMBRO|DEZEMBRO)\s*DE\s*(?P<ano>[0-9]+)')
       ano = ano_pattern.search(Detalhe) 
       if (ano):
           vlr = ano.group('ano')
       else: vlr = '0000'
       return vlr      
   
   def nomeComissao(self, Detalhe2):
       nomeComissao_pattern = re.compile(u'<NomeComissao>(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\n\s]+)')
       nome = nomeComissao_pattern.search(Detalhe2) 
       if (nome):
           vlr = nome.group('nome')
       else: vlr = '0000'
       return vlr      
    
   def convenioComissao(self, Detalhe2):
       convenioComissao_pattern = re.compile(u'<ConvenioComissao>(?P<numero>[0-9\/]+)')
       convenio = convenioComissao_pattern.search(Detalhe2) 
       if (convenio):
           vlr = convenio.group('numero')
       else: vlr = '0000'
       return vlr      
    
   def trataSeparacaoSilabica(self, txt):
       separacao_pattern = re.compile(u'(?P<separacao>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\n\s]+-\s+[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\n\s]+)')
       separado = separacao_pattern.search(txt) 
       if (separado):
           vlr = separado.group('separacao').replace('- ', '')
       else: vlr = txt
       return vlr    
   
   def converteData(sef, datas):
        data_pattern = re.compile(u'(?P<data>[X]+|00/|0000)')
        data = data_pattern.search(datas) 
        if (data):
          vlr = '01/01/1900'
        else: vlr = datas
        return vlr
        
 