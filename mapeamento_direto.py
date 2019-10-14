import functions

def executar_mapeamento_direto(tam_cache, posicoes_acesso_memoria):
  """Executa a operacao de mapeamento direto.
  """
  # zera tota a memoria cache
  memoria_cache = functions.inicializar_cache(tam_cache)

  print('Situação Inicial da Memoria Cache')
  functions.print_memoria_cache(memoria_cache,0)

  hmstatus = ''
  num_hit = 0;
  num_miss = 0
  for index, posicao_memoria in enumerate(posicoes_acesso_memoria):
    # no mapeamento direto, cada posição da memoria principal tem uma posição
    # especifica na memoria cache
    posicao_cache = posicao_memoria % tam_cache

    # contador de hits ou misses
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
