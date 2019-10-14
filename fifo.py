import functions

def politica_substituicao_FIFO(memoria_cache, num_conjuntos, posicao_memoria):
  """Nessa politica de substituição, o primeiro elemento que entra é o primeiro elemento que sai
  """
  num_conjunto = functions.get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)
  posicao_substituir = contador_fifo[num_conjunto]
  lista_posicoes = functions.get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, num_conjuntos)

  functions.imprimir_contador_fifo()
  print('Posição Memória: {}'.format(posicao_memoria))
  print('Conjunto: {}'.format(num_conjunto))
  print('Lista posições: {}'.format(lista_posicoes))
  print('Posição para subistituição: {}'.format(posicao_substituir))
  # realiza a subtituição do elemento mais antigo pelo mais recente
  memoria_cache[lista_posicoes[posicao_substituir]] = posicao_memoria
  #atualiza o contador fifo
  contador_fifo[num_conjunto] += 1
  # caso o número indicando o proximo endereço exceda o tamanho do conjunto retorne ao primero elemento
  if contador_fifo[num_conjunto] >= (len(memoria_cache)/num_conjuntos):
    contador_fifo[num_conjunto] = 0


  print('Posição de memória cache que será trocada é: {}'.format(lista_posicoes[posicao_substituir]))
