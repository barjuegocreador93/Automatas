# -*- coding: utf-8 -*-
'''
    @autor: Camilo Barbosa
            t00036196
'''

#variables globales
_mostrar_recorridos_del_grafo=0
_mostrar_gramtica_por_gramatica=1
#fin de variables globales

import string,copy

class Nodo:
    def __init__(self,nombre):
        self.nombre=nombre
        self.comparativas=[]
        self.realcom=[]
        self.dirreciones=[]
    def addDirection(self,compartivo="",destino=""):
        self.comparativas.append(compartivo)
        self.dirreciones.append(destino)



    def run(self,str_,index):
        i=0
        a=""
        if(len(str_)>index):

            for data in self.realcom:
                if(a!=""):
                    break
                for gram in data:
                    if len(str_)-index >= len(str(gram)):
                        l=index+len(str(gram))
                        if str_[index:l] == str(gram):
                            a=self.dirreciones[i]
                            if _mostrar_recorridos_del_grafo:
                                print (a)
                            if _mostrar_gramtica_por_gramatica:
                                print (self.comparativas[i])


                            index=l
                            break

                i+=1
        else: return [a,index,self.nombre]

        return [a,index]

    def callPackets(self):
        return self.comparativas


class Grafo:
    def __init__(self,grafo,gramatica):
        self.postion=0
        self.gram=gramatica
        self.hijos=[]
        self.str_=" "
        self.index=0
        self.final=""

        #algebra de bool
        self.vars=[]
        self.tabladeVerdad=[]

        if(isinstance(grafo,list)):
            for nodo in grafo:
                a=Nodo(nodo[0])
                i=1
                while i<len(nodo):
                    a.addDirection(nodo[i][0],nodo[i][1])
                    i+=1
                self.hijos.append(a)
            for sons in self.hijos:
                data=sons.callPackets()
                resul=[]
                for grm in data:
                    keys=grm.split(',')
                    if(len(keys)==2):
                        resul.append(self.gram[keys[0]][keys[1]])
                    if(len(keys)==3):
                        for here in self.gram[keys[0]][keys[1]]:
                            if(keys[2]==here):
                               resul.append([here])
                sons.realcom=resul

    #algebra de bool
    def tabladeverdad(self):
        bit=[1,0]


    def run(self,str_):
        self.str_=str_
        posa=pos=self.postion
        self.index=0
        var=""
        while pos>-1:
            pos=self.fanNodo(self.hijos[pos].run(str_,self.index))


        return self.final


    def fanNodo(self,data):
        i=0
        self.index=data[1]
        if(len(data)==3):
           self.final=data[2]
        for sons in self.hijos:
            if(sons.nombre==data[0]):
                return i
            i+=1
        return -1











class Leng:
    def __init__(self,gramatica=0,grafo=0):
        self.gramatica={}
        self.grafo=[]
        if(isinstance(gramatica,int)):
            self.gramatica={
                "operadores":{
                    "conjucion":["*"," y "],
                    "disyuncion":["+"," o "],
                    "negacion":["!","no "],
                    "condicional":[">"," implica que "," implica "," si "],
                    "exclusivo":["?"," exclueyendo "],
                    "bicondicional":["-"," para ambos "]
                },
                "variables":{
                    "caracteres":['a','b','c','d','e','f','g','h','i',
                                'j','k','l','m','n','ñ','o','p','q','r','s',
                                't','u','v','w','x','y','z',' '
                                ]

                },
                "valores":{
                    "bool":[1,0,"verdadero","falso"]
                },
                "parentecis":{
                    "min":['('],
                    "max":[')'],
                    "deep":0
                }

            }
        if(isinstance(gramatica,type({}))):
            self.gramatica=gramatica
        if(isinstance(grafo,int)):
            self.grafo=[
            ["Q0",["operadores,negacion","Q1"],["valores,bool","S1"],["variables,caracteres","S2"]],
            ["Q1",["valores,bool","S1"],["variables,caracteres","S2"]],
            ["Q2",["operadores,negacion","Q1"],["operadores,conjucion","Q0"],["operadores,disyuncion","Q0"],["operadores,condicional","Q0"]
            ,["operadores,bicondicional","Q0"]],
            ["S1",["operadores,exclusivo","Q2"],["operadores,conjucion","Q0"],["operadores,disyuncion","Q0"],["operadores,condicional","Q0"]
            ,["operadores,bicondicional","Q0"]],
            ["S2",["operadores,exclusivo","Q2"],["operadores,conjucion","Q0"],["operadores,disyuncion","Q0"],["operadores,condicional","Q0"]
            ,["operadores,bicondicional","Q0"],["variables,caracteres","S2"]]
            ]
        elif(isinstance(grafo,list)):
            self.grafo=grafo

        self.interprete=Grafo(self.grafo,self.gramatica)

    def run(self,str_):

        sts=self.interprete.run(str_)
        if(len(sts)!=0):
            if(sts[0]=="S"):
                print ""
                print ("Es una expreción de este lenguaje")
            else: print ("No es una expreción de este lenguaje")
        else: print ("No una expreción de este lenguaje")








