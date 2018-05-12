from tkinter import *
import tkinter as tk
import PIL
from CAMPO_MINADO import CampoMinado
from PIL import ImageTk, Image

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class CampoMinadoGUI(tk.Frame):


    str_botaoPadrao = "botaoPadrao"
    str_botao0 = "botao0"
    str_botao1 = "botao1"
    str_botao2 = "botao2"
    str_botao3 = "botao3"
    str_botao4 = "botao4"
    str_botao5 = "botao5"
    str_botao6 = "botao6"
    str_botao7 = "botao7"
    str_botaoBandeira = "botaoBandeira"
    str_botaoBandeiraErrada = "botaoBandeiraErrada"
    str_botaoMina = "botaoMina"
    str_botaoMinaPisada = "botaoMinaPisada"


    def __init__(self, campoMinado, master=None):

        super ( ).__init__ (master)
        master.minsize (width=600, height=600)

        self.pack ( )

        self.winfo_toplevel ( ).title ("Campo Minado - by Ricardo Varjão")

        #cria as imagens para serem utilizadas nos botoes
        imagensNomes = [self.str_botao0, self.str_botao1, self.str_botao2, self.str_botao3, self.str_botao4,
                        self.str_botao5, self.str_botao6, self.str_botao7, self.str_botaoPadrao,
                        self.str_botaoBandeira, self.str_botaoBandeiraErrada, self.str_botaoMina, self.str_botaoMinaPisada]

        self.imagens = {}
        dir = "imagens/"
        for nome in imagensNomes:
            self.imagens[nome] = self.img = ImageTk.PhotoImage (Image.open (dir + nome + ".jpg"))

        print("imagens: {}".format(self.imagens))

        self.identificandoMina = False #deve-se colocar True para quando a jogada for para identificar uma mina

        self.campoMinado = campoMinado

        self.cria_tela()


    def cria_tela(self):
        print("criando tela")

        #frames
        #---
        #---LABEL MINAS RESTANTES--BOTAO NOVO JOGO--LABEL TIMER # [ENCAPSULADOS em frame_superior]
        #---MENSAGENS------------                               # [ENCAPSULADO em frame_superior]
        #---FRAME DO CAMPO MINADO
            #---CAMPO MINADO ---- [BOTOES ENCAPSULADOS em frame_campo_minado

        self.frame_superior = tk.Frame()
        self.frame_superior.pack ()


        #-----
        self.botaoNovoJogo = tk.Button (self.frame_superior)
        self.botaoNovoJogo[ "text" ] = "Novo Jogo"

        self.labelMinasRestantes = tk.Label(self.frame_superior)
        self.labelMinasRestantes["text"] = "0"

        self.labelTimer = tk.Label (self.frame_superior)
        self.labelTimer[ "text" ] = "0"


        self.check_var_identificando_mina = tk.IntVar()
        self.check_identificando_mina = tk.Checkbutton(self.frame_superior, variable = self.check_var_identificando_mina)
        self.label_identificando_mina = tk.Label(self.frame_superior)
        self.label_identificando_mina["text"] = "Identificar mina: "


        self.botaoIdentificaMina = tk.Button(self.frame_superior)
        self.botaoIdentificaMina["text"] = "Identificar mina"
        self.botaoIdentificaMina["command"] = self.identificarMina

        self.labelMensagens = tk.Label(self.frame_superior)
        self.labelMensagens["text"] = ""

        #configurando os widgets no grid (self.frame_superior)


        row = 0
        self.labelMinasRestantes.grid(row=row, sticky=W)
        self.botaoNovoJogo.grid(row=row, column = 1, sticky = W)
        self.labelTimer.grid(row=row, column = 2, sticky = W)

        row += 1
        # >> > var = Tkinter.IntVar ( )

        self.label_identificando_mina.grid(row = row, column = 0, columnspan = 2, sticky = W + E)
        self.check_identificando_mina.grid(row = row, column = 2, sticky = W)


        # row += 1
        # self.botaoIdentificaMina.grid(row = row, column = 0, columnspan = 3, sticky = W + E)

        row += 1
        self.labelMensagens.grid(row = row, column = 0, columnspan = 3, sticky = W + E)

        self.cria_campo_minado()

        self.cria_menu()
        # self.botaoNovoJogo[ "command" ] = lambda : self.acao_menu_novo_jogo(colunas, minas)
        self.botaoNovoJogo["command"] = self.acao_botao_novo_jogo

    def cria_campo_minado(self):

        self.frame_campo_minado = tk.Frame ( )
        self.frame_campo_minado.config (bg="blue")
        self.frame_campo_minado.pack ( )
        self.botoes = []

        #cria matriz com os botoes na tela
        for i in range (0, self.campoMinado.linhas):
            self.botoes.append ([ ])
            for j in range (0, self.campoMinado.colunas):
                self.botoes[i].append(tk.Button (self.frame_campo_minado, image=self.imagens["botaoPadrao"]))
                self.botoes[i][j]["command"] = lambda x=i, y=j : self.botao_celula(x,y)
                self.botoes[i][j].grid (row=i, column=j)

    def cria_menu(self):
        #cria o menu principal
        self.menubar = Menu (self)

        #cria o primeiro menu e coloca no self.menubar
        self.menu_novo_jogo = Menu(self.menubar)

        #coloca as opcoes de comando
        self.menu_novo_jogo.choices = Menu(self.menu_novo_jogo)

        #nao entendi para quer serve wierdones
        self.menu_novo_jogo.choices.wierdones = Menu(self.menu_novo_jogo.choices)

        self.menu_5x5 = Menu(self.menu_novo_jogo)
        self.menu_5x5.add_command(label="5 minas", command=lambda : self.acao_menu_novo_jogo(5,5))
        self.menu_5x5.add_command(label="10 minas", command=lambda : self.acao_menu_novo_jogo(5,10))
        self.menu_5x5.add_command(label="15 minas", command=lambda : self.acao_menu_novo_jogo(5,15))

        self.menu_8x8 = Menu(self.menu_novo_jogo)
        self.menu_8x8.add_command(label="10 minas", command=lambda : self.acao_menu_novo_jogo(8,10))
        self.menu_8x8.add_command(label="20 minas", command=lambda : self.acao_menu_novo_jogo(8,20))
        self.menu_8x8.add_command(label="40 minas", command=lambda : self.acao_menu_novo_jogo(8,40))

        self.menu_10x10 = Menu (self.menu_novo_jogo)
        self.menu_10x10.add_command (label="5 minas", command=lambda : self.acao_menu_novo_jogo(10,5))
        self.menu_10x10.add_command (label="20 minas", command=lambda : self.acao_menu_novo_jogo(10,20))
        self.menu_10x10.add_command (label="50 minas", command=lambda : self.acao_menu_novo_jogo(10,50))

        self.menu_novo_jogo.add_cascade(label="5x5", menu=self.menu_5x5)
        self.menu_novo_jogo.add_cascade(label="8x8", menu=self.menu_8x8)
        self.menu_novo_jogo.add_cascade(label="10x10", menu=self.menu_10x10)


        self.unused = Menu(self.menubar)
        self.menubar.add_cascade(label = "Novo jogo", menu = self.menu_novo_jogo)
        # self.menu_novo_jogo.add_cascade(label="Novo jogo", menu=self.menu_novo_jogo)
        self.top = Toplevel(menu = self.menubar)


        self.unused = Menu (self.menubar)

        self.top = Toplevel (menu=self.menubar, width=500, relief=RAISED,
                             borderwidth=2)

    def acao_botao_novo_jogo(self):
        print("acao menu  colunas: {}  minas: {}".format(colunas, minas))
        self.novo_jogo(self.campoMinado.colunas, self.campoMinado.minas)


    def acao_menu_novo_jogo(self, nColunas, nMinas):
        minas = nMinas
        colunas = nColunas
        print("acao menu  colunas: {}  minas: {}".format(colunas, minas))

        self.novo_jogo(colunas, minas)

    def donothing(self):
        print("menu")



    def novo_jogo(self, nColunas, nMinas):
        self.check_var_identificando_mina.set(False)
        # self.identificandoMina = False

        self.labelMensagens["text"] = ""
        for (i, linhaBotoes) in enumerate(self.botoes):
            for (j, botao) in enumerate(linhaBotoes):
                # self.botoes[i].__delitem__(j)

                self.botoes[i][j].destroy()


        self.frame_campo_minado.destroy()

        self.campoMinado = ""
        self.campoMinado = CampoMinado(nColunas, nMinas)
        self.cria_campo_minado()
        print("Novo jogo")

    def botao_celula(self, x, y):

        # if self.identificandoMina == False:
        print("self.check_var_identificando_mina: {}",self.check_var_identificando_mina.get())
        if self.check_var_identificando_mina.get() == False:
            print("botao celula {}: ({},{})".format(self,x,y))
            self.campoMinado.fazJogadaNaPosicao(x,y)
        else:
            self.campoMinado.sinalizaMinaNaPosicao(x,y)
            self.identificandoMina = False
        self.atualiza_tela()
        self.verificaStatusDoJogo()

    def identificarMina(self):
        self.identificandoMina = not(self.identificandoMina)
        if self.identificandoMina == True:
            # self.botaoIdentificaMina.configure(bg = "blue")
            self.botaoIdentificaMina.background = "blue"
        else:
            self.botaoIdentificaMina.background = "white"
            # self.botaoIdentificaMina.configure(bg = "white")
        print("self.identificandoMina: ", self.identificandoMina)

    def verificaStatusDoJogo(self):
        print("verificaStatusDoJogo")
        print("status do jogo: {}".format(self.campoMinado.statusDoJogo))

        if self.campoMinado.statusDoJogo == self.campoMinado.statusJogoJogadorVenceu:
            print ("VOCÊ VENCEU")
            self.labelMensagens["text"] = "Você venceu! :)"
            self.bloqueiaBotoes ( )

        elif self.campoMinado.statusDoJogo == self.campoMinado.statusJogoJogadorPerdeu:
            self.labelMensagens["text"] = "Você perdeu! :("
            print ("VOCÊ PERDEU")  # abre o campo inteiro
            self.bloqueiaBotoes ( )

    def desbloqueiaBotoes(self):
        for i in range(0, self.linhas):
            for j in range(0, self.colunas):
                self.botoes[i][j].config(state = "enabled")

    def bloqueiaBotoes(self):
        for i in range(0, self.campoMinado.linhas):
            for j in range(0, self.campoMinado.colunas):
                self.botoes[i][j].config(state = "disabled")


    def atualiza_tela(self):
        for x in range(0, self.campoMinado.linhas):
            for y in range(0, self.campoMinado.colunas):
                valor = self.campoMinado.campoVisivel[x][y]
                imgNome = self.imagemDadoValorCelulaVisivel(valor)
                img = self.imagens[imgNome]
                self.botoes[x][y].configure(image = img)
                self.botoes[x][y].image = img

                if RepresentsInt(imgNome[-1]):
                    self.botoes[x][y].config(state = "disabled")

        self.labelMinasRestantes["text"] = "{}".format(self.campoMinado.minasRestantes)




    #deve-se passar o status da celula no campoMinado.campoVisivel e funcao vai retornar a imagem que
    #ser utilizada
    def imagemDadoValorCelulaVisivel(self, valorVisivel):

        nome = ""
        if isinstance(valorVisivel, int):
            nome = "botao" + "{}".format(valorVisivel)
        elif valorVisivel == self.campoMinado.str_celulaAberta:
            nome = self.str_botao0
        elif valorVisivel == self.campoMinado.str_minaSinalizada:
            nome = self.str_botaoBandeira
        elif valorVisivel == self.campoMinado.str_minaSinalizadaErrada:
            nome = self.str_botaoBandeiraErrada
        elif valorVisivel == self.campoMinado.str_celulaPadrao:
            nome = self.str_botaoPadrao
        elif valorVisivel == self.campoMinado.str_mina:
            nome = self.str_botaoMina

        # print("valor:{}  nome:{}".format(valorVisivel, nome))
        return nome

colunas = 10
minas = 5
campoMinado = CampoMinado(colunas, minas)

root = tk.Tk ()


# app = CampoMinadoGUI (master=root)
app = CampoMinadoGUI (campoMinado, master=root)

root.resizable(width=False, height=False)
root.size ( )
app.mainloop ( )