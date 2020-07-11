#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 08:57:05 2020

@author: Fernando
@author: Hermann

Classe responsável por fazer o casamento dos padrões das expressões regulares na gramática do diário oficial.
Cada ato público é definido como um conjunto de padrões de expressões regulares.
"""
from RioJaneiroLayout import RioJaneiroLayout
from Ato import Ato
from Comissoes import Comissoes
from Util import Util
from UtilRegex import UtilRegex

import re

#class RioJaneiroLayoutNomeacao(): #Mudar para RioJaneiroLayoutAtos 
class LayoutAtos():    
    Cargo = 'A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\-\s'
    Nome = '[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]'
    TodosAcentos = '/[a-zA-Z\u00C0-\u00FF ]+/i'
   
    ####### RESOLUÇÃO SIMPLES #####
    #Resolução para uma nomeação
    
#Nomear SILVIO ROBERTO MACEDO LEAL JUNIOR, matrícula
#11/241.355-7, Arquiteto, para exercer o Cargo em Comissão de Gerente I,
#símbolo DAS-08, código 072969, da Gerência de Análise Urbano
#Ambiental, da Coordenadoria de Licenciamento de Projetos Sociais,
#da Coordenadoria Geral de Integração Técnica, da Subsecretaria de
#Habitação, da Secretaria Municipal de Infraestrutura e Habitação.

 
    #OBS ver casos de "ONDE SE LÊ" "LEIA-SE"atos_nomeacao
    def atos_nomeacao(self, buffer_local, Detalhe):
        #print('BUFFER--->', buffer_local)
        servidor = []
        nomeacao_pattern1 = re.compile(u'[\.|\s]*(Nomear)[,|\s]+(?P<nome>(?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s])+)[,|\s]*matrícula[,|\s]*(?P<matricula>[0-9\.\-\/]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),*\s*para\s*exercer\s*o\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),*\s*[S|s]ímbolo\s*(?P<simbolo>[A-Z\-0-9]+),*')
        nomeacao_pattern2 = re.compile(u'[\.|\s]*(Nomear)[,|\s]+(?P<nome>(?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s])+)[,|\s]*para\s*exercer\s*o\s*[C|c]argo\s*em\s*[C|c]omissão\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),*\s*[S|s]ímbolo\s*(?P<simbolo>[A-Z-0-9\/]+),*')  
        nomeacao_pattern3 = re.compile(u'[\.|\s]*(Nomear)[,|\s]+(?P<nome>(?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s])+)[,|\s]*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[,|\s]+para\s*exercer\s*o\s*[C|c]argo\s*(de|em)*\s*([C|c]omissão)*\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*símbolo\s*(?P<simbolo>[A-Z0-9\.\/\-\s]+),*')
        nomeacao_pattern4 = re.compile(u'[\.|\s]*(Nomear)[,|\s]+(?P<nome>(?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s])+)[,|\s]*matrícula[,|\s]*(?P<matricula>[0-9\.\-\/]+)[,|\s]*com\sa*\s*validade\sa\spartir\sde\s(?P<dia>[0-9]+).*(\s)*de(\s)*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)(\s)*de(\s)*(?P<ano>[0-9]+)[,|\s]*para\s*exer[\n|-]*cer\s*o\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),*\s*[S|s]ímbolo\s*(?P<simbolo>[A-Z\-0-9]+),*')         
        nomeacao_pattern5 = re.compile(u'[\.|\s]*(Nomear)[,|\s]+(?P<nome>(?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s])+)[,|\s]*matrícula[,|\s]*(?P<matricula>[0-9\.\-\/]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*com\sa\svalidade\sa\spartir\sde\s(?P<dia>[0-9]+).*(\s)*de(\s)*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)(\s)*de(\s)*(?P<ano>[0-9]+)[,|\s]*para\s*exer[\n|-]*cer\s*o\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),*\s*[S|s]ímbolo\s*(?P<simbolo>[A-Z\-0-9]+),*')
                              #[\.|\s]*(Nomear)[,|\s]+(?P<nome>(?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s])+)[,|\s]*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[,|\s]+para\s*exercer\s*o\s*[C|c]argo\s*(de|em)\s*[C|c]omissão\s*(de)*\s*(?P<cargoComissionado>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*símbolo\s*(?P<simbolo>[A-Z0-9\.\/\-\s]+),*
    
        nom1 = nomeacao_pattern1.search(buffer_local)
        nom2 = nomeacao_pattern2.search(buffer_local)
        nom3 = nomeacao_pattern3.search(buffer_local) # Esse é um decreto(efetivo ou comissionado, exemplo: arquivo 3952.pdf Antonio Flavio Ribas)
        nom4 = nomeacao_pattern4.search(buffer_local)
        nom5 = nomeacao_pattern5.search(buffer_local)
    
        if (nom1):
           #rint('Entrou --->A')
           for nomear in nomeacao_pattern1.finditer(buffer_local):
             if (nomear):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = nomear.group('nome')
                 ato.cargo = nomear.group('cargo')
                 ato.dia = 'XX'#nomear.group('dia')
                 ato.mes = 'XX'#nomear.group('mes')
                 ato.ano = 'XXXX'#nomear.group('ano')
                 ato.matricula = nomear.group('matricula')
                 ato.simbolo = nomear.group('simbolo')
                 ato.tipocargo = 'CC' 
                 ato.CPF = '(PADRAO 1.1)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (nom2):
          # print('Entrou --->B')
           for nomear in nomeacao_pattern2.finditer(buffer_local):
             if (nomear):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = nomear.group('nome')
                 ato.cargo = nomear.group('cargo')
                 ato.dia = 'XX'#nomear.group('dia')
                 ato.mes = 'XX'#nomear.group('mes')
                 ato.ano = 'XXXX'#nomear.group('ano')
                 ato.matricula = 'XXXXXXXXXXX'
                 ato.simbolo = nomear.group('simbolo')
                 ato.tipocargo = 'CC' 
                 ato.CPF = '(PADRAO 1.2)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (nom3):
          # print('Entrou --->B')
           for nomear in nomeacao_pattern3.finditer(buffer_local):
             if (nomear):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = nomear.group('nome')
                 ato.cargo = nomear.group('cargo')
                 ato.dia = nomear.group('dia')
                 ato.mes = nomear.group('mes')
                 ato.ano = nomear.group('ano')
                 ato.matricula = 'XXXXXXXXXXX'
                 ato.simbolo = nomear.group('simbolo')
                 ato.tipocargo = 'CC' 
                 ato.CPF = '(PADRAO 1.3)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (nom4):
          # print('Entrou --->B')
           for nomear in nomeacao_pattern4.finditer(buffer_local):
             if (nomear):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = nomear.group('nome')
                 ato.cargo = nomear.group('cargo')
                 ato.dia = nomear.group('dia')
                 ato.mes = nomear.group('mes')
                 ato.ano = nomear.group('ano')
                 ato.matricula = nomear.group('matricula')
                 ato.simbolo = nomear.group('simbolo')
                 ato.tipocargo = 'CC' 
                 ato.CPF = '(PADRAO 1.4)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (nom5):
           for nomear in nomeacao_pattern5.finditer(buffer_local):
             if (nomear):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = nomear.group('nome')
                 ato.cargo = nomear.group('cargo')
                 ato.dia = nomear.group('dia')
                 ato.mes = nomear.group('mes')
                 ato.ano = nomear.group('ano')
                 ato.matricula = nomear.group('matricula')
                 ato.simbolo = nomear.group('simbolo')
                 ato.tipocargo = 'CC' 
                 ato.CPF = '(PADRAO 1.5)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        return servidor   


    def atos_dispensar(self, buffer_local, Detalhe):
        servidor = []
        dispensar_pattern1 = re.compile(u'[\.|\s]*Dispensar[,|\s]*a\s*pedido[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*matrícula\s*(?P<matricula>[0-9\./-]+),\s*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+),\s*da\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s*(?P<simbolo>[A-Z\-0-9\/\s]+),')
        dispensar_pattern2 = re.compile(u'[\.|\s]*Dispensar[,|\s]*a\s*pedido[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*matrícula\s*(?P<matricula>[0-9\.\/-]+),\s*da\s*[F|f]unção\s*[G|g]ratificada\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s*(?P<simbolo>[A-Z\-0-9\/\s]+),')
        dispensar_pattern3 = re.compile(u'[\.|\s]*Dispensar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),*\s*matrícula\s*(?P<matricula>[0-9\.\/-]+),\s*da\s*[F|f]unção\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),*\s*símbolo\s*(?P<simbolo>[A-Z\-0-9\s\/]+),')
        dispensar_pattern4 = re.compile(u'[\.|\s]*Dispensar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[\s|,]+com[\s|,]+validade[\s|,]+de[\s|,]+(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[\s|,]+(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[\s|,]+matrícula\s*(?P<matricula>[0-9\.\/-]+)[\s|,]+da\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[\s|,]+símbolo[\s|,]+(?P<simbolo>[A-Z\-0-9\/\s]+),')
        dispensar_pattern5 = re.compile(u'[\.|\s]*Dispensar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[\s|,]+(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[\s|,]+matrícula\s*(?P<matricula>[0-9\.\/-]+)[\s|,]*[\s|,]*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[\s|,]+da\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[\s|,]+sím[-|\n]*bolo[\s|,]+(?P<simbolo>[A-Z\-0-9\/\s]+),')
        dispensar_pattern6 = re.compile(u'[\.|\s]*Dispensar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*matrícula\s*(?P<matricula>[0-9\.\/-]+)[,|\s]*da\s*[F|f]unção\s*de\s*[C|c]onfiança\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*código\s*(?P<simbolo>[A-Z\-0-9\s\/]+),')
        dispensar_pattern7 = re.compile(u'[\.|\s]*Dispensar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*registro\s*(N|n)*.\s*[0-9]+[,|\s]*com(\s)*(a)*(\s)*validade(\s)*(a)*(\s)*partir(\s)*de(\s)*(?P<dia>[0-9]+).*(\s)*de(\s)*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[,|\s]*do\s*[E|e]mprego\s*de\s*[C|c]onfiança\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*[C|c]*ategoria\s*(?P<simbolo>[A-Z-0-9\–\-\/\s]+),')
        dispensar_pattern8 = re.compile(u'[\.|\s]*Dispensar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]+matrícula\s*(?P<matricula>[0-9\–\.\/-]+)[,|\s]*com\s*a*\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovem[-|\n]*bro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[,|\s]*da\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*(código)*\s*[0-9]*[,|\s]*[S|s]ím[-|\n]*bolo[,|\s]*(?P<simbolo>[A-Z\–\-0-9\/\s]+),')

        disp1 = dispensar_pattern1.search(buffer_local)
        disp2 = dispensar_pattern2.search(buffer_local)
        disp3 = dispensar_pattern3.search(buffer_local)
        disp4 = dispensar_pattern4.search(buffer_local)
        disp5 = dispensar_pattern5.search(buffer_local)
        disp6 = dispensar_pattern6.search(buffer_local)
        disp7 = dispensar_pattern7.search(buffer_local)        
        disp8 = dispensar_pattern8.search(buffer_local)        
                
        if (disp1):
           for dispensar in dispensar_pattern1.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = dispensar.group('dia')
                 ato.mes = dispensar.group('mes')
                 ato.ano = dispensar.group('ano')
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FG' #Ver regra se toda dispensa é de FG
                 ato.CPF = '(PADRAO 1.6)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (disp2):   
           for dispensar in dispensar_pattern2.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = 'XX'
                 ato.mes = 'XX'
                 ato.ano = 'XXXX'
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FG' #Ver regra se toda dispensa é de FG
                 ato.CPF = '(PADRAO 1.7)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (disp3):   
           for dispensar in dispensar_pattern3.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = 'XX'#dispensar.group('dia')
                 ato.mes = 'XX'#dispensar.group('mes')
                 ato.ano = 'XXXX'#dispensar.group('ano')
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FUN' #Ver regra para este tipo de cargo
                 ato.CPF = '(PADRAO 1.8)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (disp4):   
           for dispensar in dispensar_pattern4.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = 'XX'
                 ato.mes = 'XX'
                 ato.ano = 'XXXX'
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FG'
                 ato.CPF = '(PADRAO 1.9)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (disp5):   
           for dispensar in dispensar_pattern5.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = dispensar.group('dia')
                 ato.mes = dispensar.group('mes')
                 ato.ano = dispensar.group('ano')
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FG'
                 ato.CPF = '(PADRAO 1.10)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (disp6):   
           for dispensar in dispensar_pattern6.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = 'XX'#dispensar.group('dia')
                 ato.mes = 'XX'#dispensar.group('mes')
                 ato.ano = 'XXXX'#dispensar.group('ano')
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FUN' #Ver regra para este tipo de cargo
                 ato.CPF = '(PADRAO 1.11)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (disp7):   
           for dispensar in dispensar_pattern7.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = dispensar.group('dia')
                 ato.mes = dispensar.group('mes')
                 ato.ano = dispensar.group('ano')
                 ato.matricula = 'XXXXXXXXXXX'
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'EC' #Emprego de Confiança
                 ato.CPF = '(PADRAO 1.12)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (disp8):   
           for dispensar in dispensar_pattern8.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = dispensar.group('dia')
                 ato.mes = dispensar.group('mes')
                 ato.ano = dispensar.group('ano')
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FG' #Emprego de Confiança
                 ato.CPF = '(PADRAO 1.13)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        return servidor  

     
    def atos_exonerar(self, buffer_local, Detalhe):
        servidor = []
        exonerar_pattern1 = re.compile(u'[\.|\s]*Exonerar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*matrícula\s*(?P<matricula>[0-9\/\.\-]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*do\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*símbolo\s(?P<simbolo>[A-Z0-9\-\/\s]+),*')
        exonerar_pattern2 = re.compile(u'[\.|\s]*Exonerar[,|\s]*a\s*pedido[,|\s]*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).?\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+),\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*matrícula\s*n.?\s*(?P<matricula>[0-9\./-]+)[,|\s]*do\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s(?P<simbolo>[A-Z0-9\-\/\s]+),')
        exonerar_pattern3 = re.compile(u'[\.|\s]*Exonerar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*matrícula\s*(?P<matricula>[0-9\/\.\-]+)[,|\s]*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).?\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[,|\s]*do\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s(?P<simbolo>[A-Z0-9\-\/\s]+),*')
        exonerar_pattern4 = re.compile(u'[\.|\s]*Exonerar[,|\s]*a\s*pedido[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s*]+),*\s*matrícula\s*(?P<matricula>[0-9\.\/\-]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).?\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[,|\s]*do\s*[C|c]argo\s*e[,|\s]*m\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*[S|s]+ímbolo\s(?P<simbolo>[A-Z0-9\-\/\s]+),*')
        exonerar_pattern5 = re.compile(u'[\.|\s]*Exonerar[,|\s]+(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]+matrícula\s*(?P<matricula>[0-9\/\.\-]+),\s(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).?\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[,|\s]*do\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*símbolo\s(?P<simbolo>[A-Z0-9\-\/\s]+),*')
        exo1 = exonerar_pattern1.search(buffer_local)
        exo2 = exonerar_pattern2.search(buffer_local)
        exo3 = exonerar_pattern3.search(buffer_local)
        exo4 = exonerar_pattern4.search(buffer_local)
        exo5 = exonerar_pattern5.search(buffer_local)
        
        if (exo1):
           for exonerar in exonerar_pattern1.finditer(buffer_local):
             if (exonerar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = exonerar.group('nome')
                 ato.cargo = exonerar.group('cargo')
                 ato.dia = 'XX'
                 ato.mes = 'XX'
                 ato.ano = 'XXXX'
                 ato.matricula = exonerar.group('matricula')
                 ato.simbolo = exonerar.group('simbolo')
                 #Definor regra para cargoEfetivo
                 ato.tipocargo = 'CC'
                 ato.CPF = '(PADRAO 1.14)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (exo2):
           for exonerar in exonerar_pattern2.finditer(buffer_local):
             if (exonerar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = exonerar.group('nome')
                 ato.matricula = exonerar.group('matricula')
                 ato.dia = 'XX'
                 ato.mes = 'XX'
                 ato.ano = 'XXXX'
                 ato.cargo = exonerar.group('cargo')
                 ato.simbolo = exonerar.group('simbolo')
                 ato.tipocargo = 'CC'
                 ato.CPF = '(PADRAO 1.15)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (exo3):
           for exonerar in exonerar_pattern3.finditer(buffer_local):
             if (exonerar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = exonerar.group('nome')
                 ato.matricula = exonerar.group('matricula')
                 ato.dia = exonerar.group('dia')
                 ato.mes = exonerar.group('mes')
                 ato.ano = exonerar.group('ano')
                 ato.cargo = exonerar.group('cargo')
                 ato.simbolo = exonerar.group('simbolo')
                 ato.tipocargo = 'CC'
                 ato.CPF = '(PADRAO 1.16)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (exo4):
           for exonerar in exonerar_pattern4.finditer(buffer_local):
             if (exonerar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = exonerar.group('nome')
                 ato.matricula = exonerar.group('matricula')
                 ato.dia = exonerar.group('dia')
                 ato.mes = exonerar.group('mes')
                 ato.ano = exonerar.group('ano')
                 ato.cargo = exonerar.group('cargo')
                 ato.simbolo = exonerar.group('simbolo')
                 ato.tipocargo = 'CC'
                 ato.CPF = '(PADRAO 1.17)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (exo5):
           for exonerar in exonerar_pattern5.finditer(buffer_local):
             if (exonerar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = exonerar.group('nome')
                 ato.matricula = exonerar.group('matricula')
                 ato.dia = exonerar.group('dia')
                 ato.mes = exonerar.group('mes')
                 ato.ano = exonerar.group('ano')
                 ato.cargo = exonerar.group('cargo')
                 ato.simbolo = exonerar.group('simbolo')
                 ato.tipocargo = 'CC'
                 ato.CPF = '(PADRAO 1.18)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        return servidor 


    def atos_designar(self, buffer_local, Detalhe, arqres):
        #print('BUFFER--->', buffer_local)
        servidor = []
        designar_pattern1 = re.compile(u'[\.|\s]*Designar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*com\s*validade\s*\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+),*\s*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\-\s]+),*\s*matrícula\s*(?P<matricula>[0-9\.\/-]+),*\s*da\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),*\s*símbolo\s(?P<simbolo>[A-Z-0-9\-\/\s]+),')
        designar_pattern2 = re.compile(u'[\.|\s]*Designar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*para\s*exercer\s*a Função\sde\s*Confiança\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),')  
        designar_pattern3 = re.compile(u'[\.|\s]*Designar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\-\s]+)[,|\s]*[M|m]atrícula\s*(?P<matricula>[0-9\–\.\/-]+)[,|\s]*(\s)*com(\s)*(a)*(\s)*validade(\s)*(a)*(\s)*partir(\s)*de(\s)*(?P<dia>[0-9]+).*(\s)*de(\s)*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)(\s)*de(\s)*(?P<ano>[0-9]+)[,|\s]*para(\s)*o(\s)*exercício(\s)*da(\s)*[F|f]unção\s*[G|g]ratificada(\s)*(de)*(\s)*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*(código)*(\s)*[0-9]+[,|\s]*[S|s]ímbolo(\s)*(?P<simbolo>[A-Z-0-9\–\-\/\s]+),')
        designar_pattern4 = re.compile(u'[\.|\s]*Designar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*(N|n)*.[,|\s]*CTPS[,|\s]*(N|n)*.[,|\s]*[0-9]+[,|\s]*(S|s)érie\s(?P<serie>[0-9]+[\s|\-]*\w\w)[,|\s]*com(\s)*(a)*(\s)*validade(\s)*(a)*(\s)*partir(\s)*de(\s)*(?P<dia>[0-9]+).*(\s)*de(\s)*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[,|\s]*para\s*o\s*[E|e]mprego\s*(de)*\s*[C|c]onfiança\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*[C|c]*ategoria\s*(?P<simbolo>[A-Z-0-9\–\-\/\s]+),')
        designar_pattern5 = re.compile(u'[\.|\s]*Designar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*[M|m]atrícula\s*(?P<matricula>[0-9\–\.\/-]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\-\s]+)[,|\s]*para(\s)*exercer(\s)*a*(\s)*[F|f]unção\s*[G|g]ratificada(\s)*(de)*(\s)*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*símbolo\s(?P<simbolo>[A-Z-0-9\-\/\s]+),')
        
        des1 = designar_pattern1.search(buffer_local)
        des2 = designar_pattern2.search(buffer_local)
        des3 = designar_pattern3.search(buffer_local)
        des4 = designar_pattern4.search(buffer_local)
        des5 = designar_pattern5.search(buffer_local)
        
        if (des1):
           #rint('Entrou --->A')
           for designar in designar_pattern1.finditer(buffer_local):
             if (designar):
#                 if (designar.group('nome').strip() == 'ELIANE DE OLIVEIRA'):
#                     print('DETALHE DA ELIANE', Detalhe)
#                     print('Buffer da ELIANE', buffer_local, file=arqres)
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = designar.group('nome')
                 ato.cargo = 'XXX'#nomear.group('cargoComissionado')
                 ato.dia = 'XX'#nomear.group('dia')
                 ato.mes = 'XX'#nomear.group('mes')
                 ato.ano = 'XXXX'#nomear.group('ano')
                 ato.matricula = 'XXX'#nomear.group('matricula')
                 ato.simbolo = 'XXXX'#nomear.group('simbolo')
                 ato.tipocargo = 'FG' 
                 ato.CPF = '(PADRAO 1.19)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (des2):
           for designar in designar_pattern2.finditer(buffer_local):
             if (designar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = designar.group('nome')
                 ato.cargo = designar.group('cargo')
                 ato.dia = 'XX'#nomear.group('dia')
                 ato.mes = 'XX'#nomear.group('mes')
                 ato.ano = 'XXXX'#nomear.group('ano')
                 ato.matricula = 'XXXXXXXXXXX'
                 ato.simbolo = 'XXXX'#designar.group('simbolo')
                 ato.tipocargo = 'FC' #função de Confiança 
                 ato.CPF = '(PADRAO 1.20)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (des3):
           for designar in designar_pattern3.finditer(buffer_local):
             if (designar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = designar.group('nome')
                 ato.cargo = designar.group('cargo')
                 ato.dia = designar.group('dia')
                 ato.mes = designar.group('mes')
                 ato.ano = designar.group('ano')
                 ato.matricula = designar.group('matricula')
                 ato.simbolo = 'XXXX'#designar.group('simbolo')
                 ato.tipocargo = 'FG' #função de Confiança 
                 ato.CPF = '(PADRAO 1.21)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (des4):
           for designar in designar_pattern4.finditer(buffer_local):
             if (designar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = designar.group('nome')
                 ato.cargo = designar.group('cargo')
                 ato.dia = designar.group('dia')
                 ato.mes = designar.group('mes')
                 ato.ano = designar.group('ano')
                 ato.matricula = 'XXXXXXXXXXX' #designar.group('matricula')
                 ato.simbolo = designar.group('simbolo')
                 ato.tipocargo = 'EC' #Emprogo de Confiança 
                 ato.CPF = '(PADRAO 1.22)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (des5):
           for designar in designar_pattern5.finditer(buffer_local):
             if (designar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.nome = designar.group('nome')
                 ato.cargo = designar.group('cargo')
                 ato.dia = 'XX'#nomear.group('dia')
                 ato.mes = 'XX'#nomear.group('mes')
                 ato.ano = 'XXXX'#nomear.group('ano')
                 ato.matricula = 'XXXXXXXXXXX'
                 ato.simbolo = designar.group('simbolo')
                 ato.tipocargo = 'FG' #função de Confiança 
                 ato.CPF = '(PADRAO 1.23)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        return servidor   


    def atos_criar_comissao(self, buffer_local, Detalhe, Detalhe2):
        servidor = []
        criar_comissao_pattern1 =  re.compile(u'^(?P<orgao>\w\/\w{6,12})(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)(?P<matricula>\d{2}/\d{3}[.|\s]{0,1}\d{3}-\d{1})$', re.MULTILINE) #11/230.329-5     (?P<matricula>\d{2}/\d{3}[.|\s]{0,1}\d{3}-\d{1})   12/197.249-6
        
        comcriar1 = criar_comissao_pattern1.search(buffer_local)
    
        if (comcriar1):
           for comissao in criar_comissao_pattern1.finditer(buffer_local):
             if (comissao):
                 #print (comissao)
                 comissoes = Comissoes()
                 utilReg = UtilRegex()
                 comissoes.numero = utilReg.numeroResolucao(Detalhe)  
                 comissoes.diaResolucao = utilReg.diaResolucao(Detalhe)
                 comissoes.mesResolucao = utilReg.mesResolucao(Detalhe)
                 comissoes.anoResolucao = utilReg.anoResolucao(Detalhe)  
                 comissoes.nome = comissao.group('nome')#buffer_local#comissao.group('nome')
                 comissoes.nomeComissao = utilReg.nomeComissao(Detalhe2).upper()
                 comissoes.convenio = utilReg.convenioComissao(Detalhe2).upper()
                 comissoes.dia = 'XX'#nomear.group('dia')
                 comissoes.mes = 'XX'#nomear.group('mes')
                 comissoes.ano = 'XXXX'#nomear.group('ano')
                 comissoes.matricula = comissao.group('matricula')
                 comissoes.orgao = comissao.group('orgao')
                 comissoes.tipocargo = 'COM' 
                 comissoes.CPF = '(PADRAO 1.24)'
                 servidor.append(comissoes)
             else: servidor.append('SERVIDOR NONE')
        return servidor   





    ####### RESOLUÇÕES #####################      
    #Resolução para várias nomeações
    
#No 502 - Nomear NEFERTITE ALVES MACIEL KRAFZIK, PROFESSOR
#DE ENSINO FUNDAMENTAL, matrícula 10/297462-4, para exercer, com
#eficácia a contar de 1o de fevereiro de 2019, o Cargo em Comissão de
#DIRETOR IV, símbolo DAS-06, código 28592, setor 17898 da 6a Coor-
#denadoria Regional de Educação, desta Secretaria. (ref. ao processo n o
#07/06/000495/2019).
    
#No 488 - Nomear ALESSANDRA BRAGA BRITO ROCHA, PROFESSOR II,
#matrícula 10/216096-8, para exercer, com eficácia a contar de 1o de
#fevereiro de 2019, o Cargo em Comissão de DIRETOR IV, símbolo
#DAS-06, código 35881, setor 44185 da 4a Coordenadoria Regional de
#Educação, desta Secretaria. (ref. ao processo n o 07/04/000268/2019).
                                                   
    def atos_nomeacoes(self, buffer_local, Detalhe):
        servidor = []
        #nomeacoes_pattern = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*Nomear,*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\smatrícula\s(?P<matricula>[0-9\./-]+),\s*para\s*exercer,*\s*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s*de\s*(?P<ano>[0-9]+),\s*o\s*[C|c]argo\s*em\s*[C|c]omissão\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\s]+),\s*símbolo\s(?P<simbolo>[A-Z-0-9\s]+),')
        #\s(?P<numero>[0-9]+)\s*-\s*Nomear,*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*matrícula\s*(?P<matricula>[0-9\.\/-]+),\s*para\s*exercer,*\s*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s*de\s*(?P<ano>[0-9]+),\s*o\s*[C|c]argo\s*em\s*[C|c]omissão\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\s]+),\s*símbolo\s*(?P<simbolo>[A-Z0-9-]+)
        nomeacoes_pattern1 = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*Nomear,*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*matrícula\s*(?P<matricula>[0-9\.\/\-]+),\s*para\s*exercer,*\s*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+),\s*o\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s*(?P<simbolo>[A-Z0-9\/\-\s]+),*')
        nomeacoes_pattern2 = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*Nomear,*\s*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+),*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),*\s*matrícula\s*(n.)*\s*(?P<matricula>[0-9\.\/\-]+),*\s*para\s*exercer\s*o\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s*(?P<simbolo>[A-Z0-9\/\-\s]+),*')

        nom1 = nomeacoes_pattern1.search(buffer_local)
        nom2 = nomeacoes_pattern2.search(buffer_local)
        if (nom1):
           for nomear in nomeacoes_pattern1.finditer(buffer_local):
             if (nomear):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.numero = nomear.group('numero')
                 ato.nome = nomear.group('nome')
                 ato.cargo = nomear.group('cargo')
                 ato.dia = nomear.group('dia')
                 ato.mes = nomear.group('mes')
                 ato.ano = nomear.group('ano')
                 ato.matricula = nomear.group('matricula')
                 ato.simbolo = nomear.group('simbolo')
                 ato.tipocargo = 'CC' 
                 ato.CPF = '(PADRAO 2.1)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (nom2):
           for nomear in nomeacoes_pattern2.finditer(buffer_local):
             if (nomear):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.numero = nomear.group('numero')
                 ato.nome = nomear.group('nome')
                 ato.cargo = nomear.group('cargo')
                 ato.dia = nomear.group('dia')
                 ato.mes = nomear.group('mes')
                 ato.ano = nomear.group('ano')
                 ato.matricula = nomear.group('matricula')
                 ato.simbolo = nomear.group('simbolo')
                 ato.tipocargo = 'CC' 
                 ato.CPF = '(PADRAO 2.2)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        return servidor   
    
#No 497 - Designar MAURÍCIO OLIVEIRA CHAVES, PROFESSOR DE
#ENSINO FUNDAMENTAL, matrícula 10/285208-5, para exercer, com
#eficácia a contar de 1o de fevereiro de 2019, a Função Gratificada de
#COORDENADOR PEDAGÓGICO, símbolo DAI-06, código 7835, setor
#11075 da 8a Coordenadoria Regional de Educação, desta Secretaria. (ref.
#ao processo n o 07/08/000375/2019).
        
#No 486 - Designar ADRIANA DORNELLAS FERREIRA, PROFESSOR II,
#matrícula 10/231943-2, para exercer a Função Gratificada de DIRETOR
#ADJUNTO, símbolo DAI-06, código 6012, setor 11826 da 3a Coorde-
#nadoria Regional de Educação, desta Secretaria. (ref. ao processo n o
#07/03/000185/2019). 
                                                 
    def atos_desitestes(self, buffer_local, Detalhe):
        #print('BUFFER--->', buffer_local)
        #\s(?P<numero>[0-9]+)\s*-\s*Designar,*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\smatrícula\s(?P<matricula>[0-9\.\/-]+),\s*para\s*exercer,*\s*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s*de\s*(?P<ano>[0-9]+),\s*a\s*[F|f]unção\s*[G|g]ratificada\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâêôúã\s]+),*\s*símbolo\s(?P<simbolo>[A-Z-0-9\s]+),
        designacoes_pattern = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*Designar,*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*matrícula\s*')
        des1 = designacoes_pattern.search(buffer_local)
        if (des1):
           for designar in designacoes_pattern.finditer(buffer_local):
               print('NOME-->',designar.group('nome'),'CARGO-->',designar.group('cargoEfetivo'), )
        
    
    
    def atos_designacoes(self, buffer_local, Detalhe):
        servidor = []
        #\s(?P<numero>[0-9]+)\s*-\s*Designar,*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\smatrícula\s(?P<matricula>[0-9\.\/-]+),\s*para\s*exercer,*\s*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s*de\s*(?P<ano>[0-9]+),\s*a\s*[F|f]unção\s*[G|g]ratificada\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâêôúã\s]+),*\s*símbolo\s(?P<simbolo>[A-Z-0-9\s]+),
        #\s(?P<numero>[0-9]+)\s*-\s*\.*Designar,*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\-\s]+),\s*matrícula\s*(?P<matricula>[0-9\.\/-]+),\s*para\s*exercer,*\s*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s*de\s*(?P<ano>[0-9]+),\s*a\s*[F|f]unção\s*[G|g]ratificada\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),*\s*símbolo\s(?P<simbolo>[A-Z-0-9\-\/\s]+),
        designacoes_pattern1 = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*\.*Designar,*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\-\s]+),\s*matrícula\s*(?P<matricula>[0-9\.\/-]+),\s*para\s*exercer,*\s*com\s*(efi-*\n*)cácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+),\s*a\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),*\s*símbolo\s(?P<simbolo>[A-Z-0-9\-\/\s]+),')
        designacoes_pattern2 = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*\.*Designar,*\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\-\s]+),\s*matrícula\s*(?P<matricula>[0-9\.\/-]+),\s*para\s*exercer,*\s*a\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s(?P<simbolo>[A-Z-0-9\/\-\s]+),')
 
        des1 = designacoes_pattern1.search(buffer_local)
        des2 = designacoes_pattern2.search(buffer_local)
        if (des1):
           for designar in designacoes_pattern1.finditer(buffer_local):
             if (designar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.numero = designar.group('numero')
                 ato.nome = designar.group('nome')
                 ato.cargo = designar.group('cargo')
                 ato.dia = designar.group('dia') 
                 ato.mes = designar.group('mes')
                 ato.ano = designar.group('ano')
                 ato.matricula = designar.group('matricula')
                 ato.simbolo = designar.group('simbolo')
                 #Definor regra para cargoEfetivo
                 ato.tipocargo = 'FG'
                 ato.CPF = '(PADRAO 2.3)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (des2):
           for designar in designacoes_pattern2.finditer(buffer_local):
             if (designar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.numero = designar.group('numero')
                 ato.nome = designar.group('nome')
                 ato.matricula = designar.group('matricula')
                 ato.dia = 'XX' 
                 ato.mes = 'XX'
                 ato.ano = 'XXXX'
                 ato.cargo = designar.group('cargo')
                 ato.simbolo = designar.group('simbolo')
                 ato.tipocargo = 'FG'
                 ato.CPF = '(PADRAO 2.4)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        return servidor 



    #Resolução para várias Dispensações
#No 494 - Dispensar, a pedido, ANA CRISTINA DAVID DA SILVA,
#PROFESSOR II, matrícula 12/105900-5, com eficácia a contar de 1o
#de fevereiro de 2019, da Função Gratificada de DIRETOR ADJUNTO,
#símbolo DAI-06, código 7301, setor 11456 da 7a Coordenadoria Regional
#de Educação, desta Secretaria. (ref. ao processo n o 07/07/000338/2019).

    def atos_dispensas(self, buffer_local, Detalhe):
        servidor = []
        dispensacoes_pattern1 = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*.*Dispensar[,|\s]*a\s*pedido,\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*matrícula\s*(?P<matricula>[0-9\.\/-]+)[,|\s]*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+),\s*da\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s*(?P<simbolo>[A-Z-0-9\/\-\s]+),')
        dispensacoes_pattern2 = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*.*Dispensar[,|\s]*a\s*pedido,\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*matrícula\s*(?P<matricula>[0-9\.\/-]+)[,|\s]*da\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s*(?P<simbolo>[A-Z-0-9\-\/\s]+),')
        dispensacoes_pattern3 = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*.*Dispensar[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*matrícula\s*(?P<matricula>[0-9\.\/-]+)[,|\s]*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+),\s*da\s*[F|f]unção\s*[G|g]ratificada\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s*(?P<simbolo>[A-Z-0-9\/\-\s]+),')
        
        disp1 = dispensacoes_pattern1.search(buffer_local)
        disp2 = dispensacoes_pattern2.search(buffer_local)
        disp3 = dispensacoes_pattern3.search(buffer_local)
        
        if (disp1):
           for dispensar in dispensacoes_pattern1.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.numero = dispensar.group('numero')
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = dispensar.group('dia')
                 ato.mes = dispensar.group('mes')
                 ato.ano = dispensar.group('ano')
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FG' #Ver regra se toda dispensa é de FG
                 ato.CPF = '(PADRAO 2.5)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (disp2):   
           for dispensar in dispensacoes_pattern2.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.numero = dispensar.group('numero')
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = 'XX'
                 ato.mes = 'XX'
                 ato.ano = 'XXXX'
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FG' #Ver regra se toda dispensa é de FG
                 ato.CPF = '(PADRAO 2.6)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (disp3):   
           for dispensar in dispensacoes_pattern3.finditer(buffer_local):
             if (dispensar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.numero = dispensar.group('numero')
                 ato.nome = dispensar.group('nome')
                 ato.cargo = dispensar.group('cargo')
                 ato.dia = dispensar.group('dia')
                 ato.mes = dispensar.group('mes')
                 ato.ano = dispensar.group('ano')
                 ato.matricula = dispensar.group('matricula')
                 ato.simbolo = dispensar.group('simbolo')
                 ato.tipocargo = 'FG' #Ver regra se toda dispensa é de FG
                 ato.CPF = '(PADRAO 2.7)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        return servidor  
    
    #Resolução para várias Exoneracoes
#    def atos_exoneracoes(self, buffer_local):
#        print('entrou')
#        servidor = []
#        exoneracoes_pattern = re.compile(u'(?P<numero>[0-9]*)\s*-\s*Exonerar\s*(,\s*a\s*pedido,\s*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]*))?.*(?P<nome>(?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ]|\s)+)')
#        for exonerar in exoneracoes_pattern.finditer(buffer_local):
#          if (exonerar):
#              ato = Ato()
#              ato.numero = exonerar.group('numero')
##              ato.nome = exonerar.group('nome')
#              ato.dia = exonerar.group('dia')
#              ato.CPF = '(PADRAO XXXXXX)'               
#              servidor.append(ato)
#          else: servidor.append('SERVIDOR NONE')
#        return servidor  


#Padrao 2_1
#No 490 - Exonerar, a pedido, ELAINE CRISTINA PERES FERREIRA
#VIEIRA, PROFESSOR DE ENSINO RELIGIOSO, matrícula 11/193462-9,
#com eficácia a contar de 1o de fevereiro de 2019, do Cargo em Comissão
#de DIRETOR IV, símbolo DAS-06, código 28592, setor 17898 da 6a Coor-
#denadoria Regional de Educação, desta Secretaria. (ref. ao processo n o
#07/06/000494/2019).

#Padrao 2_2
#N° 015 - Exonerar, a pedido, com validade a partir de 01 de fevereiro
#de 2019, LUCIA MARTINS ANDRADE, matrícula no 40/901.732-8, do
#cargo em comissão de Assessor, símbolo DAS-7, da 5a Inspetoria
#Geral de Controle Externo - 5a IGE, da Secretaria Geral de Controle
#Externo - SGCE.




    def atos_exoneracoesTeste(self, buffer_local, Detalhe):
        servidor = []
#        exoneracoes_pattern1 = re.compile(u'\s(?P<numero>[0-9]*)\s*-\s*Exonerar,\sa\spedido,\s(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ]+|\s),\s(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\smatrícula\s(?P<matricula>[0-9/-]+),\scom\seficácia\sa\scontar\sde\s(?P<dia>[0-9]+)o*\sde\s(?P<mes>[a-zç]+)\sde\s(?P<ano>[0-9]+),\sdo\sCargo\sem\sComissão\sde\s(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\ssímbolo\s(?P<simbolo>[A-Z-0-9]+),')
#        exoneracoes_pattern2 = re.compile(u'(?P<numero>[0-9]*)\s*-\s*Exonerar\s*, a pedido, com validade a partir de')
#        exoneracoes_pattern_2_1 = re.compile(u'\s(?P<numero>[0-9]*)\s*-\s*Exonerar,\s*a\s*pedido, (?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\smatrícula\s(?P<matricula>[0-9/-]+),\s*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s*de\s*(?P<ano>[0-9]+),\s*do\s*cargo\s*em\s*comissão\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*símbolo\s(?P<simbolo>[A-Z-0-9]+),')
#        exoneracoes_pattern_2_2 = re.compile(u'\s(?P<numero>[0-9]*)\s*-\s*Exonerar,\s*a\s*pedido,\s*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).?\s*de\s*(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s*de\s*(?P<ano>[0-9]+),\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*matrícula\s*(?P<matricula>[0-9/-]+),\s*do\s*cargo\s*em\s*comissão\s*de\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záéóíçâôú\s]+),\s*símbolo\s(?P<simbolo>[A-Z-0-9]+),')
        exoneracoes_pattern_2_1 = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*Exonerar,\s*a\s*pedido,\s*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+)[,|\s]*(?P<cargoEfetivo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+)[,|\s]*matrícula\s*(?P<matricula>[0-9\./-]+)[,|\s]*com\s*eficácia\s*a\s*contar\s*de\s*(?P<dia>[0-9]+).*\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+),\s*do\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s(?P<simbolo>[A-Z0-9\-\/\s]+),')
        exoneracoes_pattern_2_2 = re.compile(u'\s(?P<numero>[0-9]+)\s*-\s*Exonerar,\s*a\s*pedido,\s*com\s*validade\s*a\s*partir\s*de\s*(?P<dia>[0-9]+).?\s*de\s*(?P<mes>[J|j]aneiro|[F|f]evereiro|[M|m]arço|[A|a]bril|[M|m]aio|[J|j]unho|[J|j]ulho|[A|a]gosto|[S|s]etembro|[O|o]utubro|[N|n]ovembro|[D|d]ezembro)\s*de\s*(?P<ano>[0-9]+)[,|\s]*(?P<nome>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s]+),\s*matrícula\s*n.?\s*(?P<matricula>[0-9\./-]+),\s*do\s*[C|c]argo\s*em\s*[C|c]omissão\s*(de)*\s*(?P<cargo>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\s]+),\s*símbolo\s(?P<simbolo>[A-Z0-9\-\/\s]+),')

        exo1 = exoneracoes_pattern_2_1.search(buffer_local)
        exo2 = exoneracoes_pattern_2_2.search(buffer_local)
        if (exo1):
           for exonerar in exoneracoes_pattern_2_1.finditer(buffer_local):
             if (exonerar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                 ato.numero = exonerar.group('numero')
                 ato.nome = exonerar.group('nome')
                 ato.cargo = exonerar.group('cargo')
                 ato.dia =  exonerar.group('dia')
                 ato.mes = exonerar.group('mes')
                 ato.ano = exonerar.group('ano')
                 ato.matricula = exonerar.group('matricula')
                 ato.simbolo = exonerar.group('simbolo')
                 #Definor regra para cargoEfetivo
                 ato.tipocargo = 'CC'
                 ato.CPF = '(PADRAO 2.8)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        if (exo2):
           for exonerar in exoneracoes_pattern_2_2.finditer(buffer_local):
             #print('Detalhe Resolucoes---->',Detalhe)
             if (exonerar):
                 ato = Ato()
                 utilReg = UtilRegex()
                 ato.numero = utilReg.numeroResolucao(Detalhe)  
                 ato.diaResolucao = utilReg.diaResolucao(Detalhe)
                 ato.mesResolucao = utilReg.mesResolucao(Detalhe)
                 ato.anoResolucao = utilReg.anoResolucao(Detalhe)
                 ato.numero = exonerar.group('numero')
                 ato.nome = exonerar.group('nome')
                 ato.matricula = exonerar.group('matricula')
                 ato.dia = exonerar.group('dia') 
                 ato.mes = exonerar.group('mes')
                 ato.ano = exonerar.group('ano')
                 ato.cargo = exonerar.group('cargo')
                 ato.simbolo = exonerar.group('simbolo')
                 ato.tipocargo = 'CC'
                 ato.CPF = '(PADRAO 2.9)'
                 servidor.append(ato)
             else: servidor.append('SERVIDOR NONE')
        return servidor 





