

import Automata as atm
garmatica={
"grafemas":{
  "valores":[1,2,3],
  "operador":["*","+"]}
}

grafo=[
["S",["grafemas,valores","S"],["grafemas,operador","Q1"]],
["Q1",["grafemas,valores","S"]]
]





a=atm.Leng(garmatica,grafo)
s=raw_input("Entre una oracion del lenguaje: ")
a.run(s)
