import re

def filtrar_texto(texto, palavras, *, substituir="***"):
    # checagem basica de erro
    if texto is None or palavras is None:
        raise TypeError("Input não pode ser None")
    
    if not isinstance(texto, str) or not isinstance(palavras, list):
        raise TypeError("Tipos de entrada errados")
    
    if not all(isinstance(p, str) for p in palavras):
        raise TypeError("Palavras ruins precisam ser texto")
    
    # retorno rapido se vazio
    if not texto or not palavras:
        return texto
    
    # faz o padrão e substitui
    padrao = '|'.join(r'\b' + re.escape(p) + r'\b' for p in palavras)
    return re.sub(padrao, lambda x: substituir, texto, flags=re.IGNORECASE) 