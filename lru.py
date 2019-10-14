import functions

def politica_substituicao_LRU(memoria_cache, num_conjuntos, posicao_memoria, posicao_cache_hit, flag_hit):
  """Nessa politica de substituicao quando ocorre um cache hit a posicao vai para o fim da fila,
  se ocorrer um cache miss remove o elemento 0 e a posição da cache onde a memória foi alocada e
  colocada no fim da fila
  """

  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, num_conjuntos)



  if flag_hit ==0: # copia os valores de cada posicao da cache uma posição para traz em caso de miss
      for posicao_cache in lista_posicoes:
        proxima_posicao = posicao_cache+num_conjuntos
        if proxima_posicao < len(memoria_cache):
          memoria_cache[posicao_cache] = memoria_cache[proxima_posicao]
  if flag_hit ==1:  # copia os valores de cada posicao da cache uma posição para traz em caso de hit
      for posicao_cache in lista_posicoes:
        if posicao_cache_hit <= posicao_cache:
          proxima_posicao = posicao_cache+num_conjuntos
          if proxima_posicao < len(memoria_cache):
            memoria_cache[posicao_cache] = memoria_cache[proxima_posicao]
  # coloca a posição que acabou de ser lida na topo da lista, assim, ela nesse momento e a ultima que sera removida
  memoria_cache[lista_posicoes[-1]] = posicao_memoria


  print('Posição Memória: {}'.format(posicao_memoria))
  print('Conjunto: {}'.format(num_conjunto))
  print('Lista posições: {}'.format(lista_posicoes))
