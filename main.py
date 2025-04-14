from filter import filtrar_texto


with open(text_file, "r") as file:
    texto = file.read()

#teste rapido

palavras_ruins = ["bobão", "fanfarrão", "bobinho", "panaca", "banana", "tanso", "lesado"]

print("normal:")
print(filtrar_texto(texto, palavras_ruins))

print("\ncom [CENSURADO]:")
print(filtrar_texto(texto, palavras_ruins, substituir="[CENSURADO]")) 