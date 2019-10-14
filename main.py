import random
import re
import functions
import mapeamento_direto as md
import mapeamento_associativo as ma
import mapeamento_associativo_conjunto as mac
import fifo
import lru
import lfu
import aleatorio




tam_cache = input('\nInsira o tamanho da memoria cache a ser utilizada:')
tam_cache = int(tam_cache)
tipo_mapeamento = input('\nInsira o tipo de mapeamento da memoria cache a ser utilizado (DI = Direto, AS = Associativo, AC = Associativo por Conjunto):')
arquivo_leituras = input('\nInsira o nome e endereço do arquivo de leitura a ser acessado (ex: C:/Users/exemplo.txt):')
if tipo_mapeamento == 'AC' :
  num_conjuntos = input('\nInsira o numero de conjuntos a ser utilizado:')
  num_conjuntos = int(num_conjuntos)
else:
  num_conjuntos = 1
if tipo_mapeamento != 'DI' : 
  politica_substituicao  = input('\nInsira o tipo de algoritmo de substituicao da memoria cache a ser utilizado (FIFO, RANDOM, LFU, LRU ou ALL = Todos os mapeamentos possiveis:')
else:
  politica_substituicao = 'ALL'


if num_conjuntos <= 0:
  print('\n------------------------------')
  print('Numero de conjuntos nao pode ser 0!')
  print('------------------------------')
  exit()


if arquivo_leituras == '':
  print('\n------------------------------')
  print('Arquivo de leitura informado incorretamente')
  print('------------------------------')
  exit()

# lê o arquivo de netrada e armazena cada uma das posições de memória a serem acessadas numa lista
try:
  f = open(arquivo_leituras, "r")
  posicoes_acesso_memoria = []
  for posicao_memoria in f:
    posicoes_acesso_memoria.append(int(re.sub(r"\r?\n?$", "", posicao_memoria, 1)))
  f.close()
except IOError as identifier:
  print('\n------------------------------')
  print('O Arquivo \'{}\' nao pode ser encontrado.'.format(arquivo_leituras))
  print('------------------------------')
  exit()

if len(posicoes_acesso_memoria) == 0:
    print('\n------------------------------')
    print('Arquivo vazio!'.format(arquivo_leituras))
    print('------------------------------')
    exit()

print('+====================+')
print('| SIMULADOR DE CACHE |')
print('+====================+')
print('+ Configurando parametros da cache+')


if tipo_mapeamento != 'DI':
  if politica_substituicao != 'RANDOM' and politica_substituicao != 'FIFO' and politica_substituicao != 'LRU' and politica_substituicao != 'LFU' and politica_substituicao != 'ALL':
    print('\n------------------------------')
    print(' A politica de substituicao {} nao existe.'.format(politica_substituicao))
    print('------------------------------')
    exit()

# se o tipo do mapeamento for direto DI
if tipo_mapeamento == 'DI':
  md.executar_mapeamento_direto(tam_cache, posicoes_acesso_memoria)
elif tipo_mapeamento == 'AS':
  if (politica_substituicao == 'ALL'):
    ma.executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, 'RANDOM')
    ma.executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, 'FIFO')
    ma.executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, 'LRU')
    ma.executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, 'LFU')
  else:
    ma.executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, politica_substituicao)

elif tipo_mapeamento == 'AC':
  # o número de conjuntos deve ser um divisor do total da memória
  if tam_cache%num_conjuntos != 0:
    print('\n------------------------------')
    print('Numero de conjuntos {} deve ser maior que um e um possível divisor do tamanho de memoria cache disponivel {}.'.format(num_conjuntos, tam_cache))
    print('------------------------------')
    exit()

  if (politica_substituicao == 'ALL'):
    mac.executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, 'RANDOM')
    mac.executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, 'FIFO')
    mac.executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, 'LRU')
    mac.executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, 'LFU')
  else:
    mac.executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, politica_substituicao)
else:
  print('\n------------------------------')
  print('Mapeamento \'{}\'nao e um tipo de mapeamento valido.'.format(tipo_mapeamento))
  print('------------------------------')
  exit()


print('\n')
print('-'*60)
print('Parametros da Simulacao')
print('-'*60)
print('Numero de posicoes de memoria: {}'.format(len(posicoes_acesso_memoria)))
print('As posicoes sao: {}'.format(posicoes_acesso_memoria))
print('Tamanho da memoria cache: {}'.format(tam_cache))
print("Tipo Mapeamento: {}".format(tipo_mapeamento))
if tipo_mapeamento == 'AC':
    print("Quantidade de Conjuntos: {}".format(num_conjuntos))
print("Algoritmos de Substituição: {}".format(politica_substituicao))
print('-'*60)
