from filter import filtrar_texto

# lê o arquivo de texto
with open("texto.txt", "r") as file:
    texto = file.read()

# lê a lista de palavras ruins
with open("lista.txt", "r") as file:
    palavras_ruins = [linha.strip() for linha in file]

# filtra o texto
texto_filtrado = filtrar_texto(texto, palavras_ruins)
texto_filtrado_censurado = filtrar_texto(texto, palavras_ruins, substituir="[CENSURADO]")

# mostra na tela
print("normal:")
print(texto_filtrado)

print("\ncom [CENSURADO]:")
print(texto_filtrado_censurado)

# salva em arquivo
with open("censurado.txt", "w") as file:
    file.write(texto_filtrado)

print("\nArquivo 'censurado.txt' foi criado com o texto filtrado!") 