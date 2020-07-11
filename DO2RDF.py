#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:47:55 2020

@author: Fernando
@author: Hermann

Este script faz o parser do banco de dados para triplas RDF.

"""

import psycopg2 # para o PostgreSQL
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF, OWL
n = Namespace("http://www.w3.org/2006/time#")
n.Person # as attribute




# Bind a few prefix, namespace pairs for pretty output
store = Graph()

store.bind("dc", DC)
store.bind("foaf", FOAF)
store.bind("owl", OWL)


aa = 'XXX'

####### Database
conn = psycopg2.connect(host='localhost', database='diario', user='postgres', password='020573')
cur = conn.cursor()
cur.execute("select matricula, nome, datapublicacao, acao, dataefeito, cargo, tipocargo, simbolo  from dorj.atos where id >= 13001 and id <= 15000 order by 2")
pessoas_records = cur.fetchall() 

tamanho = len(pessoas_records)

seqa=0
for row in pessoas_records:
    #print("Id = ", row[0], )
    seqa+=1
    
    idP = seqa
    idP = BNode()
    # Add triples using store's add method.
    store.add((idP, RDF.type, FOAF.Person))
    store.add((idP, FOAF.openid, Literal(row[0].strip())))#matrícula
    store.add((idP, FOAF.name, Literal(row[1].strip())))#nome do servidor
    store.add((idP, FOAF.title, Literal(row[2])))#Data da Publicação
    store.add((idP, FOAF.knows, Literal(row[3].strip())))#Operação (NOMEAR, EXONERAR, DESIGNAR, etc...)
    store.add((idP, FOAF.member, Literal(row[4])))#Data do efeito
    store.add((idP, FOAF.familyName, Literal(row[5].strip())))#Cargo
    store.add((idP, FOAF.givenName, Literal(row[6].strip())))#Tipo do Cargo
    store.add((idP, FOAF.made, Literal(row[7].strip())))#Símbolo do cargo


    # Iterate over triples in store and print them out.
    #print("--- printing raw triples ---")
    #for s, p, o in store:
    #    print(s, p, o)



    # For each foaf:Person in the store print out its mbox property.
    #print("--- printing mboxes ---")
    #for person in store.subjects(RDF.type, FOAF["Person"]):
     #   for mbox in store.objects(person, FOAF["mbox"]):
      #      print(mbox)

    # Serialize the store as RDF/XML to the file DB3.rdf.
    store.serialize("RDF/DO2RDF_13.rdf", format="pretty-xml", max_depth=3)
    #store.serialize("DB3.rdf", format="nt", max_depth=3)

    # Let's show off the serializers

    print('RDF Serializations:', seqa, 'De', tamanho)

    # Serialize as XML
    #print("--- start: rdf-xml ---")
    #print(store.serialize(format="pretty-xml"))
    #print("--- end: rdf-xml ---\n")
    #store.serialize(format="pretty-xml")

    # Serialize as Turtle
#    print("--- start: turtle ---")
#    print(store.serialize(format="turtle"))
#    print("--- end: turtle ---\n")

    # Serialize as NTriples
    #print("--- start: ntriples ---")
    #print(store.serialize(format="nt"))
    #print("--- end: ntriples ---\n")
  