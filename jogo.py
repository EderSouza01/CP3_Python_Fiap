import random

# Função para inicializar o tabuleiro
def iniciar_jogo():
    return [" " for _ in range(9)]

# Função para exibir o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\n")

# Função para escolher entre X e O
def escolher_simbolo():
    simbolo = ""
    while simbolo not in ["X", "O"]:
        simbolo = input("Escolha o seu símbolo (X ou O): ").upper()
    return simbolo

# Função para atualizar o tabuleiro
def atualizar_tabuleiro(tabuleiro, posicao, simbolo):
    if tabuleiro[posicao] == " ":
        tabuleiro[posicao] = simbolo
        return True
    return False

# Função para verificar vencedor ou empate
def verificar_vencedor(tabuleiro, simbolo):
    # Combinacoes de vitória
    combinacoes = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Linhas
                   (0, 3, 6), (1, 4, 7), (2, 5, 8), # Colunas
                   (0, 4, 8), (2, 4, 6)]            # Diagonais
    for c in combinacoes:
        if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == simbolo:
            return True
    return False

# Função para verificar se houve empate
def verificar_empate(tabuleiro):
    return " " not in tabuleiro

# Função para o computador jogar
def jogada_computador(tabuleiro, simbolo_computador):
    while True:
        posicao = random.randint(0, 8)
        if tabuleiro[posicao] == " ":
            atualizar_tabuleiro(tabuleiro, posicao, simbolo_computador)
            break

# Função para reiniciar o jogo
def reiniciar_jogo():
    escolha = input("Deseja jogar novamente? (S/N): ").upper()
    return escolha == "S"

# Função principal
def jogo_da_velha():
    print("Bem-vindo ao Jogo da Velha!")
    
    while True:
        # Inicia o tabuleiro
        tabuleiro = iniciar_jogo()
        mostrar_tabuleiro(tabuleiro)
        
        # Escolha do símbolo pelo jogador
        simbolo_jogador = escolher_simbolo()
        simbolo_computador = "O" if simbolo_jogador == "X" else "X"
        
        jogador_vez = True  # Se o jogador começa ou não

        # Loop do jogo
        while True:
            if jogador_vez:
                # Jogador faz a jogada
                posicao = int(input("Escolha uma posição (0-8): "))
                if atualizar_tabuleiro(tabuleiro, posicao, simbolo_jogador):
                    mostrar_tabuleiro(tabuleiro)
                    if verificar_vencedor(tabuleiro, simbolo_jogador):
                        print("Você venceu!")
                        break
                    jogador_vez = False
            else:
                # Computador faz a jogada
                print("Computador está jogando...")
                jogada_computador(tabuleiro, simbolo_computador)
                mostrar_tabuleiro(tabuleiro)
                if verificar_vencedor(tabuleiro, simbolo_computador):
                    print("O computador venceu!")
                    break
                jogador_vez = True

            # Verifica se o jogo empatou
            if verificar_empate(tabuleiro):
                print("O jogo empatou!")
                break
        
        # Pergunta se deseja reiniciar
        if not reiniciar_jogo():
            break

# Iniciar o jogo
jogo_da_velha()
