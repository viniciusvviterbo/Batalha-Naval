#import socketserver
import socket
import argparse
import batalha_naval
import random

# Configuracao dos argumentos
parser = argparse.ArgumentParser(description = 'Simples implementação do jogo Batalha Naval.')
parser.add_argument('-p', action = 'store', dest = 'porta', default = 9999, required = False, help = 'Porta a ser usada pelo servidor.')

def posicao_aleatoria():
    letra = chr(random.randint(97, 106))
    numero = random.randint(1, 10)
    return (letra, numero)

def main():
    print('Inicializando servidor...')
    # Instanciamento do jogo
    partida = batalha_naval.Tabuleiro()
    # Recebe os argumentos. Se as variaveis nao forem passadas, retorna -h
    arguments = parser.parse_args()
    # Instancia o socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Armazena o nome do host, seu endereço IP e a porta
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    porta = int(arguments.porta)
    # Configura o socket à porta e o nome do host
    soc.bind((host, porta))
    print(host, '({})'.format(ip))
    # Espera por uma conexão do client
    soc.listen(1)
    print('Esperando conexão do client...')
    conexao, addr = soc.accept()
    print('Recebida conexão de ', addr[0], '(', addr[1], ')\n')
    print('Conexão estabelecida. Conectado de: {}, ({})'.format(addr[0], addr[1]))
    print('\n\n')
    # Recebe o posicionamento do tabuleiro do jogador
    data = conexao.recv(1024)
    posicionamento = data.decode()
    partida.set_tabuleiro('A', posicionamento)
    # Envia mensagem de boas-vindas
    mensagem_inicial = 'Bem-vind@ e boa partida!\n\n'
    mensagem_inicial += partida.get_status_jogo('A')
    conexao.send(mensagem_inicial.encode())

    while True:
        # Recebe jogada do client
        data = conexao.recv(1024)
        jogada = data.decode()

        if jogada == 'p':
            # Envia o resultado do turno
            retorno = partida.get_status_jogo('A')
            conexao.send(retorno.encode())

        else:
            posicao = (jogada[0], int(jogada[1:]))
            print('{} fez uma jogada: {}'.format(addr[0], jogada))
            # Realiza a jogada no tabuleiro
            resultado = partida.jogada('A', posicao)

            # Realiza a jogada aleatória do oponente
            posicao = posicao_aleatoria()
            print('OPONENTE fez uma jogada: {}'.format(posicao))
            resultado_oponente = partida.jogada('B', posicao)

            # Envia o resultado da jogada
            if 'PARTIDA' in resultado:
                conexao.send(resultado.encode())
                break
            elif 'PARTIDA' in resultado_oponente:
                conexao.send('PARTIDA ENCERRADA - VOCÊ FOI DERROTADO!'.encode())
                break
            else:
                conexao.send(resultado.encode())

# Chama a função main
if __name__ == '__main__':
    main()