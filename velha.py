class Velha:

    coord = [{"A": " ", "B": " ", "C": " "}, {
        "A": " ", "B": " ", "C": " "}, {"A": " ", "B": " ", "C": " "}]
    validos = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    jogadas = 0
    jogador1 = ""
    jogador2 = ""
    Andamento = False

    def __init__(self):
        self.coord = [{"A": " ", "B": " ", "C": " "}, {
            "A": " ", "B": " ", "C": " "}, {"A": " ", "B": " ", "C": " "}]
        self.validos = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.jogadas = 0
        self.jogador1 = ""
        self.jogador2 = ""
        self.Andamento = False

    def NovoJogo(self):
        self.coord = [{"A": " ", "B": " ", "C": " "}, {
            "A": " ", "B": " ", "C": " "}, {"A": " ", "B": " ", "C": " "}]
        self.validos = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.jogadas = 0
        self.jogador1 = ""
        self.jogador2 = ""
        self.Andamento = True

        return self.EnviarTabuleiro() + "\n\nNOVO JOGO!"

    def Verifica(self):
        win = "" if self.jogadas != 9 else "velha"
        for i in range(3):
            if(self.coord[i]["A"] == self.coord[i]["B"] == self.coord[i]["C"] != ' '):
                win = self.jogador1 if self.coord[i]["A"] == 'X' else self.jogador2

        for j in self.coord[0].keys():
            if(self.coord[0][j] == self.coord[1][j] == self.coord[2][j] and self.coord[2][j] != ' '):
                win = self.jogador1 if self.coord[0][j] == 'X' else self.jogador2

        if(self.coord[0]["A"] == self.coord[1]["B"] == self.coord[2]["C"] != ' '):
            win = self.jogador1 if self.coord[0]["A"] == 'X' else self.jogador2

        if(self.coord[2]["A"] == self.coord[1]["B"] == self.coord[0]["C"] != ' '):
            win = self.jogador1 if self.coord[2]["A"] == 'X' else self.jogador2

        return win

    def EnviarTabuleiro(self):
        mensagem = ("JOGO DA VELHA\n\n"+"   A   B   C\n" +
                    "1  "+self.coord[0]["A"] + " | " + self.coord[0]["B"] + " | "+self.coord[0]["C"]+" \n" +
                    " -------------\n" +
                    "2  "+self.coord[1]["A"] + " | " + self.coord[1]["B"] + " | "+self.coord[1]["C"]+" \n" +
                    " -------------\n" +
                    "3  "+self.coord[2]["A"] + " | " + self.coord[2]["B"] + " | "+self.coord[2]["C"]+" \n\n")

        return mensagem

    def NovaJogada(self, coordenada, jogador):
        if self.Andamento is False:
            return "Começa um game antes burre"
        if self.jogadas == 0:
            self.jogador1 = jogador
        elif self.jogadas == 1:
            if jogador != self.jogador1:
                self.jogador2 = jogador
            else:
                return "Não ta vendo que não sua vez retardade?"
        else:
            if (self.jogadas % 2 == 0 and jogador == self.jogador2) or (self.jogadas % 2 == 1 and jogador == self.jogador1):
                return "Não é a vez de burre jogar!"
            if jogador != self.jogador1 and jogador != self.jogador2:
                return "Entrosa não, vc nem tá no jogo"

        if coordenada[0].isdigit():
            coordenada = coordenada[::-1]
        if self.validos.count(coordenada) == 0:
            return "Digite uma coordenada valida sue burre!"

        if(self.coord[int(coordenada[1])-1][coordenada[0]] != ' '):
            return "Você é cegue ou só é burre mesmo?"

        self.coord[int(coordenada[1])-1][coordenada[0]
                                         ] = 'X' if jogador == self.jogador1 else 'O'
        self.jogadas += 1

        status = self.Verifica()
        mensagem = self.EnviarTabuleiro()

        if status == "velha":
            mensagem += "\n\nDEU VELHA!!!"
            self.FimDeJogo()
        elif status != "":
            mensagem += f"\n\n {status} VENCEU!!!!"
            self.FimDeJogo()

        return mensagem

    def FimDeJogo(self):
        self.coord = [{"A": " ", "B": " ", "C": " "}, {
            "A": " ", "B": " ", "C": " "}, {"A": " ", "B": " ", "C": " "}]
        self.validos = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.jogadas = 0
        self.jogador1 = ""
        self.jogador2 = ""
        self.Andamento = False
