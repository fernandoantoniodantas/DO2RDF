#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:27:24 2019

@author: Fernando
@author: Hermann
Esta classe é responsável por fazer a persistencia dos dados extraídos do diário e gravar no banco de dados.
"""

from ConnectionFactory import ConnectionFactory 

class RioJaneiroDAO:
    
    def gravaDiario(self, diario):
        cur = ConnectionFactory()
        conn = cur.get_connection()
        conexao = conn.cursor()
        conexao.execute("INSERT INTO dorj.diarios (numero, tipo, anoromano, ano, datadiario, datagravacao, nomearquivo, identidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (diario.numero, diario.tipo, str(diario.anoromano), diario.ano, diario.datadiario, diario.datagravacao, diario.nomearquivo, diario.identidade ))
        conn.commit()
