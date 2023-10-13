import random
import os

# Função para limpar a tela com base no sistema operacional
def limpar_tela():
    sistema = os.name
    if sistema == 'posix':
        os.system('clear')  # Limpa a tela no macOS ou no Linux
    elif sistema == 'nt':
        os.system('cls')    # Limpa a tela no Windows

# Abre o arquivo de frases
with open('frases.txt', 'r', encoding='utf-8', errors='ignore') as arquivo:
    frases = arquivo.readlines()

# Escolhe uma frase aleatoriamente
frase_motivacional = random.choice(frases)

# Limpa a tela
limpar_tela()

# Exibe a frase escolhida
print(frase_motivacional)