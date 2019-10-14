import functions
import fifo
import lru
import lfu
import aleatorio

def inicializar_contador_fifo(num_conjuntos):
  """Preenche o contador fifo para que a primeira subsitituicao
  ocorra no primeiro elemento do conjunto
  """
  # cria no contador fifo uma posicao para cada conjunto e preenche com a primeira posicao
  for x in range(0, num_conjuntos):
    contador_fifo[x] = 0


  functions.imprimir_contador_fifo(contador_fifo)

def inicializar_contador_lfu(tam_cache):
  """Preenche o contador LFU para cada posicao da cache. Todas as posicao comecam zeradas e a cada
  cache hit a posicao e incrementada, a posicao e zerada quando for substituida
  """
  # cria on contador LFU uma posicao para cada posicao de memoria
  for x in range(0, tam_cache):
    contador_lfu[x] = 0


  functions.imprimir_contador_lfu(contador_lfu)

def executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, politica_substituicao):
  """Executa a operacaoo de mapeamento associativo por conjunto
  """

  memoria_cache = functions.inicializar_cache(tam_cache)

  # codigo para lidar com as diferencas de assiciativo e associativo por conjunto
  nome_mapeamento = 'Associativo'
  if num_conjuntos == 1:
    functions.print_memoria_cache(memoria_cache,1)
  else:
    nome_mapeamento = 'Associativo Por Conjunto'
    functions.print_memoria_cache(memoria_cache, num_conjuntos)

  num_hit = 0
  num_miss = 0

  # se a politica for FIFO entao inicializa a lista de controle
  if politica_substituicao == 'FIFO':
    inicializar_contador_fifo( num_conjuntos)

  # se a politica for LFU entao inicializa a lista de controle
  if politica_substituicao == 'LFU':
    inicializar_contador_lfu(tam_cache)

  # percorre cada uma das posicoes de memoria que estavam no arquivo
  for index, posicao_memoria in enumerate(posicoes_acesso_memoria):
    print('\n\n\nInteração número: {}'.format(index+1))
    # verificar a existencia da posicao de momoria na cache
    inserir_memoria_na_posicao_cache = functions.verifica_posicao_em_cache_associativo_conjunto(memoria_cache, num_conjuntos, posicao_memoria)

    # se a posicao desejada ja esta na memória
    if inserir_memoria_na_posicao_cache >= 0:
      num_hit += 1
      print('Cache HIT: posiçao de memória {}, posição cache {}'.format(posicao_memoria, inserir_memoria_na_posicao_cache))

      # se for LFU entao toda vez que der um HIT será incrementado o contador daquela posição
      if politica_substituicao == 'LFU':
        contador_lfu[inserir_memoria_na_posicao_cache] += 1
        functions.imprimir_contador_lfu(contador_lfu)

      # se for LRU entao toda vez que der um HIT sera incrementado o contador daquela posicao
      if politica_substituicao == 'LRU':
        lru.politica_substituicao_LRU(memoria_cache, num_conjuntos, posicao_memoria, inserir_memoria_na_posicao_cache,1)

    else:
      num_miss += 1
      print('Cache MISS: posiçao de memória {}'.format(posicao_memoria))

      # verifica se existe uma posicao vazia na cache
      posicao_vazia = functions.existe_posicao_vazia(memoria_cache, num_conjuntos, posicao_memoria)


      print('Posição da cache ainda não utilizada: {}'.format(posicao_vazia))
      print('\nLeitura linha {}, posição de memória {}.'.format(index,posicao_memoria))


      # se nao tiver posicoes vazias entao devemos executar as politicas de substituicao

      if posicao_vazia >= 0:
        memoria_cache[posicao_vazia] = posicao_memoria
      elif politica_substituicao == 'RANDOM':
        aleatorio.politica_substituicao_RANDOM(memoria_cache,num_conjuntos,posicao_memoria)
      elif politica_substituicao == 'FIFO':
        fifo.politica_substituicao_FIFO(memoria_cache,num_conjuntos,posicao_memoria,contador_fifo)
      elif politica_substituicao == 'LFU':
        lfu.politica_substituicao_LFU(memoria_cache,num_conjuntos,posicao_memoria,contador_lfu)
      elif politica_substituicao == 'LRU':
        lru.politica_substituicao_LRU(memoria_cache,num_conjuntos,posicao_memoria,0,0)


    if num_conjuntos == 1:
      functions.print_memoria_cache(memoria_cache,1)
    else:
      functions.print_memoria_cache(memoria_cache, num_conjuntos)



  if politica_substituicao == 'LFU':
    functions.imprimir_contador_lfu(contador_lfu)

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
