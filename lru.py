import functions

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
