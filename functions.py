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

  print("/------------------------------\ ")
  if num_conjuntos ==0:
        print("|        Cache Direto          |")
  elif  num_conjuntos ==1:
        print("|       Cache Associativo      |")
  else:
        print("|  Cache Associativo Conjunto  |")
  print("|------------------------------|")
  if num_conjuntos >1:
        print("|Tamanho: {:>21}|\n|Conjuntos: {:>19}|".format(len(memoria_cache), num_conjuntos))
  else:
        print("|Tamanho cache: {:>15}| ".format(len(memoria_cache)))
  print("|------------------------------|")
  if num_conjuntos <=1:
        print("| Pos cache   | Posição Memória|")
        print("|-------------|----------------|")
        for posicao, valor in memoria_cache.items():
            print("|{:>13}|{:>16}|".format(posicao, valor))
        print("|-------------|----------------|")
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
