#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:18:50 2019

@@author: Fernando
@author: Hermann

Classe responsável por fazer a chamada para construção do arquivo de auditoria e persistencia no banco de dados PostgreSql.
"""
#from Layout import Layout
from LayoutAtos import LayoutAtos 
from Util import Util
from Diario import Diario
from RioJaneiroDAO import RioJaneiroDAO
from Ato import Ato
from Comissoes import Comissoes
from Persistencia import Persistencia

t = u"u00b0"

import re

class RioJaneiroLayoutFinal(LayoutAtos):    
   
    tipo = ""
   
    
    
    def do_diario(self, buffer, arquivo):
        print(arquivo)
        #diario_pattern = re.compile('Ano\s(\w{3}|\w{4}|\w{5}|\w{6})\s•\sN\w\s(\d{3})')
        diario_pattern = re.compile('Ano\s([A-Z]*)\s•\sN\w\s([0-9]*)')        
        diario_edicao = diario_pattern.search(buffer)        
        print(diario_edicao.group(1))        
        print("Arquivo->"+arquivo+'\n')
        
        #Diário Suplementar
        diario_suplemento_pattern = re.compile('Diário Oficial do Município do Rio de Janeiro\s\|\s\w*\s\w*\s\|\s\w*\s\w*\s\|\s(Suplemento)')
        diario_suplemento = diario_suplemento_pattern.search(buffer)
        if diario_suplemento:
           tipo = 2 #Suplemento
        else:
           tipo = 1 #Normal 
        
        util = Util()
        diario = Diario()                
        RioDAO = RioJaneiroDAO()        
        diario.anoromano = (diario_edicao.group(1))
        diario.ano = (util.converteRomano(diario_edicao.group(1)))
        diario.numero = (diario_edicao.group(2))
        diario.nomearquivo = None #str(arquivo)
        diario.datadiario = None #Colocar aqui a informação correta da data do diário
        diario.tipo = (tipo)
        diario.identidade = None #int(1) #Codigo provisorio do Rio de Janeiro
        diario.datagravacao = None #Colocar aqui uam finção de data atual do sistema
        RioDAO.gravaDiario(diario)
               
  
        
        
        
    def resolucoes(self, buffer, arquivo, arq1, criticas, contarq, data_e_hora, arqres, perc):
        print('ARQUIVO========================================================>',arquivo,'(CARGOS)', perc,'%')
        ################# PROCESSA CABEÇALHO DO DIARIO ################
        diario_pattern = re.compile('Ano\s([A-Z]*)\s•\sN\w\s([0-9]*)')        
        diario_edicao = diario_pattern.search(buffer)  

        diario_suplemento_pattern = re.compile('Diário Oficial do Município do Rio de Janeiro\s\|\s\w*\s\w*\s\|\s\w*\s\w*\s\|\s(Suplemento)')
        diario_suplemento = diario_suplemento_pattern.search(buffer)
        if diario_suplemento:
           tipo = 'SUPLEMENTAR' #Suplemento
        else:
           tipo = 'NORMAL' #Normal 

        util = Util()
        diario = Diario() 
        if (diario_edicao.group(1)):               
            diario.anoromano = '{: <6}'.format(((diario_edicao.group(1))))
            diario.ano = (util.converteRomano(diario_edicao.group(1)))
            diario.numero = '{:0>6}'.format((diario_edicao.group(2)))
            diario.tipo = '{: <12}'.format((tipo))
            if (diario.ano < 26): print("Diário anterior a 2013:", "Ano:",diario.ano, "Arquivo:", arquivo.upper() ,file=criticas) 
        else:
            diario.anoromano = 'XXXXXX'
            diario.ano = 'XXXXXX'
            diario.numero = 'XXXXXX'
            diario.tipo = 'XXXXXXXXXXXX'


        print('', file=arq1)
        print('(PUC-RIO/TECMF)   ::PROCESSAMENTO DO DIÁRIO::', 'ANO:', diario.ano,'No.:', diario.numero, 'TIPO:', diario.tipo, '* RIO DE JANEIRO * ARQUIVO:',arquivo.upper(), 'SEQ.:', '{:0>4}'.format(contarq), '                                             ',data_e_hora,  file=arq1)
        print('', file=arq1) 

           
        #############################################################
        
        resolucao_pattern = re.compile(r'^(\*RESOLUÇÕES|RESOLUÇÕES|RESOLUÇOES|RESOLUÇÃO|RESOLUÇAO|PORTARIAS|DECRETO RIO|PORTARIA)\s*(.)*\s*“P”.*',re.M)
        contador = 1
        cont=-1
        inicio = []
        bloco = []
        servidor = []
        tamanho = len(buffer)
        for resolucao in resolucao_pattern.finditer(buffer):
            inicio.append(resolucao.start())
            contador=contador + 1 
        inicio.append(tamanho)        
            
  
 
        for i in range(len(inicio)-1):
            bloco.append(inicio[i+1]-inicio[i])
            buffer_local = buffer[inicio[i]:inicio[i]+bloco[i]]
            
            
            ###### Resolução #####
            resolucao1_pattern = re.compile(r'^(?P<resolucao1>\*RESOLUÇÕES|RESOLUÇÕES|RESOLUÇOES|RESOLUÇÃO|RESOLUÇAO|PORTARIAS|DECRETO RIO|PORTARIA)\s*(.)*\s*“P”(?P<detalhe_resolucao1>.*)',re.M)
            resolucao1 = resolucao1_pattern.search(buffer_local)
            if (resolucao1):
                Tipo = '{: <11}'.format(resolucao1.group('resolucao1'))
                Detalhe = resolucao1.group('detalhe_resolucao1')
            else:
                #print('Não casou resolucao1')
                Tipo = 'SEM TIPO'
                Detalhe = 'SEM DETALHE'
            #####################
            
            
            #### Gestor #####
            gestor_pattern = re.compile(r'(?P<gestor>[O|A]*\s(SECRETÁRI[O|A]+|PROCURADOR[A]*|PREFEITO[A]*|COORDENADOR[A]*)[A-ZÁÚÍÃÓÇÊÉ\s-]+)')
            gestor = gestor_pattern.search(buffer_local)
            if (gestor):
                Gestor = gestor.group('gestor')
            else:
                Gestor = 'SEM GESTOR'
            #print('-----FIM DO BLOCO-----')
            ###### Fim Gestor
            
         ################################# RESOLUÇÕES COMPOSTAS #############################
            persistencia = Persistencia()
            if ((resolucao1.group('resolucao1') == '*RESOLUÇÕES') or (resolucao1.group('resolucao1') == 'RESOLUÇÕES') or (resolucao1.group('resolucao1') == 'RESOLUÇOES') or (resolucao1.group('resolucao1') == 'RESOLUCOES') or (resolucao1.group('resolucao1') == 'PORTARIAS') ):
                
               servidor = LayoutAtos.atos_nomeacoes(self, buffer_local, Detalhe)
               util = Util()
               ato = Ato()
               
               for i in range(len(servidor)):
                   ato.numero = '{:0>4}'.format(servidor[i].numero)
                   ato.nome = '{: <50}'.format((servidor[i].nome).replace('\n', ' ').replace('  ', ' ').strip(" "))
                   ato.diaResolucao = '{:0>2}'.format(servidor[i].diaResolucao)
                   ato.mesResolucao = '{:0>2}'.format(servidor[i].mesResolucao)
                   ato.anoResolucao = servidor[i].anoResolucao  
                   ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                   ato.dia = '{:0>2}'.format(servidor[i].dia)
                   ato.mes = util.retornaMes(servidor[i].mes.replace(' ', ''))
                   ato.ano = servidor[i].ano
                   ato.dataEfeito = ato.dia+'/'+ato.mes+'/'+ato.ano
                   ato.matricula = '{: <12}'.format(servidor[i].matricula.replace('.', ''))
                   #ato.cargo = '{: <48}'.format(servidor[i].cargo.upper()).replace('\n', ' ')
                   ato.cargo = '{: <48}'.format((servidor[i].cargo.upper()).replace('\n', ' ').replace('  ', ' ').replace('- ', '').strip(" "))
                   ato.CPF = '{: <13}'.format(servidor[i].CPF) #vER ESTA REGRA!!!!!
                   ato.tipocargo =  servidor[i].tipocargo
                   ato.simbolo = '{: <6}'.format(servidor[i].simbolo.replace('\n', ''))
                   print(ato.CPF, Tipo, ato.numero, ato.dataResolucao, 'NOMEAR   ',  ato.matricula, ato.nome, ato.dataEfeito, ato.cargo, ato.simbolo, ato.tipocargo, file=arq1)
                   persistencia.insert(ato.matricula, ato.nome, ato.dataResolucao, 'NOMEAR', ato.dataEfeito, ato.cargo, ato.tipocargo, ato.simbolo)


               servidor = LayoutAtos.atos_designacoes(self, buffer_local, Detalhe)
               ato = Ato()
               for i in range(len(servidor)):
                   ato.numero = '{:0>4}'.format(servidor[i].numero)
                   ato.nome = '{: <50}'.format((servidor[i].nome).replace('\n', ' ').replace('  ', ' ').strip(" "))
                   ato.diaResolucao = '{:0>2}'.format(servidor[i].diaResolucao)
                   ato.mesResolucao = '{:0>2}'.format(servidor[i].mesResolucao)
                   ato.anoResolucao = servidor[i].anoResolucao
                   ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                   ato.dia = '{:0>2}'.format(servidor[i].dia)
                   ato.mes = util.retornaMes(servidor[i].mes.replace(' ', ''))
                   ato.ano = servidor[i].ano
                   ato.dataEfeito = ato.dia+'/'+ato.mes+'/'+ato.ano
                   ato.matricula = '{: <12}'.format(servidor[i].matricula.replace('.', ''))
                   ato.cargo = '{: <48}'.format((servidor[i].cargo.upper()).replace('\n', ' ').replace('  ', ' ').replace('- ', '').strip(" "))
                   ato.CPF = '{: <13}'.format(servidor[i].CPF) #vER ESTA REGRA!!!!!
                   ato.tipocargo =  servidor[i].tipocargo
                   ato.simbolo = '{: <6}'.format(servidor[i].simbolo.replace('\n', ''))
                   print(ato.CPF, Tipo, ato.numero, ato.dataResolucao, 'DESIGNAR ',  ato.matricula, ato.nome, ato.dataEfeito, ato.cargo, ato.simbolo, ato.tipocargo, file=arq1)
                   persistencia.insert(ato.matricula, ato.nome, ato.dataResolucao, 'DESIGNAR', ato.dataEfeito, ato.cargo, ato.tipocargo, ato.simbolo)
             
              
               servidor = LayoutAtos.atos_dispensas(self, buffer_local, Detalhe)
               ato = Ato()
               util = Util()
               for i in range(len(servidor)):
                   ato.numero = '{:0>4}'.format(servidor[i].numero)
                   ato.nome = '{: <50}'.format((servidor[i].nome).replace('\n', ' ').replace('  ', ' ').strip(" "))
                   ato.diaResolucao = '{:0>2}'.format(servidor[i].diaResolucao)
                   ato.mesResolucao = '{:0>2}'.format(servidor[i].mesResolucao)
                   ato.anoResolucao = servidor[i].anoResolucao
                   ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                   ato.dia = '{:0>2}'.format(servidor[i].dia)
                   ato.mes = util.retornaMes(servidor[i].mes.replace(' ', ''))
                   ato.ano = servidor[i].ano
                   ato.dataEfeito = ato.dia+'/'+ato.mes+'/'+ato.ano
                   ato.matricula = '{: <12}'.format(servidor[i].matricula.replace('.', ''))
                   #ato.cargo = '{: <48}'.format(servidor[i].cargo.upper()).replace('\n', ' ')
                   ato.cargo = '{: <48}'.format((servidor[i].cargo.upper()).replace('\n', ' ').replace('  ', ' ').replace('- ', '').strip(" "))
                   ato.CPF = '{: <13}'.format(servidor[i].CPF) #vER ESTA REGRA!!!!!
                   ato.tipocargo =  servidor[i].tipocargo
                   ato.simbolo = '{: <6}'.format(servidor[i].simbolo.replace('\n', ''))
                   print(ato.CPF, Tipo, ato.numero, ato.dataResolucao, 'DISPENSAR',  ato.matricula, ato.nome, ato.dataEfeito, ato.cargo, ato.simbolo, ato.tipocargo, file=arq1)
                   persistencia.insert(ato.matricula, ato.nome, ato.dataResolucao, 'DISPESAR', ato.dataEfeito, ato.cargo, ato.tipocargo, ato.simbolo)
  

               servidor = LayoutAtos.atos_exoneracoesTeste(self, buffer_local, Detalhe)
               ato = Ato()
               util = Util()
               for i in range(len(servidor)):
                   ato.numero = '{:0>4}'.format(servidor[i].numero)
                   ato.nome = '{: <50}'.format((servidor[i].nome).replace('\n', ' ').replace('  ', ' ').strip(" "))
                   ato.diaResolucao = '{:0>2}'.format(servidor[i].diaResolucao)
                   ato.mesResolucao = '{:0>2}'.format(servidor[i].mesResolucao)
                   ato.anoResolucao = servidor[i].anoResolucao                   
                   ato.dia = '{:0>2}'.format(servidor[i].dia)
                   ato.mes = util.retornaMes(servidor[i].mes)
                   ato.ano = servidor[i].ano
                   ato.dataEfeito = ato.dia+'/'+ato.mes+'/'+ato.ano
                   ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                   ato.matricula = '{: <12}'.format(servidor[i].matricula.replace('.', ''))
                   #ato.cargo = '{: <48}'.format(servidor[i].cargo.upper()).replace('\n', ' ')
                   ato.cargo = '{: <48}'.format((servidor[i].cargo.upper()).replace('\n', ' ').replace('  ', ' ').replace('- ', '').strip(" "))
                   ato.CPF = '{: <13}'.format(servidor[i].CPF) #vER ESTA REGRA!!!!!
                   ato.tipocargo =  servidor[i].tipocargo
                   ato.simbolo = '{: <6}'.format(servidor[i].simbolo.replace('\n', ''))
                   print(ato.CPF, Tipo, ato.numero, ato.dataResolucao, 'EXONERAR ',  ato.matricula, ato.nome, ato.dataEfeito, ato.cargo, ato.simbolo, ato.tipocargo, file=arq1)
                   persistencia.insert(ato.matricula, ato.nome, ato.dataResolucao, 'EXONERAR', ato.dataEfeito, ato.cargo, ato.tipocargo, ato.simbolo)

               
       ######################## RESOLUÇÃO SIMPLES ########################### 
              
            elif ((resolucao1.group('resolucao1') == 'RESOLUÇÃO') or (resolucao1.group('resolucao1') == 'RESOLUÇAO') or (resolucao1.group('resolucao1') == 'RESOLUCAO') or (resolucao1.group('resolucao1') == 'DECRETO RIO') or (resolucao1.group('resolucao1') == 'PORTARIA')):
               servidor = LayoutAtos.atos_nomeacao(self, buffer_local, Detalhe)
               for i in range(len(servidor)):
                   ato = Ato()
                   ato.nome = '{: <50}'.format((servidor[i].nome).replace('\n', ' ').replace('  ', ' ').strip(" "))
                   ato.numero = '{:0>4}'.format(servidor[i].numero)
                   ato.diaResolucao = '{:0>2}'.format(servidor[i].diaResolucao)
                   ato.mesResolucao = '{:0>2}'.format(servidor[i].mesResolucao)
                   ato.anoResolucao = servidor[i].anoResolucao
                   ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                   ato.dia = '{:0>2}'.format(servidor[i].dia)
                   ato.mes = util.retornaMes(servidor[i].mes)
                   ato.ano = servidor[i].ano
                   ato.dataEfeito = ato.dia+'/'+ato.mes+'/'+ato.ano
                   ato.matricula = '{: <12}'.format(servidor[i].matricula.replace('.', ''))
                   #ato.cargo = '{: <48}'.format(servidor[i].cargo.upper()).replace('\n', ' ')
                   ato.cargo = '{: <48}'.format((servidor[i].cargo.upper()).replace('\n', ' ').replace('  ', ' ').replace('- ', '').strip(" "))
                   ato.CPF = '{: <13}'.format(servidor[i].CPF) #vER ESTA REGRA!!!!!
                   ato.tipocargo =  servidor[i].tipocargo
                   ato.simbolo = '{: <6}'.format(servidor[i].simbolo.replace('\n', ''))
                   print(ato.CPF, Tipo, ato.numero, ato.dataResolucao, 'NOMEAR   ',  ato.matricula, ato.nome, ato.dataEfeito, ato.cargo, ato.simbolo, ato.tipocargo, file=arq1)
                   persistencia.insert(ato.matricula, ato.nome, ato.dataResolucao, 'NOMEAR', ato.dataEfeito, ato.cargo, ato.tipocargo, ato.simbolo)

               servidor = LayoutAtos.atos_dispensar(self, buffer_local, Detalhe)
               for i in range(len(servidor)):
                   ato = Ato()
                   ato.nome = '{: <50}'.format((servidor[i].nome).replace('\n', ' ').replace('  ', ' ').strip(" "))
                   ato.numero = '{:0>4}'.format(servidor[i].numero)
                   ato.diaResolucao = '{:0>2}'.format(servidor[i].diaResolucao)
                   ato.mesResolucao = '{:0>2}'.format(servidor[i].mesResolucao)
                   ato.anoResolucao = servidor[i].anoResolucao
                   ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                   ato.dia = '{:0>2}'.format(servidor[i].dia)
                   ato.mes = util.retornaMes(servidor[i].mes)
                   ato.ano = servidor[i].ano
                   ato.dataEfeito = ato.dia+'/'+ato.mes+'/'+ato.ano
                   ato.matricula = '{: <12}'.format(servidor[i].matricula.replace('.', ''))
                   #ato.cargo = '{: <48}'.format(servidor[i].cargo.upper()).replace('\n', ' ')
                   ato.cargo = '{: <48}'.format((servidor[i].cargo.upper()).replace('\n', ' ').replace('  ', ' ').replace('- ', '').strip(" "))
                   ato.CPF = '{: <13}'.format(servidor[i].CPF) #vER ESTA REGRA!!!!!
                   ato.tipocargo =  servidor[i].tipocargo
                   ato.simbolo = '{: <6}'.format(servidor[i].simbolo.replace('\n', ''))
                   print(ato.CPF, Tipo, ato.numero, ato.dataResolucao, 'DISPENSAR',  ato.matricula, ato.nome, ato.dataEfeito, ato.cargo, ato.simbolo, ato.tipocargo, file=arq1)
                   persistencia.insert(ato.matricula, ato.nome, ato.dataResolucao, 'DISPENSAR', ato.dataEfeito, ato.cargo, ato.tipocargo, ato.simbolo)
 
               servidor = LayoutAtos.atos_exonerar(self, buffer_local, Detalhe)
               for i in range(len(servidor)):
                   ato = Ato()
                   ato.nome = '{: <50}'.format((servidor[i].nome).replace('\n', ' ').replace('  ', ' ').strip(" "))
                   ato.numero = '{:0>4}'.format(servidor[i].numero)
                   ato.diaResolucao = '{:0>2}'.format(servidor[i].diaResolucao)
                   ato.mesResolucao = '{:0>2}'.format(servidor[i].mesResolucao)
                   ato.anoResolucao = servidor[i].anoResolucao
                   ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                   ato.dia = '{:0>2}'.format(servidor[i].dia)
                   ato.mes = util.retornaMes(servidor[i].mes)
                   ato.ano = servidor[i].ano
                   ato.dataEfeito = ato.dia+'/'+ato.mes+'/'+ato.ano
                   ato.matricula = '{: <12}'.format(servidor[i].matricula.replace('.', ''))
                   #ato.cargo = '{: <48}'.format(servidor[i].cargo.upper()).replace('\n', ' ')
                   ato.cargo = '{: <48}'.format((servidor[i].cargo.upper()).replace('\n', ' ').replace('  ', ' ').replace('- ', '').strip(" "))
                   ato.CPF = '{: <13}'.format(servidor[i].CPF) #vER ESTA REGRA!!!!!
                   ato.tipocargo =  servidor[i].tipocargo
                   ato.simbolo = '{: <6}'.format(servidor[i].simbolo.replace('\n', ''))
                   print(ato.CPF, Tipo, ato.numero, ato.dataResolucao, 'EXONERAR ',  ato.matricula, ato.nome, ato.dataEfeito, ato.cargo, ato.simbolo, ato.tipocargo, file=arq1)
                   persistencia.insert(ato.matricula, ato.nome, ato.dataResolucao, 'EXONERAR', ato.dataEfeito, ato.cargo, ato.tipocargo, ato.simbolo)
  
               servidor = LayoutAtos.atos_designar(self, buffer_local, Detalhe, arqres)
               for i in range(len(servidor)):
                   ato = Ato()
                   ato.nome = '{: <50}'.format((servidor[i].nome).replace('\n', ' ').replace('  ', ' ').strip(" "))
                   #print(ato.nome)
                   ato.numero = '{:0>4}'.format(servidor[i].numero)
                   ato.diaResolucao = '{:0>2}'.format(servidor[i].diaResolucao)
                   ato.mesResolucao = '{:0>2}'.format(servidor[i].mesResolucao)
                   ato.anoResolucao = servidor[i].anoResolucao
                   ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
                   ato.dia = '{:0>2}'.format(servidor[i].dia)
                   ato.mes = util.retornaMes(servidor[i].mes)
                   ato.ano = servidor[i].ano
                   ato.dataEfeito = ato.dia+'/'+ato.mes+'/'+ato.ano
                   ato.matricula = '{: <12}'.format(servidor[i].matricula.replace('.', ''))
                   #ato.cargo = '{: <48}'.format(servidor[i].cargo.upper()).replace('\n', ' ')
                   ato.cargo = '{: <48}'.format((servidor[i].cargo.upper()).replace('\n', ' ').replace('  ', ' ').replace('- ', '').strip(" "))
                   ato.CPF = '{: <13}'.format(servidor[i].CPF) #vER ESTA REGRA!!!!!
                   ato.tipocargo =  servidor[i].tipocargo
                   ato.simbolo = '{: <6}'.format(servidor[i].simbolo.replace('\n', ''))
                   print(ato.CPF, Tipo, ato.numero, ato.dataResolucao, 'DESIGNAR ',  ato.matricula, ato.nome, ato.dataEfeito, ato.cargo, ato.simbolo, ato.tipocargo, file=arq1)
                   persistencia.insert(ato.matricula, ato.nome, ato.dataResolucao, 'DESIGNAR', ato.dataEfeito, ato.cargo, ato.tipocargo, ato.simbolo)
              

####### COMISSOES ########



    def comissoes(self, buffer, arquivo, arq, contarq, data_e_hora, arqres, perc, arq2):
        print('ARQUIVO========================================================>',arquivo,'(COMISSÕES)', perc,'%' )
        ################# PROCESSA CABEÇALHO DO DIARIO ################
        diario_pattern = re.compile('Ano\s([A-Z]*)\s•\sN\w\s([0-9]*)')        
        diario_edicao = diario_pattern.search(buffer)  

        diario_suplemento_pattern = re.compile('Diário Oficial do Município do Rio de Janeiro\s\|\s\w*\s\w*\s\|\s\w*\s\w*\s\|\s(Suplemento)')
        diario_suplemento = diario_suplemento_pattern.search(buffer)
        if diario_suplemento:
           tipo = 'SUPLEMENTAR' #Suplemento
        else:
           tipo = 'NORMAL' #Normal 

        util = Util()
        diario = Diario() 
        if (diario_edicao.group(1)):               
            diario.anoromano = '{: <6}'.format(((diario_edicao.group(1))))
            diario.ano = (util.converteRomano(diario_edicao.group(1)))
            diario.numero = '{:0>6}'.format((diario_edicao.group(2)))
            diario.tipo = '{: <12}'.format((tipo))
        else:
            diario.anoromano = 'XXXXXX'
            diario.ano = 'XXXXXX'
            diario.numero = 'XXXXXX'
            diario.tipo = 'XXXXXXXXXXXX'


        print('', file=arq2)
        print('(PUC-RIO/TECMF)   ::PROCESSAMENTO DO DIÁRIO::', 'ANO:', diario.ano,'No.:', diario.numero, 'TIPO:', diario.tipo, '* RIO DE JANEIRO * ARQUIVO:',arquivo.upper(), 'SEQ.:', '{:0>4}'.format(contarq), '                                             ',data_e_hora,  file=arq2)
        print('', file=arq2) 
            
        #############################################################
        
        resolucao_pattern = re.compile(r'^(RESOLUÇÃO|RESOLUÇAO)\s[A-Z0-9]+\sN.\s[0-9]+\sDE.*[\s|\n]+.*',re.M)
        contador = 1
        inicio = []
        bloco = []
        servidor = []
        tamanho = len(buffer)
        for resolucao in resolucao_pattern.finditer(buffer):
            inicio.append(resolucao.start())
            contador=contador + 1 
        inicio.append(tamanho)        
            

        for i in range(len(inicio)-1):
            bloco.append(inicio[i+1]-inicio[i])
            buffer_local = buffer[inicio[i]:inicio[i]+bloco[i]]
        
            
            ###### Resolução #####
            resolucao1_pattern = re.compile(r'^(?P<resolucao1>RESOLUÇÃO|RESOLUÇAO)\s(?P<detalhe_resolucao1>[A-Z0-9]+\sN.\s[0-9]+\sDE.*)[\s|\n]+.*',re.M)
            resolucao1 = resolucao1_pattern.search(buffer_local)
           
            if (resolucao1):
                #print(resolucao1.group('resolucao1'), resolucao1.group('detalhe_resolucao1'))
                Tipo = '{: <09}'.format(resolucao1.group('resolucao1'))
                Detalhe = resolucao1.group('detalhe_resolucao1')
            else:
                #print('Não casou resolucao1')
                Tipo = 'SEM TIPO'
                Detalhe = 'SEM DETALHE'
            #####################
            
            
            #### Gestor #####
            gestor_pattern = re.compile(r'(?P<gestor>[O|A]*\s(SECRETÁRI[O|A]+|PROCURADOR[A]*|PREFEITO[A]*|COORDENADOR[A]*)[A-ZÁÚÍÃÓÇÊÉ\s-]+)')
            gestor = gestor_pattern.search(buffer_local)
            if (gestor):
                Gestor = gestor.group('gestor')
            else:
                Gestor = 'SEM GESTOR'
            ###### Fim Gestor

            #### Detalhes da Comissão #####]
#            print('Arquivo->',arq)
#            if (arq == '3915.pdf'):
#                print(buffer_local)
            
            comissao1_pattern = re.compile(r'Art.\s[1-2]+.\sDesignar os membros abaixo indicados para comporem a (?P<nomeComissao>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\n\s\–]+)[\-|\–]*\sCONVÊNIO\sN\w\s(?P<convenio>[0-9\/]+)\n*\s*Titulares\n*\s*Órgão\s*Nome\s*Matrícula\n*')
            comissao2_pattern = re.compile(r'Art.\s[1-2]+.\sDesignar os membros abaixo indicados para comporem a (?P<nomeComissao>[A-ZÉÁÍÓÚÇÃÊÔÕÀÜa-záêéóíçãâôú\-\n\s\–]+):\n*\s*Titulares\n*\s*Órgão\s*Nome\s*Matrícula\n*')
            
            comissao1 = comissao1_pattern.search(buffer_local)
            comissao2 = comissao2_pattern.search(buffer_local)
            Detalhe2 = ''

            if (comissao1):
                #print('comissao 1')
                Detalhe2 = '<NomeComissao>'+comissao1.group('nomeComissao')+'<ConvenioComissao>'+comissao1.group('convenio')
            
            if (comissao2):
                #print('comissao 2')
                Detalhe2 = '<NomeComissao>'+comissao1.group('nomeComissao')+'<ConvenioComissao>'+'0000'
            
            
            
            ###### Fim Gestor


            
         ################################# RESOLUÇÕES COMPOSTAS #############################
           
            if ((resolucao1.group('resolucao1') == '*RESOLUÇÕES') or (resolucao1.group('resolucao1') == 'RESOLUÇÕES') or (resolucao1.group('resolucao1') == 'RESOLUÇOES') or (resolucao1.group('resolucao1') == 'RESOLUCOES') or (resolucao1.group('resolucao1') == 'PORTARIAS') ):
               print(resolucao1.group('resolucao1'))
 
        ######################## RESOLUÇÃO SIMPLES ########################### 
              
            elif ((resolucao1.group('resolucao1') == 'RESOLUÇÃO') or (resolucao1.group('resolucao1') == 'RESOLUÇAO') or (resolucao1.group('resolucao1') == 'RESOLUCAO') or (resolucao1.group('resolucao1') == 'DECRETO RIO') or (resolucao1.group('resolucao1') == 'PORTARIA')):

               ####### COMISSÃO ###############
               servidor = LayoutAtos.atos_criar_comissao(self, buffer_local, Detalhe, Detalhe2)
               for i in range(len(servidor)):
                   comissoes = Comissoes()
                   comissoes.nome = '{: <43}'.format((servidor[i].nome).replace('\n', ' ').replace('  ', ' ').strip(" "))
                   comissoes.numero = '{:0>4}'.format(servidor[i].numero)
                   comissoes.diaResolucao = '{:0>2}'.format(servidor[i].diaResolucao)
                   comissoes.mesResolucao = '{:0>2}'.format(servidor[i].mesResolucao)
                   comissoes.anoResolucao = servidor[i].anoResolucao
                   comissoes.dia = '{:0>2}'.format(servidor[i].dia)
                   comissoes.mes = util.retornaMes(servidor[i].mes)
                   comissoes.ano = servidor[i].ano
                   comissoes.matricula = '{: <13}'.format(servidor[i].matricula)
                   comissoes.nomeComissao = '{: <68}'.format(servidor[i].nomeComissao.replace('\n', ' ').replace('  ', ' '))
                   comissoes.convenio = '{: <9}'.format(servidor[i].convenio)
                   comissoes.CPF = '{: <13}'.format(servidor[i].CPF) #vER ESTA REGRA!!!!!
                   comissoes.tipocargo =  servidor[i].tipocargo
                   comissoes.orgao = '{: <10}'.format(servidor[i].orgao)
                   print(comissoes.CPF, Tipo, comissoes.numero, comissoes.diaResolucao,'/',comissoes.mesResolucao,'/',comissoes.anoResolucao, 'DESIGNAR ', comissoes.orgao, comissoes.nome, comissoes.matricula, comissoes.nomeComissao, comissoes.convenio, comissoes.tipocargo, file=arq2)
                   
  





######################### SEM USO ##########################            
            
    
    def do_exoneracao(self, buffer, arquivo):
  
        
        resolucao_pattern = re.compile(r'(RESOLUÇÃO|PORTARIAS|DECRETO RIO)\s*“P”\sN\w*\s*(\d+)\s*DE\s*(\d+)(?!dd\/dd\/dddd)\s*DE\s*([A-Z]+)\s*DE\s*(\d+)\s*')
        resolucao = resolucao_pattern.search(buffer)
        
        contador = 1
        while (resolucao):
            print(contador)
            print(arquivo)
            contador = contador + 1
          
            ind_headergestor = resolucao.end()
            buffer = buffer[ind_headergestor:]
            header_gestor_pattern = re.compile(r'((?:.|\n.)+)\n\n')
            header_gestor = header_gestor_pattern.search(buffer)
            if header_gestor:
                print("========= Gestor ==========") 
                print(header_gestor.group(1))
            else: print("NÃO Casou gestor")
            ind_content = header_gestor.end()
            buffer = buffer[ind_content:]
            
            
            #atribuicao_pattern = re.compile(u'(?P<nome>Exonerar)[,/s]+ (?!a pedido,) (?!os servidores abaixo relacionados)')
            atribuicao_pattern = re.compile(u'(RESOLVE[:]*\nNomear(?!Relotar))')
            atribuicao = atribuicao_pattern.search(buffer)
            print(atribuicao)

            if atribuicao:
                print("===Atribuicao====")
                
                print('Entrou no if da atribuicao')
                print('Ação->'+atribuicao.group(1))
                #print('Servidor->'+atribuicao.group(2))
                ind_next_buffer_position = atribuicao.end()
                
                #buffer = buffer[ind_next_buffer_position:] 
                #header_resol = header_pattern.search(buffer)
            else: 
                print("NAO CASOU ATRIBUICAO")
                print('Entrou no else da atribuicao')
                buffer = buffer[ind_next_buffer_position:] 
                resolucao = resolucao_pattern.search(buffer)
            print('Entrou no fim do while')
            buffer = buffer[ind_next_buffer_position:] 
            resolucao = resolucao_pattern.search(buffer)

        print("Não Casou Resolução")
        print('Fim do script')
        

    def do_nomeacao(self, buffer, arquivo):
  
        
        resolucao_pattern = re.compile(r'(RESOLUÇÃO|DECRETO RIO)\s*“P”\sN\w*\s*(\d+)\s*DE\s*(\d+)\s*DE\s*([A-Z]+)\s*DE\s*(\d+)\s*')
        resolucao = resolucao_pattern.search(buffer)
        
        contador = 1
        while (resolucao):
            #print(contador)
            #print(arquivo)
            contador = contador + 1
          
            ind_headergestor = resolucao.end()
            buffer = buffer[ind_headergestor:]
            header_gestor_pattern = re.compile(r'((?:.|\n.)+)\n\n')
            header_gestor = header_gestor_pattern.search(buffer)
            if header_gestor:
                print("========= Gestor ==========") 
                print(header_gestor.group(1))
            else: print("NÃO Casou gestor")
            ind_content = header_gestor.end()
            buffer = buffer[ind_content:]

            
            #resolucao1_pattern = re.compile(u'(?P<acao>Nomear)(?!a pedido)\s(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+)[,\s]*')
            resolucao1_pattern = re.compile(u'(?P<acao>Nomear)')
            
            resolucao = resolucao1_pattern.search(buffer)
            if resolucao:
                print("===Atribuicao====")
                print('Ação->'+resolucao.group('acao'))
                #print('Servidor->'+resolucao.group('nome'))
                ind_next_buffer_position = resolucao.end()
                #buffer = buffer[ind_next_buffer_position:] 
                #header_resol = header_pattern.search(buffer)
            else: print("NAO CASOU ATRIBUICAO")
                #g.add( (donna, RDF.type, FOAF.Person) )       
                #else: print("NÃO Casou content") 
            buffer = buffer[ind_next_buffer_position:] 
            resolucao = resolucao_pattern.search(buffer)
        print("Não Casou Resolução")
