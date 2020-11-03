# Batalha Naval

Implementação do jogo [Batalha Naval](https://pt.wikipedia.org/wiki/Batalha_naval_(jogo)) baseando-se no protocolo [TCP](https://pt.wikipedia.org/wiki/Transmission_Control_Protocol)

### Instalando Dependências

Clone esse repositório e execute:
```
pip3 install argparse
```

### Uso

# Servidor
```
python3 server.py [-h] [-p PORTA]
```
Informe a porta pela qual pretende-se comunicar com o jogador.

Exemplo:
```
python3 server.py -p 9999
```

# Cliente
```
python3 client.py [-h] [-i HOST] [-p PORTA] [-f ARQUIVO]
```

Informe o endereço IP e a porta do servidor que arbitrará o jogo e o arquivo que corresponde à posição inicial do posicionamento das embarcações do jogador.

Exemplo:
```
python3 client.py -i 127.0.1.1 -p 9999 -f ./posicionamento_tabuleiro.txt
```

Todos os parâmetros, tanto do servidor quanto do cliente são opcionais.

**[GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html)**
