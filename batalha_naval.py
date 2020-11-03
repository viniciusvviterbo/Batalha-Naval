class Tabuleiro():
    def __init__(self):
        self.tabuleiroA = {
            'a': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],  
            'b': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
            'c': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
            'd': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
            'e': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
            'f': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
            'g': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
            'h': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
            'i': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], 
            'j': ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
        }
        self.tabuleiroB = {
            'a': ['4','4','~','~','~','~','~','~','~','~'],  
            'b': ['~','~','~','~','~','~','3','~','~','~'], 
            'c': ['~','1','~','4','4','~','3','~','~','~'], 
            'd': ['~','1','~','~','~','~','3','~','~','2'], 
            'e': ['~','1','~','~','~','~','~','~','~','2'], 
            'f': ['~','1','~','2','2','2','2','~','~','2'], 
            'g': ['~','1','~','~','~','~','~','~','~','2'], 
            'h': ['3','~','4','~','~','~','~','~','~','~'], 
            'i': ['3','~','4','~','~','~','~','~','~','~'], 
            'j': ['3','~','~','3','3','3','~','~','4','4']
        }
        self.turno = 1
        
    # Configura o tabuleiro do jogador informado
    def set_tabuleiro(self, jogador, posicionamento):
        tabuleiro = self.tabuleiroA if jogador == 'A' else self.tabuleiroB
        letra = 97
        num = 0
        for pos in range(0, len(posicionamento)):
            if posicionamento[pos] == '\n': continue
            tabuleiro[chr(letra)][num] = posicionamento[pos]
            num += 1
            if num == 10:
                letra += 1
                if letra == 107: break
                num = 0
    
    # Realiza um ataque do jogador informado na posição informada 
    def jogada(self, jogador, posicao):
        tabuleiro_alvo = self.tabuleiroA if jogador == 'B' else self.tabuleiroB 
        resposta = 'MISS'
        # Testa se algum alvo foi atingido
        if(tabuleiro_alvo[posicao[0]][posicao[1] - 1] != '~'):
            resposta = 'HIT'
        # Atualiza a contagem de turnos
        self.turno += 1
        # Marca o local atingido
        tabuleiro_alvo[posicao[0]][posicao[1] - 1] = 'X'

        # Testa se não existem mais navios a serem combatidos
        finalizada = True
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        for letra in letras:
            for num in range(0, 10):
                if tabuleiro_alvo[letra][num] != 'X' and tabuleiro_alvo[letra][num] != '~':
                    finalizada = False
                    break

        if finalizada:
            resposta += ' - PARTIDA VENCIDA!'

        return resposta

    # Imprime o status do jogo do ponto de vista do jogador informado
    def get_status_jogo(self, jogador):
        status = ''

        tab_eu = self.tabuleiroA.copy() if jogador == 'A' else self.tabuleiroB.copy()
        tab_outro = self.tabuleiroA.copy() if jogador == 'B' else self.tabuleiroB.copy()
        
        status += ('TURNO: {}\n\n'.format(self.turno))
        status += ('VOCÊ:                  \t\t\tOPONENTE:\n\n')
        status += ('  1 2 3 4 5 6 7 8 9 10\t\t\t   1 2 3 4 5 6 7 8 9 10 \n')
        for linha in tab_eu:
            status += '{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(
                linha,
                tab_eu[linha][0],
                tab_eu[linha][1],
                tab_eu[linha][2],
                tab_eu[linha][3],
                tab_eu[linha][4],
                tab_eu[linha][5],
                tab_eu[linha][6],
                tab_eu[linha][7],
                tab_eu[linha][8],
                tab_eu[linha][9],
                '\t\t\t',
                linha,
                self.get_pos_censurado(tab_outro[linha][0]),
                self.get_pos_censurado(tab_outro[linha][1]),
                self.get_pos_censurado(tab_outro[linha][2]),
                self.get_pos_censurado(tab_outro[linha][3]),
                self.get_pos_censurado(tab_outro[linha][4]),
                self.get_pos_censurado(tab_outro[linha][5]),
                self.get_pos_censurado(tab_outro[linha][6]),
                self.get_pos_censurado(tab_outro[linha][7]),
                self.get_pos_censurado(tab_outro[linha][8]),
                self.get_pos_censurado(tab_outro[linha][9]),
                '\n'
            )
            
        return status

    # Retorna a posição do tabuleiro informado censurado, com exceção das posições já atingidas
    def get_pos_censurado(self, posicao):
        new_posicao = posicao if posicao == 'X' else '-'
        return new_posicao

