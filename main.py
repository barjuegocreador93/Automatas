

import Automata as atm
garmatica={
"grafemas":
  "valores":[1,2,3]
  "operador":["*","+"]
}

grafo=[
["S",["grafemas,valores","S"],["grafemas,operador","Q1"],
["Q1",["grafemas,valores","S"]]
]





a=atm.Leng(garamtica,grafo)
s=input("Entre una oracion del lenguaje: ")
a.run(s)


