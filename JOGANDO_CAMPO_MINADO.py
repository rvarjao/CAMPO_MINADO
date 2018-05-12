from CAMPO_MINADO import CampoMinado

#inicio do jogo
#pergunta como quer o jogo, pode colocar opcoes menores
colunas = int(input("Numero de colunas: "))
minas = int(input("Numero de minas: "))

campoMinado = CampoMinado(colunas, minas)

# campoMinado.imprimeCampoEscondido()

# print ("Campo visivel")
# campoMinado.imprimeCampoVisivel()

#comeca a jogar
print(campoMinado.statusDoJogo)
while(
        (campoMinado.statusDoJogo == campoMinado.statusJogoEmAndamento) or
        (campoMinado.statusDoJogo == campoMinado.statusJogoPausado) or
        (campoMinado.statusDoJogo == campoMinado.statusJogoProntoParaInicio)
    ):

        print("status do jogo: ".format(campoMinado.statusDoJogo))
        print("Para identificar a bomba, digite i na frente da jogada\nEx: i1,2")
        entrada = input("Digite a jogada (x,y):")

        pos = entrada.find (",")

        if entrada[0] == "i":

            x = int(entrada[1:pos])
            y = int(entrada[-pos+1:])
            campoMinado.sinalizaMinaNaPosicao(x,y)

        else:
            x = int(entrada[:pos])
            y = int(entrada[-pos:])
            campoMinado.fazJogadaNaPosicao(x,y)

if campoMinado.statusDoJogo == campoMinado.statusJogoJogadorVenceu:
    print("Parabéns! Você venceu")
elif campoMinado.statusDoJogo == campoMinado.statusJogoJogadorPerdeu:
    print("Que pena! Você perdeu")
