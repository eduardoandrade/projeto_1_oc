def existe_posicao_vazia(memoria_cache, num_conjuntos, posicao_memoria):
  """Verifica se existe na memoria cache uma posicao de memoria que ainda nao foi utilizada
  """
  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache, num_conjunto, num_conjuntos)

  # verifica se alguma  está vazia
  for x in lista_posicoes:
    if memoria_cache[x] == -1:
      return x
  return -1


def get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos):
  """Retorna o numero do conjunto onde essa posicao de memoria esta mapeada
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
  """Cria um dicionario para representar a  memoria cache zerada, onde cada posicao recebe o
  valor padrao igual a '-1'
  """
  # cria a memoria cache
  memoria_cache = {}

  # insere cada posicao da memória cache com o valor -1, indicando que a posicao nao foi usada
  for x in range(0, tam_cache):
    memoria_cache[x] = -1

  return memoria_cache

def verifica_posicao_em_cache_associativo_conjunto(memoria_cache, num_conjuntos, posicao_memoria,):
  """Verifica se uma determinada posicao de memoria esta na cache
    no modo associativo / associativo por conjunto
  """
  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)

  while num_conjunto < len(memoria_cache):
    if memoria_cache[num_conjunto] == posicao_memoria:
      return num_conjunto

    num_conjunto += num_conjuntos

  # caso nao achou tenha achacdo a posicao da memoria na cache
  return -1

def get_lista_posicoes_cache_conjunto(memoria_cache, num_conjunto, num_conjuntos):
  """Retorna uma lista com todas as posicoes da memoria cache que fazem
  parte do conjunto.
  """
  lista_posicoes = []
  posicao_inicial = num_conjunto
  while posicao_inicial < len(memoria_cache):
    lista_posicoes.append(posicao_inicial)
    posicao_inicial += num_conjuntos
  return lista_posicoes
