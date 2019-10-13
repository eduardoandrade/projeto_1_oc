import functions

def executar_mapeamento_direto(tam_cache, posicoes_acesso_memoria):
  """Executa a operação de mapeamento direto.

  Arguments:
    tam_cache {int} -- tamanho total de palavras da cache
    posicoes_acesso_memoria {list} - quais são as posições de memória que devem ser acessadas
  """
  # zera tota a memória cache
  memoria_cache = functions.inicializar_cache(tam_cache)

  print('Situação Inicial da Memória Cache')
  functions.print_memoria_cache(memoria_cache,0)

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
    functions.print_memoria_cache(memoria_cache,0)


    print('Poisição de Memória: {} \nPosição Mapeada na Cache: {}'.format(posicao_memoria, posicao_cache))

  print('\n\n------------------------')
  print('Resumo Mapeamento Direto')
  print('------------------------')
  print('Total de memórias acessadas: {}'.format(len(posicoes_acesso_memoria)))
  print('Total HIT: {}'.format(num_hit))
  print('Total MISS: {}'.format(num_miss))
  taxa_cache_hit = (num_hit / len(posicoes_acesso_memoria))*100
  print('Taxa de Cache HIT: {number:.{digits}f}%'.format(number=taxa_cache_hit, digits=2))
