#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:38:03 2020

@author: Fernando
@author: Hermann

Classe de testes unitários. Esta classe detecta se as expressões regulares estão reconhecendo os padrões implementados na classe Layout.py.
Além do casamento de padrôes, foram testados, atravéz de self.assertEqual da classe unittest, se as listas retornam as informações corretas como: nome, cargo e natrícula nos atos de nomeações, exonerações e designações.
Case1, Case2 e Case3 representam um string buffer (partes do diário) como casos de testes do teste unitário.
Foram testados os seguintes comportamentos:
layout.atos_nomeacao()
layout.atos_exonerar()
layout.atos_designacoes()
    
"""

import unittest
from LayoutAtos import LayoutAtos
from Ato import Ato


def buildListCase1():
    obj = []
    ato = Ato()
    ato.numero = '83'  
    ato.diaResolucao = '3'
    ato.mesResolucao = '1'
    ato.anoResolucao = '2013'
    ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
    ato.nome = 'ANA WAKSBERG GUERRINI'
    ato.cargo = 'Gestor'
    ato.dia = '01'
    ato.mes = '01'
    ato.ano = '2013'
    ato.matricula = '60/272.922-6'
    ato.simbolo = 'DAS-10.A'
    ato.tipocargo = 'CC' 
    obj.append(ato)    
    
    return obj

def buildListCase2():
    obj = []
    ato = Ato()
    ato.numero = '83'  
    ato.diaResolucao = '3'
    ato.mesResolucao = '1'
    ato.anoResolucao = '2013'
    ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
    ato.nome = 'GUSTAVO MIRANDA RODRIGUES'
    ato.cargo = 'Gestor'
    ato.dia = '01'
    ato.mes = '01'
    ato.ano = '2013'
    ato.matricula = '11/156.395-6'
    ato.simbolo = 'DAS-10.A'
    ato.tipocargo = 'CC' 
    obj.append(ato)    
    
    return obj


def buildListCase3():
    obj = []
    ato = Ato()
    ato.numero = '88'  
    ato.diaResolucao = '1'
    ato.mesResolucao = '2'
    ato.anoResolucao = '2019'
    ato.dataResolucao = ato.diaResolucao+'/'+ato.mesResolucao+'/'+ato.anoResolucao
    ato.nome = 'MAURÍCIO OLIVEIRA CHAVES'
    ato.cargo = 'COORDENADOR PEDAGÓGICO'
    ato.dia = '01'
    ato.mes = '02'
    ato.ano = '2019'
    ato.matricula = '10/285208-5'
    ato.simbolo = 'DAI-06'
    ato.tipocargo = 'CC' 
    obj.append(ato)    
    
    return obj




case1 = 'Nomear ANA WAKSBERG GUERRINI, matrícula 60/272.922-6, com validade a partir de 1o de janeiro de 2013, para exercer o Cargo em Comissão de Gestor, símbolo DAS-10.A, código 035078, da Central de Teleatendimento da PCRJ - Central 1746, da Secretaria Municipal da Casa Civil.'
case11 = '83 DE 03 DE JANEIRO DE 2013'

case2 = 'Exonerar, a pedido, GUSTAVO MIRANDA RODRIGUES, matrícula 11/156.395-6, Fiscal de Atividades Econômicas, com validade a partir de 1o de janeiro de 2013, do Cargo em Comissão de Gestor, símbolo DAS-10.A, código 035078, da Central de Teleatendimento da PCRJ Central 1746, da Secretaria Municipal da Casa Civil.'
case22 = '83 DE 03 DE JANEIRO DE 2013'

case3= 'No 497 - Designar MAURÍCIO OLIVEIRA CHAVES, PROFESSOR DE ENSINO FUNDAMENTAL, matrícula 10/285208-5, para exercer, com eficácia a contar de 1o de fevereiro de 2019, a Função Gratificada de COORDENADOR PEDAGÓGICO, símbolo DAI-06, código 7835, setor 11075 da 8a Coordenadoria Regional de Educação, desta Secretaria. (ref. ao processo n o 07/08/000375/2019).'
case33 = '01 DE FEVEREIRO DE 2019'


class TestesUnitarios(unittest.TestCase):
    
    def testNomearNome(self):
        layout = LayoutAtos()
        servidor = []
        servidor = layout.atos_nomeacao(case1, case11)
        servidorDest = buildListCase1()    
        self.assertEqual(servidor[0].nome, servidorDest[0].nome)


    def testNomearCargo(self):
        layout = LayoutAtos()
        servidor = []
        servidor = layout.atos_nomeacao(case1, case11)
        servidorDest = buildListCase1()    
        self.assertEqual(servidor[0].cargo, servidorDest[0].cargo)

    def testNomearMatricula(self):
        layout = LayoutAtos()
        servidor = []
        servidor = layout.atos_nomeacao(case1, case11)
        servidorDest = buildListCase1()    
        self.assertEqual(servidor[0].matricula, servidorDest[0].matricula)

    def testExonerarNome(self):
        layout = LayoutAtos()
        servidor = []
        servidor = layout.atos_exonerar(case2, case22)
        servidorDest = buildListCase2()    
        self.assertEqual(servidor[0].nome, servidorDest[0].nome)


    def testExonerarCargo(self):
        layout = LayoutAtos()
        servidor = []
        servidor = layout.atos_exonerar(case2, case22)
        servidorDest = buildListCase2()    
        self.assertEqual(servidor[0].cargo, servidorDest[0].cargo)

    def testExonerarMatricula(self):
        layout = LayoutAtos()
        servidor = []
        servidor = layout.atos_exonerar(case2, case22)
        servidorDest = buildListCase2()    
        self.assertEqual(servidor[0].matricula, servidorDest[0].matricula)



    def testDesignarNome(self):
        layout = LayoutAtos()
        servidor = []
        servidor = layout.atos_designacoes(case3, case33)
        servidorDest = buildListCase3()    
        self.assertEqual(servidor[0].nome, servidorDest[0].nome)


    def testDesignarMatricula(self):
        layout = LayoutAtos()
        servidor = []
        servidor = layout.atos_designacoes(case3, case33)
        servidorDest = buildListCase3()    
        self.assertEqual(servidor[0].matricula, servidorDest[0].matricula)


if __name__ == '__main__':
    unittest.main()
    
