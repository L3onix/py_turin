from maquina import Maquina
from os import system
from time import sleep

#transforma a entrada do usuário em uma fita de processamento
def frase_to_fita(frase):
    fita = ['-', '*']
    for x in frase:
        fita.append(x)
    fita.append('*')
    return fita

def processar_fita(fita, maquina):
    pos_inicial = len(fita) - 1
    pos_atual = pos_inicial
    pos_final = 0

    maquina.estado = 'INICIO'

    while not(maquina.estado == 'PARAR'):
        resultado_processamento = maquina.consultar_tabela_de_processamento(fita[pos_atual])

        #imprimindo antes de reescrever celula
        imprimir_tela(fita.copy(), pos_atual, maquina.estado, 
            resultado_processamento['direcao'], resultado_processamento['valor_a_escrever'])
        input()
        #enter para apresentar próximo passo, se quiser automático substitua por print()

        fita[pos_atual] = resultado_processamento['valor_a_escrever']

        #imprime depois de reescrever celula
        imprimir_tela(fita.copy(), pos_atual, maquina.estado, 
            resultado_processamento['direcao'], resultado_processamento['valor_a_escrever'])
        input()

        pos_atual = ajustar_pos_atual(resultado_processamento['direcao'], pos_atual)

def imprimir_tela(fita, pos_atual, estado, direcao, valor_escrita):
    system('clear')
    line = ('__________________________')

    #IMPRIMINDO INFORMAÇÕES DA MÁQUINA
    maquina_title = line+'>> MAQUINA <<'+line
    print(maquina_title)
    print('ESTADO = ' + estado)
    print('DIREÇÃO = ' + direcao)
    print('VALOR P/ ESCREVER = ' + valor_escrita)
    print()

    #IMPRIMINDO FITA
    fita_title = line+'>> FITA <<'+line
    fita[pos_atual] = '< '+fita[pos_atual]+' >'
    print(fita_title)
    print(fita)
    
#ajusta a posição atual de acordo com o comando de direção retornado pela tabela de processamento
def ajustar_pos_atual(direcao, pos_atual):
    if (direcao == 'ESQUERDA'):
        return pos_atual - 1
    elif (direcao == 'DIREITA'):
        return pos_atual + 1


#criando uma máquina
mk_1 = Maquina()

#fita a ser processada
entrada_user = '101'
fita = frase_to_fita(entrada_user)

#processamento da fita
system('clear')
processar_fita(fita, mk_1)

