# -*- coding: utf-8 -*-
#Este codigo toma una lista y retorna otra en la que se eliminan los elementos "sandia" 

import numpy  # Error 1: module imported but unused

lista = ["banano", "sandia", "naranja", "mango", "melon"]

for i in lista:
    if i is not "sandia":  
        # Error 2: use ==/!= to compare str, bytes, and int literals
        listanueva.append(i)  # Error 3: undefined name

print(listanueva)
