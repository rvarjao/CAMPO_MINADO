
# coding=utf-8

import random

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __contains__(self, item):
        return (self.x == item.x) and (self.y == item.y)


def stringSeparetedBy(self, text, separator):
    words = [ ]
    cWord = ""
    for char in text:
        if char == separator:
            words.append (cWord)
            cWord = ""
        else:
            cWord += char
    if cWord != "": words.append (cWord)
    return words



class CampoMinado():

    str_celulaPadrao = chr (9606) #  ▆
    str_celulaAberta = chr (9617) #  ░
    str_minaSinalizada = "$"
    str_mina = "*"
    str_minaSinalizadaErrada = "%"


    statusJogoProntoParaInicio = "statusJogoProntoParaInicio"
    statusJogoJogadorVenceu = "statusJogoJogadorVenceu"
    statusJogoJogadorPerdeu = "statusJogoJogadorPerdeu"
    statusJogoEmAndamento = "statusJogoEmAndamento"
    # statusJogoFinalizado = "statusJogoFinalizado"
    statusJogoPausado = "statusJogoPausado"


    def __init__(self, nColunas, nMinas):

        self.colunas = nColunas
        self.minas = nMinas

        self.linhas = nColunas

        self.campo = []
        self.campoVisivel = []

        self.posicoesDasMinas = []
        self.posicoesDasMinasSinalizadas = []  #[["1,1"],["2,3"]]     [2,3] : significa x = 2, y = 3
        self.statusDoJogo = self.statusJogoProntoParaInicio

        # cria o campo
        self.criaCampo()
        self.criaCampoVisivel() #o que sera visivel

        self.imprimeCampoEscondido()
        self.imprimeCampoVisivel()
        self.minasRestantes = nMinas




    import random

    #campo minado
    #fazer um jogo de campo minado
    #exemplo abaixo:

    #     A B C D E F
    # 0   0 0 0 0 0 0
    # 1   0 1 1 1 0 0
    # 2   0 1 X 1 0 0
    # 3   0 1 2 1 1 0
    # 4   0 0 1 X 1 0
    # 5   0 0 1 1 1 0

    # x é a mina
    # os numeros representam quantas minas tem em volta daquela posicao

    def imprimeCampoEscondido(self):
        self.imprimeCampo(self.campo)

    def imprimeCampoVisivel(self):
        self.imprimeCampo(self.campoVisivel)

    def imprimeCampo(self, campo):
        colunas = len(campo)
        linhas = colunas

        print("\n      ", end = " ")
        for x in range(0, colunas):
            print(x, end= " ")
        print("\n")

        for x in range(0, linhas):
            print ("{}     ".format(x), end=" ")
            for y in range(0, colunas):
                valor = campo[x][y]
                print(valor, end=" ")
            print()

    def criaCampo(self):

        for x in range (0, self.colunas):
            self.campo.append ([ ])
            for y in range (0, self.colunas):
                self.campo[ x ].append (0)

        self.colocaMinas()
        self.ajustaNumeros()

    def colocaMinas(self):
        self.minasRestantes = self.minas

        if self.statusDoJogo == self.statusJogoProntoParaInicio:
            # coloca as minas de forma aleatoria
            minasColocadas = 0
            posicaoMinas = []

            while minasColocadas < self.minas:
                linha = random.randrange (0, self.linhas)
                coluna = random.randrange (0, self.colunas)

                # print("colocar mina na posicao: ({},{}) ou [{}]".format(linha, coluna))

                if self.campo[ linha ][ coluna ] == 0:
                    self.campo[ linha ][ coluna ] = self.str_mina
                    minasColocadas += 1
                    self.posicoesDasMinas.append(Point(linha, coluna))
            print(self.posicoesDasMinas)


    def ajustaNumeros(self):
        #coloca os numeros corretamente apos ter colocado as minas
        colunas = self.colunas

        # print("colunas: {}".format(colunas))
        for x in range(0, self.colunas):
            for y in range(0, self.colunas):

                valor = self.campo[x][y]
                if valor == self.str_mina:  # tem que ajustar os numeros das posicoes em volta
                    # x - 1   -> y, y - 1, y + 1
                    # x + 0  ->  y, y - 1, y + 1
                    # x + 1  ->  y, y - 1, y + 1
                    # print("achei a mina na posicao: ({},{})".format(x,y))
                    for i in range(-1, 2):

                        if (x + i) < 0 or (x+ i) >= colunas:
                            # print("nao vai procurar na linha: {}".format(x+i))
                            continue
                        for j in range(-1, 2):

                            if (y + j) < 0 or (y + j >= colunas):
                                continue
                            # print("x: {}  y:{}".format(x,y))
                            # print("valor antes: {}".format(tempCampo[x+i][y+j]))
                            if self.campo[x+i][y+j] != self.str_mina: self.campo[x+i][y+j] += 1
                            # print("valor depois: {}".format(tempCampo[x+i][y+j]))


        self.imprimeCampo(self.campo)




    # str_celulaPadrao = chr(11035)
    # str_celulaAberta = chr(11036)

    def criaCampoVisivel(self): #cria o campo visivel
        self.campoVisivel = []
        for x in range(0, self.colunas):
            self.campoVisivel.append([])
            for y in range(0, self.colunas):
                self.campoVisivel[x].append(self.str_celulaPadrao)

    def sinalizaMinaNaPosicao(self, x,y):

        if self.campoVisivel[x][y] == self.str_minaSinalizada: #ja esta marcada, deve-se desmarcar
            self.campoVisivel[ x ][ y ] = self.str_celulaPadrao
            self.posicoesDasMinasSinalizadas.remove(Point(x,y))
            self.minasRestantes += 1
        else:
            self.campoVisivel[x][y] = self.str_minaSinalizada
            self.posicoesDasMinasSinalizadas.append(Point(x,y))
            self.minasRestantes -= 1

        self.atualizaStatusDoJogo()

        if self.statusDoJogo == self.statusJogoJogadorPerdeu:
            print("Fim de jogo, você perdeu")
            self.revelaMinas()
        elif self.statusDoJogo == self.statusJogoJogadorVenceu:
            print("Você venceu")

        self.imprimeCampoVisivel()


    def fazJogadaNaPosicao(self, x, y):
        # tempCampoVisivel = self.campoVisivel

        valor = self.campo[x][y]
        if self.posicoesDasMinasSinalizadas.__contains__(Point(x,y)): return

        if valor == self.str_mina:
            print("Você pisou numa bomba!")
            self.statusDoJogo = self.statusJogoJogadorPerdeu
            self.revelaMinas()

        elif valor == 0:
            self.limparRegiaoAPartirDaPosicao(x, y)
        else: #revela o valor
            self.campoVisivel[x][y] = valor

        self.imprimeCampoVisivel()

    def atualizaStatusDoJogo(self):
        # todas as minas sinalizadas devem coincidir com as posicoes das minas
        minasCoincidentes = 0

        print("posicoesDasMinas: ",self.posicoesDasMinas)
        print ("posicoesDasMinasSinalizadas: ", self.posicoesDasMinasSinalizadas)

        if len(self.posicoesDasMinasSinalizadas) == len(self.posicoesDasMinas):#ja chutou todas, deve-se verificar se ganhou

            for (i, p) in enumerate(self.posicoesDasMinasSinalizadas):

                print("[{}] - {}".format(i, p))

                # if posicaoSinalizada in self.posicoesDasMinas: print("in funcionando")

                if self.posicoesDasMinas.__contains__(p):
                    print ("acertou mais uma")
                    minasCoincidentes += 1
                    if minasCoincidentes == self.minas:
                        self.statusDoJogo = self.statusJogoJogadorVenceu
                        return
                else:
                    print("nao encontrou a mina na posicao: ".format(p))
                    self.statusDoJogo = self.statusJogoJogadorPerdeu #errou ao menos uma
                    return


        else:
            self.statusDoJogo = self.statusJogoEmAndamento

    def revelaMinas(self):   #tem que sinalizar aquelas posicoes que foram marcadas erradas
        for mina in self.posicoesDasMinas:
            x = mina.x
            y = mina.y
            self.campoVisivel[x][y] = self.str_mina

        for minaSinalizada in self.posicoesDasMinasSinalizadas:
            x = minaSinalizada.x
            y = minaSinalizada.y
            if self.posicoesDasMinas.__contains__(minaSinalizada):
                self.campoVisivel[x][y] = self.str_minaSinalizada
            else:
                self.campoVisivel[x][y] = self.str_minaSinalizadaErrada


    def abreTodoOCampo(self):
        for x in range(0,self.linhas):
            for y in range(0, self.colunas):
                print("(x,y): ({},{})".format(x,y))
                valorCampo = self.campo[x][y]
                valorVisivel = self.campoVisivel[x][y]

                if isinstance (valorCampo, int):
                    self.campoVisivel[x][y] = valorCampo
                else:
                    self.campoVisivel[x][y] = self.str_mina

        self.imprimeCampoVisivel()


    def limparRegiaoAPartirDaPosicao(self, x, y):
        #quando o jogados clica em uma região onde não tem bomba proximas e o valor da celula é 0
        #toda a area limitada tem que ser limpa, como preencher um area com determinada cor
        #aqui vai ser usado a tecnica:
        #  8-Connected Polygon, disponivel no link:
        #https://www.tutorialspoint.com/computer_graphics/polygon_filling_algorithm.htm
        #acesso em 06/05/2018

        if self.campo[x][y] > 0: self.campoVisivel[x][y] = self.campo[x][y]
        else: self.campoVisivel[x][y] = self.str_celulaAberta

        colunas = len(self.campoVisivel)
        i = x
        j = y

        #faz por recursividade
        # FloodFill (seedx – 1, seedy, fcol, dcol)
        # FloodFill (seedx + 1, seedy, fcol, dcol)
        # FloodFill (seedx, seedy - 1, fcol, dcol)
        # FloodFill (seedx, seedy + 1, fcol, dcol)
        # FloodFill (seedx – 1, seedy + 1, fcol, dcol)
        # FloodFill (seedx + 1, seedy + 1, fcol, dcol)
        # FloodFill (seedx + 1, seedy - 1, fcol, dcol)
        # FloodFill (seedx – 1, seedy - 1, fcol, dcol)

        for i in range(-1, 2):
            if (x + i) < 0 or (x + i) >= colunas: continue
            for j in range (-1, 2):
                if i == 0 and j == 0 : continue
                if (y + j) < 0 or (y + j >= colunas): continue

                indexX = x+i
                indexY = y+j

                valorCampo = self.campo[indexX][indexY]
                valorVisivel = self.campoVisivel[indexX][indexY]

                if valorCampo == 0 and self.campoVisivel[indexX][indexY] == self.str_celulaPadrao:
                    self.campoVisivel[indexX][indexY] = self.str_celulaAberta
                    self.limparRegiaoAPartirDaPosicao(indexX, indexY)
                elif isinstance(valorCampo, int) and self.campoVisivel[x+i][y+j] == self.str_celulaPadrao:
                    self.campoVisivel[indexX][indexY] = valorCampo


