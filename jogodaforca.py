class JogoForca:

    listaTotal = [] # Lista com todas as palavras
    lista = []
    contaLetras = {}
    tentativa = ()

    def novoJogo(n):
        JogoForca.abreLista()
        JogoForca.tela(n)
        JogoForca.buscaPalavras(n)
        JogoForca.primeiroAcerto()
        JogoForca.tentativas(tentativa,posicao)

    def abreLista(): # Copia palavras do arquivo para lista
        listaPalavras = open('palavras.txt', 'r')
        for linha in listaPalavras: #
            palavra = linha.rstrip('\n')
            palavra = palavra.strip('.')
            JogoForca.listaTotal.append(palavra)
        listaPalavras.close()

    def buscaPalavras(n): # Busca palavras com n n• de caracteres
        lista = [] # Lista restrita ao n• de Caracteres
        contaLetras = {} # Dicionário com contagem de palavras por letra
        import string
        alfabeto = list(string.ascii_lowercase)
        for palavra in JogoForca.listaTotal: # Cria lista de palavras com  n caracteres
            if len(palavra) == n:
                lista.append(palavra)
        for letra in alfabeto: # Cria dicionário
            soma = 0
            for palavra in lista:
                n = palavra.count(letra)
                if n > 0: soma += 1
            contaLetras[letra] = soma
        JogoForca.lista = lista  # Copia lista para lista pública da classe
        JogoForca.contaLetras = contaLetras # Copia dicionário //

    def primeiroAcerto(): # Primeira tentativa até primeiro acerto
        acerto = False
        print("Hummmm... vamos lá...")
        while acerto == False:
            n = 0
            for item in JogoForca.contaLetras:
                if JogoForca.contaLetras[item] > n:
                    n = JogoForca.contaLetras[item]
                    tentativa = item
            pergunta = input("A palavra possui a letra " + tentativa + "?: ")
            if pergunta == "s":
                acerto = True
                posicao = input("Show! E qual a posição? ")
                return tentativa,posicao
            del JogoForca.contaLetras[tentativa]

    def tentativas(tentativa,posicao): # Demais tentativas
        pass


    def tela(n): # Cria a interface
        import os
        os.system("clear")
        print("PALAVRA: ", end='')
        for i in range(n):
            if i == n-1: print("__")
            else: print("__ ",end='')

# Palavra = bola
jogo = JogoForca
jogo.novoJogo(4)
