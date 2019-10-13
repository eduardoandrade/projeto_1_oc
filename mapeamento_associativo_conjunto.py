import functions
import fifo
import lru
import lfu
import aleatorio

def executar_mapeamento_associativo_conjunto(tam_cache, num_conjuntos, posicoes_acesso_memoria, politica_substituicao='RANDOM'):
  """Executa a operação de mapeamento associativo, ou seja, não existe uma posição específica
  para o mapemento de uma posição de memória.

  Arguments:
    tam_cache {int} -- tamanho total de palavras da cache
    num_conjuntos {int} -- quantidade de conjuntos na cache
    posicoes_acesso_memoria {list} -- quais são as posições de memória que devem ser acessadas
    politica_substituicao {str} -- Qual é a política para substituição caso a posição de memória desejada não esteja na cache E não exista espaço vazio
  """

  memoria_cache = functions.inicializar_cache(tam_cache)

  # se o número de conjuntos for igual a zero, então estamos simulando
  # com a cache associativo!
  nome_mapeamento = 'Associativo'
  if num_conjuntos == 1:
    functions.print_memoria_cache(memoria_cache,1)
  else:
    nome_mapeamento = 'Associativo Por Conjunto'
    functions.print_memoria_cache(memoria_cache, num_conjuntos)

  num_hit = 0
  num_miss = 0

  # se a política for fifo então inicializa a lista de controle
  if politica_substituicao == 'FIFO':
    functions.inicializar_contador_fifo()

  # se a política for fifo então inicializa a lista de controle
  if politica_substituicao == 'LFU':
    functions.inicializar_contador_lfu()

  # percorre cada uma das posições de memória que estavam no arquivo
  for index, posicao_memoria in enumerate(posicoes_acesso_memoria):
    print('\n\n\nInteração número: {}'.format(index+1))
    # verificar se existe ou não a posição de memória desejada na cache
    inserir_memoria_na_posicao_cache = functions.verifica_posicao_em_cache_associativo_conjunto(memoria_cache, num_conjuntos, posicao_memoria)

    # a posição desejada já está na memória
    if inserir_memoria_na_posicao_cache >= 0:
      num_hit += 1
      print('Cache HIT: posiçao de memória {}, posição cache {}'.format(posicao_memoria, inserir_memoria_na_posicao_cache))

      # se for LFU então toda vez que der um HIT será incrementado o contador daquela posição
      if politica_substituicao == 'LFU':
        contador_lfu[inserir_memoria_na_posicao_cache] += 1
        functions.imprimir_contador_lfu()

      # se for LRU então toda vez que der um HIT será incrementado o contador daquela posição
      if politica_substituicao == 'LRU':
        lru.politica_substituicao_LRU(memoria_cache, num_conjuntos, posicao_memoria, inserir_memoria_na_posicao_cache,1)

    else:
      num_miss += 1
      print('Cache MISS: posiçao de memória {}'.format(posicao_memoria))

      # verifica se existe uma posição vazia na cache, se sim aloca nela a posição de memória
      posicao_vazia = functions.existe_posicao_vazia(memoria_cache, num_conjuntos, posicao_memoria)


      print('Posição da cache ainda não utilizada: {}'.format(posicao_vazia))
      print('\nLeitura linha {}, posição de memória {}.'.format(index,posicao_memoria))

      ########
      # se posicao_vazia for < 0 então devemos executar as políticas de substituição
      ########
      if posicao_vazia >= 0:
        memoria_cache[posicao_vazia] = posicao_memoria
      elif politica_substituicao == 'RANDOM':
        aleatorio.politica_substituicao_RANDOM(memoria_cache,num_conjuntos,posicao_memoria)
      elif politica_substituicao == 'FIFO':
        fifo.politica_substituicao_FIFO(memoria_cache,num_conjuntos,posicao_memoria)
      elif politica_substituicao == 'LFU':
        lfu.politica_substituicao_LFU(memoria_cache,num_conjuntos,posicao_memoria)
      elif politica_substituicao == 'LRU':
        lru.politica_substituicao_LRU(memoria_cache,num_conjuntos,posicao_memoria,0,0)


    if num_conjuntos == 1:
      functions.print_memoria_cache(memoria_cache,1)
    else:
      functions.print_memoria_cache(memoria_cache, num_conjuntos)



  # se for LFU e com debug imprimir os dados computador no contador LFU
  if politica_substituicao == 'LFU':
    functions.imprimir_contador_lfu()

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
