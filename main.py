from bad_words_filter import filter_text

#teste rapido
t = "palavras ruins como bad, horrible e terrible nao podem aparecer"
w = ["bad", "horrible", "terrible"]

print("normal:")
print(filter_text(t, w))

print("\ncom [CENSURADO]:")
print(filter_text(t, w, "[CENSURADO]")) 