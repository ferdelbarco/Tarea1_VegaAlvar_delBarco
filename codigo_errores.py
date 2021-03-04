#Este codigo toma una lista y retorna otra en la que se eliminan los elementos "sandia"

lista = ["banano", "sandia", "naranja", "mango", "melon"]
listanueva = []

for i in lista:
    if i != "sandia":
        listanueva.append(i)

print(listanueva)