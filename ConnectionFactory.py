#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:00:56 2019

@author: Fernando
@author: Hermann

Implementa uma fabrica de conexões para o banco de dados PostgreSql.

"""
import psycopg2

class ConnectionFactory:
    
    @staticmethod
    def get_connection():
       conn = psycopg2.connect(host='localhost', database='diario', user='postgres', password='020573')
       return conn