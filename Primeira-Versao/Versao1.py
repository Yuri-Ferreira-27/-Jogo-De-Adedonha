# Projeto jogo de Adedonha

# Módulos a serem utilizadas:
import random
import string
from time import sleep

# Funções a Serem utilizadas:
print('Bem vindo ao Adedonha! Vamos começar?\n')
sleep(2)
print('Rodada Inicial: \nLetra selecionada: ',random.choice(string.ascii_uppercase),'\n')
sleep(5)
opcao = str(input('Deseja prosseguir? S - Sim / N - Não '))
#print('\n')

i = 0
while opcao == 'S' or opcao == 's':
    i +=1
    print(f'Rodada {i}: \nLetra selecionada: ',random.choice(string.ascii_uppercase))
    sleep(5)
    opcao = str(input('Deseja prosseguir? S - Sim / N - Não '))
    print('\n')
    if opcao == 'N' or opcao == 'n':
        print('Jogo encerrado!')
        break
    if opcao != 'S' and opcao != 's':
        print('Comando inválido, tente novamente')
        opcao = str(input('Deseja prosseguir? S - Sim / N - Não '))
    print('\n')
