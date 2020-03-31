class JogoForca:

    listaTotal = [] # Lista com todas as palavras
    lista = [] # Lista restrita ao n• de caracteres
    contaLetras = {} # Dicionário com contagem de palavras por letra
    palavra = {} # Dicionário com posição das letras encontradas na palavra
    erradas = [] # Lista com tentativas
    erros = 0
    acertos = 0
    acerto = False # Condição para iniciar o método tentativas()

    def novoJogo(n):
        JogoForca.abreLista()
        JogoForca.buscaPalavras(n)
        JogoForca.primeiroAcerto(n)
        if JogoForca.acerto: JogoForca.tentativas(n)

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
        for letra in alfabeto: # Cria dicionário com número de palavras por letra
            soma = 0
            for palavra in lista:
                n = palavra.count(letra)
                if n > 0: soma += 1
            contaLetras[letra] = soma
        JogoForca.lista = lista  # Copia lista para lista pública da classe
        JogoForca.contaLetras = contaLetras # Copia dicionário //

    def tela(n): # Cria a interface (temporária)
        import os
        os.system("clear")
        print("PALAVRA: ", end='')
        if not JogoForca.palavra:
            for i in range(1,n+1):
                JogoForca.palavra[i] = "_ "
        for i in JogoForca.palavra:
            print(JogoForca.palavra[i],end='')
        print("\nErros:",JogoForca.erros, "/6")
        print("Letras Certas:",JogoForca.acertos,"/",n)

    def primeiroAcerto(carac): # Primeira tentativa até primeiro acerto
        acerto = False
        while acerto == False:
            JogoForca.tela(carac)
            n = 0
            for item in JogoForca.contaLetras:
                if JogoForca.contaLetras[item] > n:
                    n = JogoForca.contaLetras[item]
                    tentativa = item
            pergunta = input("A palavra possui a letra " + tentativa + "?: ")

            if pergunta == "s":
                while acerto == False:
                    JogoForca.tela(carac)
                    quantas = int(input("Quantas vezes a letra \"" + tentativa + "\" aparece na palavra? "))
                    print("Digite a posição da letra começando pelo início da palavra")
                    for i in range(quantas):
                        posicao = int(input("Posição da ocorrência: "))
                        JogoForca.palavra[posicao] = tentativa
                        JogoForca.acertos += 1
                    acerto = True
                JogoForca.erradas.append(tentativa)
                del JogoForca.contaLetras[tentativa]
                JogoForca.acerto = True

            elif pergunta == "n":
                JogoForca.erros += 1
                JogoForca.erradas.append(tentativa)
                del JogoForca.contaLetras[tentativa]
                if JogoForca.erros == 6: # Condição para perder e encerrar loop
                    acerto = True
                    JogoForca.perdi(carac)
                if len(JogoForca.lista) == 0:
                    acerto = True
                    JogoForca.perdi(carac)

            else: n = input("Resposta Inválida! Tecle <enter> para continuar.")


    def tentativas(carac): # Demais tentativas

        if len(JogoForca.lista) == 0:
            gameover = True
            JogoForca.perdi(carac)
        else: gameover = False

        while gameover == False:
            lista = [] # Lista com palavras encontradas
            letras = {} # Dicionário com posição de letras encontradas
            contaLetras = {} # Dicionário com contagem de palavras por letra
            import string
            alfabeto = list(string.ascii_lowercase)
            JogoForca.tela(carac)

            for item in JogoForca.palavra: # Cria dicio com posição e letras já encontradas
                if JogoForca.palavra[item] != "_ ":
                    letras[item] = JogoForca.palavra[item]

            for palavra in JogoForca.lista: # Procura palavras com posição e letras encontradas
                parametro = 0
                for letra in letras:
                    if palavra.find(letras[letra],letra-1,carac) == letra-1:
                        parametro += 1
                if parametro == len(letras):
                    lista.append(palavra)

            for letra in alfabeto: # Cria dicionário com número de palavras por letra
                elimina = False
                soma = 0
                for palavra in lista:
                    n = palavra.count(letra)
                    if n > 0: soma += 1
                for item in letras: # Descarta os acertos
                    if letras[item] == letra:
                        elimina = True
                for item in JogoForca.erradas: # Descarta as tentativas erradas
                    if letra == item:
                        elimina = True
                if elimina == False and soma > 0:
                    contaLetras[letra] = soma

                if len(lista) == 0:
                    break
                    perdi(carac)

            # Tentativa

            JogoForca.tela(carac)
            n = 0
            for item in contaLetras:
                if contaLetras[item] > n:
                    n = contaLetras[item]
                    tentativa = item
            pergunta = input("A palavra possui a letra " + tentativa + "?: ")

            if pergunta == "s":
                acerto = False
                while acerto == False:
                    JogoForca.tela(carac)
                    quantas = int(input("Quantas vezes a letra \"" + tentativa + "\" aparece na palavra? "))
                    print("Digite a posição da letra começando pelo início da palavra")
                    for i in range(quantas):
                        posicao = int(input("Posição da ocorrência: "))
                        JogoForca.palavra[posicao] = tentativa
                        JogoForca.acertos += 1
                    acerto = True
                JogoForca.erradas.append(tentativa)
                del JogoForca.contaLetras[tentativa]
                if JogoForca.acertos == carac: # Condição para vencer e encerrar loop
                    gameover = True
                    JogoForca.ganhei(carac)

            elif pergunta == "n":
                JogoForca.erros += 1
                JogoForca.erradas.append(tentativa)
                del JogoForca.contaLetras[tentativa]
                if JogoForca.erros == 6: # Condição para perder e encerrar loop
                    acerto = True
                    gameover = True
                    JogoForca.perdi(carac)

            else: n = input("Resposta Inválida! Tecle para continuar.")

    def ganhei(n):
        JogoForca.tela(n)
        print("GANHEI")

    def perdi(n):
        JogoForca.tela(n)
        print("PERDI")
        print

# Palavra = bala
import os
os.system("clear")
print("*** J O G O  D A  F O R C A ***\n")
n = int(input("Quantas letras tem a palavra que você pensou: "))
jogo = JogoForca
jogo.novoJogo(n)
