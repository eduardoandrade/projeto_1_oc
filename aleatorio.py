import functions

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
