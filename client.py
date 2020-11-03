import socket
import argparse

# Configuracao dos argumentos
parser = argparse.ArgumentParser(description = 'Simples implementação do jogo Batalha Naval.')
parser.add_argument('-i', action = 'store', dest = 'host', default = '127.0.1.1', required = False, help = 'Endereço IP do servidor.')
parser.add_argument('-p', action = 'store', dest = 'porta', default = 9999, required = False, help = 'Porta a ser usada pelo servidor.')
parser.add_argument('-f', action = 'store', dest = 'arquivo', default = 'posicao_tabuleiro.txt', required = False, help = 'Arquivo para posicionamento do tabuleiro.')

def get_posicoes(caminho_arquivo):
    arquivo = open(caminho_arquivo, 'r')
    str_arquivo = ''
    for char in arquivo: str_arquivo += char
    return str_arquivo

def main():
    # Recebe os argumentos. Se as variaveis nao forem passadas, retorna -h
    arguments = parser.parse_args()
    # Instancia o socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Armazena o nome do host, seu endereço IP e a porta
    host = arguments.host
    porta = int(arguments.porta)
    caminho_arquivo = arguments.arquivo
    # Estabelece conexão com o servidor
    print('Inicializando jogo...')
    print('Tentando estabelecer conexão com o servidor: {}:{}'.format(host, porta))
    soc.connect((host, porta))
    print("Conexão estabelecida\n")
    # Envia o posicionamento do tabuleiro
    posicoes = get_posicoes(caminho_arquivo)
    soc.send(posicoes.encode())
    # Recebe e exibe mensagem inicial
    mensagem_inicial = soc.recv(1024)
    print(mensagem_inicial.decode())

    while True:
        jogada = input('Selecione qual posição atacar: ')
        # Testa se o jogador não pretende abandonar a partida
        if jogada == '[sair]':
            break
        # Execuda a jogada
        soc.send(jogada.encode())
        # Recebe as consequências da sua jogada
        status_partida = soc.recv(1024).decode()
        print(status_partida)
        # Testa se o jogador venceu a partida
        if 'PARTIDA' in status_partida:
            break

# Chama a função main
if __name__ == '__main__':
    main()