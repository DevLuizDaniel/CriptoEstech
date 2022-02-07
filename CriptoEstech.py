"""Bibliotecas necessárias para executar de forma correta o script
Caso não tenha instalado um dessas bibliotecas, basta usar o comando:
        pip install [nome da biblioteca] -> no terminal
Em seu sistema para realizar a instalação
"""
from os import system as sys
from tqdm import tqdm
from time import sleep

#Nessa parte eu resolvi fazer uma firula :)
sys('cls')
sys('color 02')
print('\t\t ============================================\n')
print('\t\t |\t\tCriptoEstech\t\t    |\n')
print('\t\t ============================================\n\n')

with tqdm(total=100) as carregamento:
    for i in range(10):
        sleep(1)
        carregamento.update(10)

sys('color 07')
#Agora bora pro código B)
print('\nSistema CriptoEstech \n\nSistema feito com base na esteganografia com o objetivo de esconder todo tipo de mensagem de texto em arquivos de imagem para deixar menos visível o possível ao seu destino final.\n\n')
sleep(1)
cont_cripto = 0
while cont_cripto == 0:
    try:
        arquivo = input('\n\nDigite o local do arquivo de imagem: ')

        #Você deve deixar pelo menos 3 linhas vazias antes de escrever o texto no arquivo de texto
        sys('cls')
        texto = input('\n\nDigite o local do arquivo de texto: \n\n**** Por favor, é importante disponibilizar, antes de escrever a mensagem no arquivo de texto, pelo menos 3 linhas vazias antes do texto****\n\n>')

        #Você pode por o local onde arquivo vai estar, caso queira colocar o arquivo em outro lugar
        sys('cls')
        nome_copia = input('\n\nDigite o nome e/ou o local do arquivo que será criptografado: ')

        sys(f'copy /B {arquivo} + {texto} {nome_copia}')
        print('\n\nCriptografia efetuada com sucesso!!!\n\n')
        selecionar_outro = input('Deseja escolher outro arquivo para a criptografia? ')
        lista_sim = ['sim', 's', 'y', 'yes']
        lista_nao = ['nao', 'não', 'n', 'no', 'not']
        if selecionar_outro.lower() in lista_sim:
            sys('cls')
            cont_cripto = 0
        elif selecionar_outro.lower() in lista_nao:
            sys('cls')
            print('\n\nEntão, esse é o fim, até a próxima ;)\n\n')
            cont_cripto = 1
            sys('pause')
        else:
            sys('cls')
            print('\n\nEu não entendi o que você disse, poderia repetir? \n\n')
            sleep(1)
            cont_cripto = 0

    except ValueError:
        cont_erro = 0
        while cont_erro == 0:
            print('Erro, Caminho do arquivo não informado ou não existe!\n\n')
            selecionar_outro = input('Deseja escolher novamente? ')
            lista_sim = ['sim', 's', 'y', 'yes']
            lista_nao = ['nao', 'não', 'n', 'no', 'not']
            if selecionar_outro.lower() in lista_sim:
                sys('cls')
                cont_cripto = 0
                cont_erro = 1
            elif selecionar_outro.lower() in lista_nao:
                sys('cls')
                print('\n\nEntão, esse é o fim, até a próxima ;)\n\n')
                cont_cripto = 1
                cont_erro = 1
                sys('pause')
            else:
                sys('cls')
                print('\n\nEu não entendi o que você disse, poderia repetir? \n\n')
                sleep(1)
                cont_erro = 0
