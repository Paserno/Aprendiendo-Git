miDiccionario={"Chile":"Santiago","Peru":"Lima","Argentina":"Buenos Aires"}
miDiccionario["España"]="Roma"
print(miDiccionario)
miDiccionario["España"]="Madrid"
print(miDiccionario)

del miDiccionario["Peru"] #Eliminar un valor en el diccionario 
print(miDiccionario)