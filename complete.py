import random, re


# Essa lista irá armazenar qual o número de vezes que uma
# determinada posição da memória cache foi acessada.
contador_lfu = {}


# Essa lista irá armazenar a ordem que a posição da memória
# principal foi inserida na memória cache, quando ocorre um CACHE MISS
# a posição ZERO dessa lista será removida e a nova posição de memória
# será inserida no topo da lista.
contador_fifo = {}


def existe_posicao_vazia(memoria_cache, num_conjuntos, posicao_memoria):
  """Verifica se existe na cache uma posição de memória que ainda não foi utilizada,
  se existir, essa posição é retornada.

  Arguments:
    memoria_cache {list} -- memória cache
    num_conjuntos {int} -- número de conjuntos da cache
    posicao_memoria {int} -- posição de memória que se quer armazenar na cache

  Returns:
    [int] -- com a primeira posição de memória vazia do conjunto
  """
  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache, num_conjunto, num_conjuntos)

  # verifica se alguma das posições daquele conjunto está vazia
  for x in lista_posicoes:
    if memoria_cache[x] == -1:
      return x
  return -1


def imprimir_contador_fifo():
  """Função de debug que exibe o estado do contador FIFO
  """
  print('+--------------------------------------+')
  print("| Contador FIFO                        |")
  print('+--------------------------------------+')
  print("|Conjunto | Próxima Posição Substituir |")
  print('+---------+----------------------------+')
  for index, x in enumerate(contador_fifo):
    print("|{:>9}|{:>28}|".format(index,x))
  print('+---------+----------------------------+')


def inicializar_contador_fifo():
  """Seta os valores do contador fifo para que a primeira subsitituição
  ocorra no primeiro elemento que faz parte do conjunto
  """
  # cria no contador fifo uma posição para cada conjunto
  for x in range(0, num_conjuntos):
    contador_fifo[x] = 0

  
  imprimir_contador_fifo()


def imprimir_contador_lfu():
    """Função de debug que exibe o estado do contador LFU
    """
    print('+--------------------------------------+')
    print("| Contador LFU                         |")
    print('+--------------------------------------+')
    print("|Posição Cache | Qtd Acessos           |")
    print('+---------+----------------------------+')
    for index, x in enumerate(contador_lfu):
      print("|{:>9}|{:>28}|".format(index,contador_lfu[x]))
    print('+---------+----------------------------+')


def inicializar_contador_lfu():
  """Seta os valores do contador LFU para zero, ou seja, a posição de memória que ocupa aquela
  posição da cache ainda não foi utilizada. Para cada posição da cache teremos um contador
  que será somado tada vez que houver um CACHE HIT e, será zerado quando a posição for substituida
  """
  # cria on contador LFU uma posiçõao para caqda posição de memória
  for x in range(0, tam_cache):
    contador_lfu[x] = 0

  
  imprimir_contador_lfu()


def get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos):
  """Retorna o número do conjunto onde essa posição de memória é sempre mapeada

  Arguments:
    posicao_memoria {int} -- posição de memória que se quer acessar
    num_conjuntos {int} -- número de conjuntos que a cache possui
  """
  return int(posicao_memoria)%int(num_conjuntos)



def print_memoria_cache(memoria_cache, num_conjuntos):

  print("/--------------------------\ ")
  if num_conjuntos ==0:
        print("|      Cache Direto        |")
  elif  num_conjuntos ==1:
        print("|     Cache Associativo    |")
  else:
        print("|Cache Associativo Conjunto|")
  print("|------------------------------|")
  if num_conjuntos >1:
        print("|Tamanho: {:>11}|\n|Conjuntos: {:>10}|".format(len(memoria_cache), num_conjuntos))
  else:      
        print("|Tamanho cache: {:>21}| ".format(len(memoria_cache)))
  print("|------------------------------|")
  if num_conjuntos <=1:
        print("|Pos cache |Posição Memória|")
        print("|----------|---------------|")
        for posicao, valor in memoria_cache.items():
            print("|{:>10}|{:>15}|".format(posicao, valor))
        print("|----------|---------------|")
  else:
     print("|#\t| Cnj\t|   Pos Memória|")
     print("|-------|-------|--------------|")
     for posicao, valor in memoria_cache.items():
         num_conjunto = get_num_conjunto_posicao_memoria(posicao, num_conjuntos)
         print("|{} \t|{:4}\t|\t   {:>4}|".format(posicao, num_conjunto, valor)) 
     print("|-------|-------|--------------|")


def inicializar_cache(tam_cache):
  """Cria uma memória cache zerada utilizando dicionários (chave, valor) e com
  valor padrão igual a '-1'

  Arguments:
    tam_cache {int} -- tamanho total de palavras da cache

  Returns:
    [list] -- [dicionário]
  """
  # zera tota a memória cache
  memoria_cache = {}

  # popula a memória cache com o valor -1, isso indica que a posição não foi usada
  for x in range(0, tam_cache):
    memoria_cache[x] = -1

  return memoria_cache


def verifica_posicao_em_cache_associativo_conjunto(memoria_cache, num_conjuntos, posicao_memoria,):
  """Verifica se uma determinada posição de memória está na cache
    no modo associativo / associativo por conjunto

  Arguments:
    memoria_cache {list} -- memória cache
    num_conjuntos {int} -- número de conjuntos do cache
    posicao_memoria {int} -- posição que se deseja acessar
  """
  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)

  while num_conjunto < len(memoria_cache):
    if memoria_cache[num_conjunto] == posicao_memoria:
      return num_conjunto

    num_conjunto += num_conjuntos

  # não achou a posição de memória na cache
  return -1


def get_lista_posicoes_cache_conjunto(memoria_cache, num_conjunto, num_conjuntos):
  """Retorna uma lista com todas as posições da memória cache que fazem
  parte de um determinado conjunto.

  Arguments:
    memoria_cache {list} -- memória cache
    num_conjunto {int} -- número do conjunto que se quer saber quais são os endereçamentos associados com aquele conjunto
    num_conjuntos {int} -- quantidade total de conjuntos possíveis na memória

  Returns:
    [list] -- lista de posições de memória associada com um conjunto em particular
  """
  lista_posicoes = []
  posicao_inicial = num_conjunto
  while posicao_inicial < len(memoria_cache):
    lista_posicoes.append(posicao_inicial)
    posicao_inicial += num_conjuntos
  return lista_posicoes


def politica_substituicao_RANDOM(memoria_cache, num_conjuntos, posicao_memoria):
  """Nessa politica de substituição, no momento que ocorrer um CACHE MISS,
  será sorteado um elemento do conjunto para ser substituído pela nova posição
  de memória.

  Arguments:
    memoria_cache {list} -- memóiria cache
    num_conjuntos {int} -- quantidade de conjuntos
    posicao_memoria {int} -- posição de memória que será acessada
  """
  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)

  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, num_conjuntos)

  # seleciona de forma aleatória uma das posições de memória
  # que fazem parte do conjunto em particular e armazena dentro
  # daquela posição o valor da memória principal
  posicao_troca_memoria = random.choice(lista_posicoes)


  print('Posição de memória cache que será trocada é: {}'.format(posicao_troca_memoria))

  memoria_cache[posicao_troca_memoria] = posicao_memoria


def politica_substituicao_FIFO(memoria_cache, num_conjuntos, posicao_memoria):
  """Nessa politica de substituição, o primeiro elemento que entra é o primeiro elemento que sai,
  funciona exatamente como uma fila.

  Arguments:
    memoria_cache {list} -- memóiria cache
    num_conjuntos {int} -- quantidade de conjuntos
    posicao_memoria {int} -- posição de memória que será acessada
  """
  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)
  posicao_substituir = contador_fifo[num_conjunto]
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, num_conjuntos)

  imprimir_contador_fifo()
  print('Posição Memória: {}'.format(posicao_memoria))
  print('Conjunto: {}'.format(num_conjunto))
  print('Lista posições: {}'.format(lista_posicoes))
  print('Posição para subistituição: {}'.format(posicao_substituir))

  memoria_cache[lista_posicoes[posicao_substituir]] = posicao_memoria

  contador_fifo[num_conjunto] += 1

  if contador_fifo[num_conjunto] >= (len(memoria_cache)/num_conjuntos):
    contador_fifo[num_conjunto] = 0


  print('Posição de memória cache que será trocada é: {}'.format(lista_posicoes[posicao_substituir]))


def politica_substituicao_LFU(memoria_cache, num_conjuntos, posicao_memoria):
  """Nessa politica de substituição, o elemento que é menos acessado é removido da
  memória cache quando ocorrer um CACHE MISS. A cada CACHE HIT a posição do HIT ganha um ponto
  de acesso, isso é usado como contador para saber qual posição deve ser removida no caso de
  CACHE MISS.

  Arguments:
    memoria_cache {list} -- memóiria cache
    num_conjuntos {int} -- quantidade de conjuntos
    posicao_memoria {int} -- posição de memória que será acessada
  """
  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, num_conjuntos)

  # descobrir dentro do conjunto qual posição da cache tem menos acesso
  posicao_substituir = 0
  if len(lista_posicoes) > 1:


    imprimir_contador_lfu()

    # descobrir qual das posições é menos usada
    lista_qtd_acessos = []
    for qtd_acessos in lista_posicoes:
      lista_qtd_acessos.append(contador_lfu[qtd_acessos])

    posicoes_com_menos_acesso = min(lista_qtd_acessos)
    candidatos_lfu = []

    for qtd_acessos in lista_posicoes:
      if contador_lfu[qtd_acessos] == posicoes_com_menos_acesso:
        candidatos_lfu.append(qtd_acessos)

    # para garantir ordem aleatória de escolha caso duas ou mais posições
    # tenham o mesmo número de acessos
    posicao_substituir = random.choice(candidatos_lfu)

  # zera o número de acessos a posição que foi substituida
  contador_lfu[posicao_substituir] = 0

  # altera a posição de memória que está na cache
  memoria_cache[posicao_substituir] = posicao_memoria

  print('Posição Memória Lida No Arquivo: {}'.format(posicao_memoria))
  print('Conjunto: {}'.format(num_conjunto))
  print('Número de Acesso Da Posição com Menos Acesso: {}'.format(posicoes_com_menos_acesso))
  print('Lista Posições do  conjunto: {}'.format(lista_posicoes))
  print('Lista com as posições menos acessadas do conjunto: {}'.format(candidatos_lfu))
  print('Posição Cache Substituir: {}'.format(posicao_substituir))
  print('Posição de memória cache que será trocada é: {}'.format(posicao_substituir))


def politica_substituicao_LRU(memoria_cache, num_conjuntos, posicao_memoria, posicao_cache_hit, flag_hit):
  """Nessa politica de substituição quando ocorre um HIT a posição vai para o topo da fila,
  se ocorrer um MISS remove o elemento 0 e a posição da cache onde a memória foi alocada é
  colocada no topo da fila
  """
  
  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, num_conjuntos)
  
  
  
  if flag_hit ==0: # copiar os valores de cada posição da cache do conjunto em questão uma posição para traz
      for posicao_cache in lista_posicoes:
        proxima_posicao = posicao_cache+num_conjuntos
        if proxima_posicao < len(memoria_cache):
          memoria_cache[posicao_cache] = memoria_cache[proxima_posicao]
  if flag_hit ==1:  # copiar os valores de cada posição da cache do conjunto em questão uma posição para traz
      for posicao_cache in lista_posicoes:
        if posicao_cache_hit <= posicao_cache:
          # em uma cache com 4 conjuntos e 20 posições, as posições do 'conjunto 0' são:
          # [0, 4, 8, 12, 16], se o hit for na poição 4, então, então, será necessário copiar os dados da posição
          # 0 não faz nada
          # 4 <- 8
          # 8 <- 12
          # 12 <- 16
          # 16 <- 4
          proxima_posicao = posicao_cache+num_conjuntos
          if proxima_posicao < len(memoria_cache):
            memoria_cache[posicao_cache] = memoria_cache[proxima_posicao]    
  # coloca a posição que acabou de ser lida na topo da lista, assim, ela nesse momento é a última que será removida
  memoria_cache[lista_posicoes[-1]] = posicao_memoria

  
  print('Posição Memória: {}'.format(posicao_memoria))
  print('Conjunto: {}'.format(num_conjunto))
  print('Lista posições: {}'.format(lista_posicoes))



def executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, politica_substituicao='RANDOM'):
  """Executa a operação de mapeamento associativo, ou seja, não existe uma posição específica
  para o mapemento de uma posição de memória.

  Arguments:
    tam_cache {int} -- tamanho total de palavras da cache
    num_conjuntos {int} -- quantidade de conjuntos na cache
    posicoes_acesso_memoria {list} -- quais são as posições de memória que devem ser acessadas
    politica_substituicao {str} -- Qual é a política para substituição caso a posição de memória desejada não esteja na cache E não exista espaço vazio
  """

  memoria_cache = inicializar_cache(tam_cache)

  # se o número de conjuntos for igual a zero, então estamos simulando
  # com a cache associativo!
  nome_mapeamento = 'Associativo'
  if num_conjuntos == 1:
    print_memoria_cache(memoria_cache,1)
  else:
    nome_mapeamento = 'Associativo Por Conjunto'
    print_memoria_cache(memoria_cache, num_conjuntos)

  num_hit = 0
  num_miss = 0

  # se a política for fifo então inicializa a lista de controle
  if politica_substituicao == 'FIFO':
    inicializar_contador_fifo()

  # se a política for fifo então inicializa a lista de controle
  if politica_substituicao == 'LFU':
    inicializar_contador_lfu()

  # percorre cada uma das posições de memória que estavam no arquivo
  for index, posicao_memoria in enumerate(posicoes_acesso_memoria):
    print('\n\n\nInteração número: {}'.format(index+1))
    # verificar se existe ou não a posição de memória desejada na cache
    inserir_memoria_na_posicao_cache = verifica_posicao_em_cache_associativo_conjunto(memoria_cache, num_conjuntos, posicao_memoria)

    # a posição desejada já está na memória
    if inserir_memoria_na_posicao_cache >= 0:
      num_hit += 1
      print('Cache HIT: posiçao de memória {}, posição cache {}'.format(posicao_memoria, inserir_memoria_na_posicao_cache))

      # se for LFU então toda vez que der um HIT será incrementado o contador daquela posição
      if politica_substituicao == 'LFU':
        contador_lfu[inserir_memoria_na_posicao_cache] += 1
        imprimir_contador_lfu()

      # se for LRU então toda vez que der um HIT será incrementado o contador daquela posição
      if politica_substituicao == 'LRU':
        politica_substituicao_LRU(memoria_cache, num_conjuntos, posicao_memoria, inserir_memoria_na_posicao_cache,1)

    else:
      num_miss += 1
      print('Cache MISS: posiçao de memória {}'.format(posicao_memoria))

      # verifica se existe uma posição vazia na cache, se sim aloca nela a posição de memória
      posicao_vazia = existe_posicao_vazia(memoria_cache, num_conjuntos, posicao_memoria)


      print('Posição da cache ainda não utilizada: {}'.format(posicao_vazia))
      print('\nLeitura linha {}, posição de memória {}.'.format(index,posicao_memoria))

      ########
      # se posicao_vazia for < 0 então devemos executar as políticas de substituição
      ########
      if posicao_vazia >= 0:
        memoria_cache[posicao_vazia] = posicao_memoria
      elif politica_substituicao == 'RANDOM':
        politica_substituicao_RANDOM(memoria_cache,num_conjuntos,posicao_memoria)
      elif politica_substituicao == 'FIFO':
        politica_substituicao_FIFO(memoria_cache,num_conjuntos,posicao_memoria)
      elif politica_substituicao == 'LFU':
        politica_substituicao_LFU(memoria_cache,num_conjuntos,posicao_memoria)
      elif politica_substituicao == 'LRU':
        politica_substituicao_LRU(memoria_cache,num_conjuntos,posicao_memoria,0,0)


    if num_conjuntos == 1:
      print_memoria_cache(memoria_cache,1)
    else:
      print_memoria_cache(memoria_cache, num_conjuntos)



  # se for LFU e com debug imprimir os dados computador no contador LFU
  if politica_substituicao == 'LFU':
    imprimir_contador_lfu()

  print('\n\n-----------------')
  print('Resumo Mapeamento {}'.format(nome_mapeamento))
  print('-----------------')
  print('Política de Substituição: {}'.format(politica_substituicao))
  print('-----------------')
  print('Total de memórias acessadas: {}'.format(len(posicoes_acesso_memoria)))
  print('Total HIT {}'.format(num_hit))
  print('Total MISS {}'.format(num_miss))
  taxa_cache_hit = (num_hit / len(posicoes_acesso_memoria))*100
  print('Taxa de Cache HIT {number:.{digits}f}%'.format(number=taxa_cache_hit, digits=2))


def executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, politica_substituicao):
  """O mapeamento associativo é um tipo de mapeamento associativo por conjunto
  ou o número de conjunto é igual a 1

  Arguments:
    tam_cache {int} -- tamanho total de palavras da cache
    posicoes_acesso_memoria {list} - quais são as posições de memória que devem ser acessadas
    politica_substituicao {str} -- qual será a política de subistituição
  """
  # o número 1 indica que haverá apenas um único conjunto no modo associativo por conjunto
  # que é igual ao modo associativo padrão! :) SHAZAM
  executar_mapeamento_associativo_conjunto(tam_cache, 1, posicoes_acesso_memoria, politica_substituicao)


def executar_mapeamento_direto(tam_cache, posicoes_acesso_memoria):
  """Executa a operação de mapeamento direto.

  Arguments:
    tam_cache {int} -- tamanho total de palavras da cache
    posicoes_acesso_memoria {list} - quais são as posições de memória que devem ser acessadas
  """
  # zera tota a memória cache
  memoria_cache = inicializar_cache(tam_cache)

  print('Situação Inicial da Memória Cache')
  print_memoria_cache(memoria_cache,0)

  hmstatus = ''
  num_hit = 0;
  num_miss = 0
  for index, posicao_memoria in enumerate(posicoes_acesso_memoria):
    # no mapeamento direto, cada posição da memória principal tem uma posição
    # específica na memória cache, essa posição será calculada em função
    # do mod da posição acessada em relação ao tamanho total da cache
    posicao_cache = posicao_memoria % tam_cache

    # se a posição de memória principal armazenada na linha da cache for a posição
    # desejada então dá hit, caso contrário da miss
    if memoria_cache[posicao_cache] == posicao_memoria:
      num_hit += 1
      hmstatus = 'Hit'
    else:
      num_miss += 1
      hmstatus = 'Miss'

    memoria_cache[posicao_cache] = posicao_memoria

    print('\nLeitura linha {},  posição de memória desejada {}.'.format(index,posicao_memoria))
    print('Status: {}'.format(hmstatus))
    print_memoria_cache(memoria_cache,0)


    print('Poisição de Memória: {} \nPosição Mapeada na Cache: {}'.format(posicao_memoria, posicao_cache))

  print('\n\n------------------------')
  print('Resumo Mapeamento Direto')
  print('------------------------')
  print('Total de memórias acessadas: {}'.format(len(posicoes_acesso_memoria)))
  print('Total HIT: {}'.format(num_hit))
  print('Total MISS: {}'.format(num_miss))
  taxa_cache_hit = (num_hit / len(posicoes_acesso_memoria))*100
  print('Taxa de Cache HIT: {number:.{digits}f}%'.format(number=taxa_cache_hit, digits=2))

##########################
# O programa começa aqui!
##########################


# recuperar toos os parâmetros passados
tam_cache = input('\nInsira o tamanho da memoria cache a ser utilizada:')
tam_cache = int(tam_cache)
tipo_mapeamento = input('\nInsira o tipo de maepamento da memoria cache a ser utilizado( DI=Direto, AS = Associativo, AC = Associativo por Conjunto):')
arquivo_leituras = input('\nInsira o nome e endereço do arquivo de leitura a ser acessado (ex: C:/Users/exemplo.txt):')
num_conjuntos = input('\nInsira o numero de conjuntos a ser utilizado:')
num_conjuntos = int(num_conjuntos)
politica_substituicao  = input('\nInsira o tipo de algoritmo de substiruição da memoria cache a ser utilizado( FIFO, RANDOM, LFU, LRU ou ALL= Todos os mapeamentos possiveis:')


if num_conjuntos <= 0:
  print('\n\n------------------------------')
  print('ERRO: O número de conjuntos não pode ser 0.')
  print('------------------------------')
  exit()


if arquivo_leituras == '':
  print('\n\n------------------------------')
  print('ERRO: É necesário informar o nome do arquivo que será processado, o parâmetro esperado é --arquivo_leituras seguido do nome do arquivo.')
  print('------------------------------')
  exit()

# lê o arquivo e armazena cada uma das posições de memória que será lida em uma lista
try:
  f = open(arquivo_leituras, "r")
  posicoes_acesso_memoria = []
  for posicao_memoria in f:
    posicoes_acesso_memoria.append(int(re.sub(r"\r?\n?$", "", posicao_memoria, 1)))
  f.close()
except IOError as identifier:
  print('\n\n------------------------------')
  print('ERRO: Arquivo \'{}\'não encontrado.'.format(arquivo_leituras))
  print('------------------------------')
  exit()

if len(posicoes_acesso_memoria) == 0:
    print('\n\n------------------------------')
    print('ERRO: o arquivo {} não possui nenhuma linha com números inteiros.'.format(arquivo_leituras))
    print('------------------------------')
    exit()

print('+====================+')
print('| SIMULADOR DE CACHE |')
print('+====================+')
print('+ Setando parâmetros iniciais da cache+')


if tipo_mapeamento != 'DI':
  if politica_substituicao != 'RANDOM' and politica_substituicao != 'FIFO' and politica_substituicao != 'LRU' and politica_substituicao != 'LFU' and politica_substituicao != 'ALL':
    print('\n\n------------------------------')
    print('ERRO: A política de substituição {} não existe.'.format(politica_substituicao))
    print('------------------------------')
    exit()

# se o tipo do mapeamento for direto DI
if tipo_mapeamento == 'DI':
  executar_mapeamento_direto(tam_cache, posicoes_acesso_memoria)
elif tipo_mapeamento == 'AS':
  if (politica_substituicao == 'ALL'):
    executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, 'RANDOM')
    executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, 'FIFO')
    executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, 'LRU')
    executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, 'LFU')
  else:
    executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, politica_substituicao)

elif tipo_mapeamento == 'AC':
  # o número de conjuntos deve ser um divisor do total da memória
  if tam_cache%num_conjuntos != 0:
    print('\n\n------------------------------')
    print('ERRO: O número de conjuntos {} deve ser obrigatoriamente um divisor do total de memória cache disponível {}.'.format(num_conjuntos, tam_cache))
    print('------------------------------')
    exit()

  if (politica_substituicao == 'ALL'):
    executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, 'RANDOM')
    executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, 'FIFO')
    executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, 'LRU')
    executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, 'LFU')
  else:
    executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, politica_substituicao)
else:
  print('\n\n------------------------------')
  print('ERRO: O tipo de mapeamento \'{}\'não foi encontrado. \nOs valores possíveis para o parâmetro --tipo_mapeamento são: DI / AS / AC'.format(tipo_mapeamento))
  print('------------------------------')
  exit()


print('\n')
print('-'*60)
print('Parâmetros da Simulação')
print('-'*60)
print('Número de posições de memória: {}'.format(len(posicoes_acesso_memoria)))
print('As posições são: {}'.format(posicoes_acesso_memoria))
print('Tamanho da memoria cache: {}'.format(tam_cache))
print("Tipo Mapeamento: {}".format(tipo_mapeamento))
if tipo_mapeamento != 'AS':
    print("Quantidade de Conjuntos: {}".format(num_conjuntos))
print("Algoritmos de Substituição: {}".format(politica_substituicao))
print('-'*60)


