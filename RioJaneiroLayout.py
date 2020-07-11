#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:18:50 2019

@@author: Fernando
@author: Hermann

Classe que herda Layout, faz buffer das partições do diário e executa a busca com base nos padrões.

"""
from Layout import Layout
from Util import Util
from UtilRegex import UtilRegex
from Diario import Diario
from RioJaneiroDAO import RioJaneiroDAO

t = u"u00b0"

import re

class RioJaneiroLayout(Layout):    
   
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
               
        
    def teste(self, buffer, arquivo):
        resolucao_pattern = re.compile(r'(RESOLUÇÃO|PORTARIAS|DECRETO RIO)\s*“P”\sN\w*\s*(\d+)\s*DE\s*(\d+)\s*DE\s*([A-Z]+)\s*DE\s*(\d+)\s*')
        contador = 1
        for resolucao in resolucao_pattern.finditer(buffer):
            print(resolucao, contador, arquivo)
            contador = contador + 1
            #### Tratando ogestor ####
            IndheaderGestor = resolucao.end()
            print(resolucao.span())
            bufferGestor = buffer[IndheaderGestor:]
            headerGestor_pattern = re.compile(r'^O\s((SECRETÁRIO|O PROCURADOR|O PREFEITO)[A-ZÁÚÍ\s-]+)')
            #headerGestor_pattern = re.compile(r'^[A-Z\sÁÚÍ-]+')
            #headerGestor_pattern = re.compile(r'((?:.|\n.)+)\n\n')
            headerGestor = headerGestor_pattern.search(bufferGestor)##>100
            if (headerGestor):
                print(headerGestor)
                
                bufferGeral = buffer[IndheaderGestor:IndheaderGestor+500]
                headerGeral_parttner = re.compile(u'(Nomear)\s*(, a pedido,\s)?((?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ]|\s)+)')
                
                headerGeral = headerGeral_parttner.search(bufferGeral)
                if (headerGeral):
                    print(headerGeral.group(1))
                    print(headerGeral.group(3))
                    print('-------')
                    #bufferGeral2 = bufferGeral[]
                else:
                    print('Não casou Geral')
                    #print(bufferGeral) #Para debugar o motivo do não casamento
            else:
                print('Não casou Gestor')
                
#Nomear SILVIO ROBERTO MACEDO LEAL JUNIOR, matrícula
#11/241.355-7, Arquiteto, para exercer o Cargo em Comissão de Gerente I,
#símbolo DAS-08, código 072969, da Gerência de Análise Urbano
#Ambiental, da Coordenadoria de Licenciamento de Projetos Sociais,
#da Coordenadoria Geral de Integração Técnica, da Subsecretaria de
#Habitação, da Secretaria Municipal de Infraestrutura e Habitação.        
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
          
#            if content:
#               print("========== Content ==========") 
               #print(content)
               #textoregComissionado = u'[\d+\s-]*\s*(Nomear|Exonerar)[,|\s]*((?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ’]|\s)+)[,|\s]*[M|m]atrícula\s([0-9/.-]+)[,|\s]*(?:[a-zA-ZÉÁÍÓÚÇÃÊÔÕÀÜa-zéáíóúçaãêôõà,]|\s)+(\d+)\s[DE|de]+\s+([a-z]+)\s+[de|DE]+\s+([0-9]+)[,|\s]*do [C/c]argo em [C|c]omissão[\s|de]+([A-Za-z\s]+)[,|\s]*símbolo\s+([A-Z0-9-]+)' 
#               textoregComissionado = u'(Exonerar)[,|\s]*[a pedido,]*((?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ’]|\s)+)[,|\s]*[m|M]atrícula\s+([0-9/.-]+),.*com validade a partir de\s*([0-9]+)\s*de\s*([A-Za-z]+)\s*de\s*([0-9]+), do [C|c]argo em [C|c]omissão\s*[de]*\s*([A-Za-z\s]+),\ssímbolo\s([A-Z0-9-]+)' 
               #textoregComissionado = u'(?P<acao>Exonerar)[a-z\s,]+(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+),\s((matrícula)\s|([A-Za-zí\s,]+))(?P<matricula>[0-9/.-]+),\s[A-Za-z,\s]*(com validade a partir de|com eficácia a contar de)\s(?P<dia>[\d]+)[º\s]*de\s(?P<mes>[a-zç]+)\sde\s(?P<ano>[\d]+),' ]
               #textoregComissionado = u'(?P<acao>Exonerar)[,\s]*(a pedido)?[,\s]*(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+)[,\s]*((matrícula)?\s?([0-9/.-]+)?[,\s]*)?([A-Za-zíã\sº]*[,\s]*)((com validade a partir de)?\s?([0-9]+)?[º]?)((matrícula [nº]*)?\s?([0-9/.-]+)?)'
               #textoregComissionado = u'(?P<acao>Exonerar)[,\s]*(a pedido)?[,\s]*(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+)[,\s]*((matrícula)?\s?([0-9/.-]+)?[,\s]*)?([A-Za-zíã\sº]*[,\s]*)((com validade a partir de)?\s?([0-9]+)?[º]?\s(de\s)?((matrícula [nº]*)?\s?([0-9/.-]+)?[,\s]*)?(?P<mes>[a-zç]+)?)((matrícula [nº]*)?\s?([0-9/.-]+)?)'
               #textoregComissionado = u'(?P<acao>Exonerar)[,\s]*(a pedido)?[,\s]*(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+)[,\s]*((matrícula)?\s?([0-9/.-]+)?[,\s]*)?([A-Za-zíã\sº]*[,\s]*)((com validade a partir de)?\s?([0-9]+)?[º]?\s(de\s)?((matrícula [nº]*)?\s?([0-9/.-]+)?[,\s]*)?(?P<mes>[a-zç]+)?)((matrícula [nº]*)?\s?([0-9/.-]+)?)\s(de\s)?([0-9]+)?(,\sdo\s)?([c|C]argo em [c|C]omissão (de )?)?(eficácia a contar de)?'
               #textoregComissionado = u'(?P<acao>Exonerar)[,\s]*(a pedido)?[,\s]*(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+)[,\s]*((matrícula)?\s?([0-9/.-]+)?[,\s]*)?([A-Za-zíã\sº]*[,\s]*)((com validade a partir de)?\s?([0-9]+)?[º]?\s(de\s)?((matrícula [nº]*)?\s?([0-9/.-]+)?[,\s]*)?(?P<mes>[a-zç]+)?)((matrícula [nº]*)?\s?([0-9/.-]+)?)\s(de\s)?([0-9]+)?(,\sdo\s)?([c|C]argo em [c|C]omissão (de )?)?(eficácia a contar de)?'
               #textoregComissionado = u'(?P<acao>Exonerar)[,\s]*(a pedido)?[,\s]*(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+)[,\s]*((matrícula)?\s?([0-9/.-]+)?[,\s]*)?([A-Za-zíã\sº]*[,\s]*)((com validade a partir de)?\s?([0-9]+)?[º]?\s(de\s)?((matrícula [nº]*)?\s?([0-9/.-]+)?[,\s]*)?(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)?)((matrícula [nº]*)?\s?([0-9/.-]+)?)\s(de\s)?([0-9]+)?(,\sdo\s)?([c|C]argo em [c|C]omissão (de )?)?(com eficácia a contar de)?(\s)?([0-9]+)?\s?[º]?\s?(de\s)?([a-zç]+)?\s?de?\s([0-9]+)?([,\s]+)?(do [c|C]argo em [c|C]omissão (de )?)?(?P<cargo>[A-Za-z\s]+)[,\s]+símbolo\s(?P<simbolo>[A-Z-0-9]+)'
               #textoregComissionado = u'(?P<acao>Exonerar)[,\s]*(a pedido)?[,\s]*(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+)[,\s]*((matrícula)?\s?([0-9/.-]+)?[,\s]*)?([A-Za-zíã\sº]*[,\s]*)((com validade a partir de)?\s?([0-9]+)?[º]?\s(de\s)?((matrícula [nº]*)?\s?([0-9/.-]+)?[,\s]*)?(?P<mes>janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)?)((matrícula [nº]*)?\s?([0-9/.-]+)?)\s(de\s)?([0-9]+)?(,\sdo\s)?([c|C]argo em [c|C]omissão (de )?)?(com eficácia a contar de)?(\s)?([0-9]+)?\s?[º]?\s?(de\s)?([a-zç]+)?\s?(de\s)?([0-9]+)?(,\sdo\s)?([c|C]argo em [c|C]omissão de )?'
#               textoregComissionado = u'(?P<acao>Exonerar)(?!a pedido)\s(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+)[,\s]*'
#               atribuicaoResolucao_pattern = re.compile(textoregComissionado)
#               atribuicaoResolucao = atribuicaoResolucao_pattern.search(buffer)
               
               #RESOLVE Exonerar EDUARDO AVEIRO DA SILVEIRA, matrícula 60/304.868-3, com validade a partir de 20 de maio de 2019, do Cargo em Comissão de Assistente I, símbolo DAS-06, código 073448, do Gabinete do Prefeito.
               #RESOLVE Exonerar CHARLES CHAPLIM DA PAZ BENTES, matrícula 11/224.063-8, Fisioterapeuta, com validade a partir de 29 de abril de 2019, do Cargo em Comissão Assistente I, símbolo DAS-06, código 073647
               #RESOLVE Exonerar, a pedido, SANDRA MARIA BRAGA PASSOS LIMA, matrícula 70/302.703-4, com validade a partir de 9 de maio de 2019, do Cargo em Comissão de Diretor IV, símbolo DAS-06
               #RESOLVE Nomear DANIELA DE ALBUQUERQUE SÁ MATTA SCHUCHMANN, com validade a partir de 20 de maio de 2019, para exercer o Cargo em Comissão de Assistente I, símbolo DAS-06, código 073448, do Gabinete do Prefeito.
               #RESOLVE Nomear MARCO ANTONIO CARDOSO DA COSTA, matrícula 11/231.480-5, Agente Educador II, com validade a partir de 24 de abril de 2019, para exercer o Cargo em Comissão de Assessor III, símbolo DAS-07, 
               #RESOLVE Nomear FLÁVIA FERREIRA DE OLIVEIRA, matrícula 11/285.946-0, Professor de Ensino Fundamental, com validade a partir de 6 de maio de 2019, para exercer o Cargo em Comissão de Gerente II, símbolo DAS-07,
               #RESOLVE Designar SEBASTIANA DE FREITAS, matrícula 12/085.305-1, Merendeira, para exercer a Função Gratificada de Subgerente III, símbolo DAI-06, 
               #RESOLVE Exonerar, a pedido, RENATA SEABRA GARRÃO, PROFESSOR I, matrícula 11/249945-7, com eficácia a contar de 11 de abril de 2019, do Cargo em Comissão de DIRETOR IV, símbolo DAS-06, código 5260, setor 11539 da 1ª Coordenadoria Regional de Educação, desta Secretaria. (ref. ao processo no 07/002956/2019).
               #print(atribuicaoResolucao.span())
               

#               if (atribuicaoResolucao):                   
                 #print('Ação->'+atribuicaoResolucao.group('acao'))
                 #print('Servidor->'+atribuicaoResolucao.group('nome'))
                 #print('Matr->'+atribuicaoResolucao.group(4))
                 #print('Dia->'+atribuicaoResolucao.group(8))
                 #print('Mes->'+atribuicaoResolucao.group('mes'))
                 #print('Ano->'+atribuicaoResolucao.group('ano'))                 
                 
               #else: print("NAO CASOU ATRIBUICAO")              
             
#            else: print("NAO CASOU CONTENT")
            #ind_next_buffer_position = atribuicaoResolucao.end()
            #buffer = buffer[ind_next_buffer_position:] 
            #resolucao = resolucao_pattern.search(buffer)
            #print(resolucao.span())
            #print('Boffer 2->'+resolucao.span())               

            

#Exonerar EDUARDO AVEIRO DA SILVEIRA, matrícula 60/304.868-3,
#com validade a partir de 20 de maio de 2019, do Cargo em Comissão de
#Assistente I, símbolo DAS-06, código 073448, do Gabinete do Prefeito.


#        while (resolucaoSME):
#            print(arquivo)
#            print(resolucaoSME.group(1)) 
            #textoreg = u'\d+\s-\s*(Nomear|Exonerar|Aposentar|Dispensar|Designar|Dispensar)[\,|\s]*[a pedido,\s+]*((?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ]|\s)+),' 
#            textoreg = u'\d+\s-\s*(Nomear|Exonerar|Aposentar|Dispensar|Designar|Dispensar),' 
            
            #textoreg = u'\d+\s-\s*(Nomear|Exonerar|Aposentar|Dispensar|Designar)[a pedido,\s+]*((?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ]|\s)+),\s((?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ]+|\s)+),\s+[M|m]atrícula\s([0-9\/-]+),\s[a-zá\s,]+\s([0-9]+)\sde\s([a-z]+)\s*de\s*([0-9]+),\s*[a-z\s*]+\s\s+(Cargo em Comissão|Função Gratificada)\s+de\s+([A-ZÉÁÍÓÚÇÃÊÔÕÀÜ\s*]+)[,\s+símbolo]+\s+([A-Z0-9-]+)'
            #textoreg = u'(Exonerar)'
#            atribuicaoSME_pattern = re.compile(textoreg)
#            atribuicaoSME = atribuicaoSME_pattern.search(buffer)
#            if (atribuicaoSME):
#               print('Ação->'+atribuicaoSME.group(1))
               #print('Ação->'+atribuicaoSME.group(1))
               #print('Servidor->'+atribuicaoSME.group(2))
               #print('Cargo Efetivo->'+atribuicaoSME.group(3))
               #print('Matr->'+atribuicaoSME.group(4))
               #print('Dia->'+atribuicaoSME.group(5))
               #print('Mes->'+atribuicaoSME.group(6))
               #print('Ano->'+atribuicaoSME.group(7))
               #print('TipoCargo->'+atribuicaoSME.group(8))
               #print('Cargo ou Função Gratificada->'+atribuicaoSME.group(9))
               #print('Símbolo->'+atribuicaoSME.group(10))
#               print('--------------')
#            ind_next_buffer_positionSME = atribuicaoSME.end()
#            buffer = buffer[ind_next_buffer_positionSME:] 
#            resolucaoSME = resolucaoSME_pattern.search(buffer)


#        while (portaria):
#            print(arquivo)
#            print(portaria.group(1))
#            atribuicaoPortaria_pattern = re.compile(u'(Nomear|Exonerar|Aposentar|Dispensar|Designar)\s((?:[A-ZÉÁÍÓÚÇÃÊÔÕÀÜ]|\s)+),([m,M]atrícula)\s([0-9\/.-]+)')
#            atribuicaoPortaria = atribuicaoPortaria_pattern.search(buffer)
#            if (atribuicaoPortaria.group(0)):
#               print('Ação->'+atribuicaoPortaria.group(1))
#               print('Servidor->'+atribuicaoPortaria.group(2))
#               print('Matr->'+atribuicaoPortaria.group(3))
               #matricula_portaria_pattern = re.compile(u'([m,M]atrícula)\s([0-9\/.-]+)')
               #matriculaPortaria = matricula_portaria_pattern.search(buffer)
               #print('Matr->'+matriculaPortaria.group(2))
#               print('--------------')
#            ind_next_buffer_position_Portaria = atribuicaoPortaria.end()
#            buffer = buffer[ind_next_buffer_position_Portaria:] 
#            portaria = portaria_pattern.search(buffer)


#marcelo fagundes felix
#PEG

#(Nomear|Exonerar|Aposentar|Dispensar)\s([A-ZÉÁÍÓÚÇÃÊÔÕÀÜ]|\s)+,\s([A-ZÉÁÍÓÚÇÃÊÔÕÀÜ]|\s)+,\s[m|M]atrícula\s([0-9/-]+),

#RESOLVE:
#No 2548 - Dispensar, a pedido, MÁRCIA LINHARES COSTA FREITAS, PROFESSOR II, matrícula 12/105649-8,
#da Função Gratificada de DIRETOR ADJUNTO, símbolo DAI-06, código 5607, setor 10860 da 2a Coordenadoria
#Regional de Educação, desta Secretaria. (ref. ao processo n o 07/02/003089/2019).
               
#RESOLVE:
#No 2520 - Exonerar, a pedido, ANA MARIA PRAZERES DA GUI
#No 2521 - Dispensar, a pedido, ANA ROSA MOUTELA DE OLIVEIRA,

#RESOLVE:
##No 2575 - Dispensar, a pedido, REINALDO VARGAS AUGUSTO,
#PROFESSOR I, matrícula 12/106455-9, com eficácia a contar de 11 de
#outubro de 2019, da Função Gratificada de CHEFE I, símbolo DAI-06,
#código 7321, setor 11632 da 7a Coordenadoria Regional de Educação,
#desta Secretaria. (ref. ao processo n o 07/07/003409/2019).



#No 483 - Designar MICHELI MELO DA SILVA DE ARAÚJO, PROFESSOR II,
#matrícula 10/265751-8, para exercer, com eficácia a contar de 1o
#de fevereiro de 2019, a Função Gratificada de COORDENADOR
#PEDAGÓGICO, símbolo DAI-06, código 5163, setor 11225 da 1a Coor-
#denadoria Regional de Educação, desta Secretaria. (ref. ao processo n o
#07/000596/2019).

#Onde se lê: “Designar ELIÂNGELA ARAÚJO RODRIGUES, PROFESSOR DE ENSINO FUNDAMENTAL,
#matrícula 10/290721-0, para exercer a Função Gratificada de DIRETOR ADJUNTO...”.
#Leia-se: “Designar ELIÂNGELA ARAÚJO RODRIGUES, PROFESSOR DE ENSINO FUNDAMENTAL, matrícula
#10/290721-0, para exercer, com eficácia a contar de 2 de agosto de 2019, a Função Gratificada de DIRETOR
#ADJUNTO...”.


#No 1369 - Nomear CARLA GOMES PETRUNGARO, PROFESSOR II,
##matrícula 10/201076-7, para exercer, com eficácia a contar de 15 de maio
#de 2019, o Cargo em Comissão de DIRETOR IV, símbolo DAS-06, código
#28951, setor 18641 da 1a Coordenadoria Regional de Educação, desta
#Secretaria. (ref. ao processo n o 07/003771/2019).


#No 2784 - Dispensar ELAINE MARIA MENDES SENA, PROFESSOR I,
#matrícula 12/264512-5, com eficácia a contar de 11 de abril de 2018, da
#Função Gratificada de COORDENDOR PEDAGÓGICO, símbolo DAI-06,
#código 8195, setor 11102 da 9a Coordenadoria Regional de Educação,
#desta Secretaria (ref. ao processo n°07/09/000874/2018) diario 3732.pdf



        #RESOLUÇÃO “P” No 1929 DE 22 DE MAIO DE 2019
        #DECRETO RIO “P” No 3498 DE 22 DE AGOSTO DE 2017
       # RESOLUÇÕES SME “P” DE 17 DE ABRIL DE 2018.
#            print("====== Resol =======")
#    print("Resolução #"+header_resol.group(1))
#    if header_resol.group(2) and header_resol.group(3) and header_resol.group(4):
##      print("Data "+header_resol.group(2)+" de "+header_resol.group(3)+" de "+header_resol.group(4))
#    else: print("Data invalida")
#    ind_headergestor = header_resol.end()
#    buffer = buffer[ind_headergestor:]
#    header_gestor_pattern = re.compile(r'((?:.|\n.)+)\n\n')
#    header_gestor = header_gestor_pattern.search(buffer)
    
    
#No 076 - Nomear RACHEL CRISTINA DOS SANTOS DE SOUZA LIMO-
#EIRO, PROFESSOR II, matrícula 10/260111-0, para exercer, com eficá-
#cia a contar de 16 de maio de 2017, o Cargo em Comissão de DIRETOR
#IV, símbolo DAS-06, código 006469, setor 11308 da 11a Coordenadoria
#Regional de Educação, da Secretaria Municipal de Educação e conside-
#rá-la dispensada da Função Gratificada de DIRETOR-ADJUNTO, símbo-
#lo DAI-06, código 006470, setor 11308 da 11a Coordenadoria Regional
#de Educação, desta Secretaria. (ref. ao processo n° 07/11/000480/2017)    
    
    
    
#RESOLUÇÃO “P” No 330 DE 21 DE JANEIRO DE 2019
#O SECRETÁRIO CHEFE DA SECRETARIA MUNICIPAL DA CASA CIVIL, no uso das atribuições que lhe são
#conferidas pela legislação em vigor,
#RESOLVE
#Nomear CARLOS ANTÔNIO RIBEIRO PEREIRA, com validade a partir de 1o. de janeiro de 2019, para exercer
#o Cargo em Comissão de Assistente I, símbolo DAS-06, código 075151, da Coordenadoria Geral de Ações de
#Cidadania, da Subsecretaria de Relações Institucionais, da Secretaria Municipal da Casa Civil.

#(?P<acao>Exonerar)[a-z\s,]+(?P<nome>[A-ZÁÉÍÓÚÃÕ\s]+),\s((matrícula)\s|([A-Za-zí\s,]+))(?P<matricula>[0-9/.-]+),\s[A-Za-z,\s]*(com validade a partir de|com eficácia a contar de)\s(?P<dia>[\d]+)[º\s]*de\s(?P<mes>[a-zç]+)\sde\s(?P<ano>[\d]+),\sdo\s[C|c]argo em [C|c]omissão de\s(?P<cargo>[A-Za-z\s]+),\ssímbolo\s(?P<simbolo>[A-Z0-9-]+)

# """       

