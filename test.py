import unittest
from filter import filtrar_texto

class TestesFiltro(unittest.TestCase):
    
    def test_basico(self):
        texto = "esse bobão e fanfarrão fica se achando o bobinho da turma"
        palavras = ["bobão", "fanfarrão", "bobinho"]
        resultado = filtrar_texto(texto, palavras)
        esperado = "esse *** e *** fica se achando o *** da turma"
        self.assertEqual(resultado, esperado)
    
    def test_maiuscula(self):
        texto = "BOBÃO bobão Bobão bObÃo"
        palavras = ["bobão"]
        resultado = filtrar_texto(texto, palavras)
        esperado = "*** *** *** ***"
        self.assertEqual(resultado, esperado)
    
    def test_varias_palavras(self):
        texto = "esse panaca e banana fica se achando o tanso da turma"
        palavras = ["panaca", "banana", "tanso"]
        resultado = filtrar_texto(texto, palavras)
        esperado = "esse *** e *** fica se achando o *** da turma"
        self.assertEqual(resultado, esperado)
    
    def test_parte_palavra(self):
        texto = "a palavra 'banana' tem 'nana' dentro mas nao deve ser filtrada"
        palavras = ["nana"]
        resultado = filtrar_texto(texto, palavras)
        esperado = "a palavra 'banana' tem '***' dentro mas nao deve ser filtrada"
        self.assertEqual(resultado, esperado)
    
    def test_pontuacao(self):
        texto = "bobão! bobão, bobão. bobão? bobão; bobão:"
        palavras = ["bobão"]
        resultado = filtrar_texto(texto, palavras)
        esperado = "***! ***, ***. ***? ***; ***:"
        self.assertEqual(resultado, esperado)
    
    def test_texto_vazio(self):
        texto = ""
        palavras = ["bobão"]
        resultado = filtrar_texto(texto, palavras)
        esperado = ""
        self.assertEqual(resultado, esperado)
    
    def test_lista_vazia(self):
        texto = "esse texto nao deve mudar"
        palavras = []
        resultado = filtrar_texto(texto, palavras)
        esperado = "esse texto nao deve mudar"
        self.assertEqual(resultado, esperado)
    
    def test_none(self):
        with self.assertRaises(TypeError):
            filtrar_texto(None, ["bobão"])
        
        with self.assertRaises(TypeError):
            filtrar_texto("texto", None)
    
    def test_tipo_errado(self):
        with self.assertRaises(TypeError):
            filtrar_texto(123, ["bobão"])
        
        with self.assertRaises(TypeError):
            filtrar_texto("texto", "bobão")
        
        with self.assertRaises(TypeError):
            filtrar_texto("texto", ["bobão", 123])
    
    def test_substituicao(self):
        texto = "esse bobão fica zuando"
        palavras = ["bobão"]
        resultado = filtrar_texto(texto, palavras, substituir="[CENSURADO]")
        esperado = "esse [CENSURADO] fica zuando"
        self.assertEqual(resultado, esperado)
    
    def test_espacos(self):
        texto = "   varios   espacos   entre   bobão   palavras   "
        palavras = ["bobão"]
        resultado = filtrar_texto(texto, palavras)
        esperado = "   varios   espacos   entre   ***   palavras   "
        self.assertEqual(resultado, esperado)
    
    def test_quebras(self):
        texto = "linha com bobão\noutra linha\tcom bobão\tpalavras"
        palavras = ["bobão"]
        resultado = filtrar_texto(texto, palavras)
        esperado = "linha com ***\noutra linha\tcom ***\tpalavras"
        self.assertEqual(resultado, esperado)

if __name__ == "__main__":
    unittest.main()