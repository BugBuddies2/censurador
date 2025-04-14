from filtro_palavras import filtrar_texto

#teste rapido
texto = "esse bobão e fanfarrão fica se achando o bobinho da turma"
palavras_ruins = ["bobão", "fanfarrão", "bobinho"]

print("normal:")
print(filtrar_texto(texto, palavras_ruins))

print("\ncom [CENSURADO]:")
print(filtrar_texto(texto, palavras_ruins, substituir="[CENSURADO]")) 