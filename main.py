from filter import filtrar_texto

# lê o arquivo de texto
with open("texto.txt", "r") as file:
    texto = file.read()

# lê a lista de palavras ruins
with open("lista.txt", "r") as file:
    palavras_ruins = [linha.strip() for linha in file]

print("normal:")
print(filtrar_texto(texto, palavras_ruins))

print("\ncom [CENSURADO]:")
print(filtrar_texto(texto, palavras_ruins, substituir="[CENSURADO]")) 