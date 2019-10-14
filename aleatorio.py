import functions
import random 

def politica_substituicao_RANDOM(memoria_cache, num_conjuntos, posicao_memoria):
  """Nessa politica de substituição, cada vez que ocorre um evento de cache miss,
  será sorteado um elemento do conjunto para ser substituído.
  """
  num_conjunto = functions.get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)

  lista_posicoes = functions.get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, num_conjuntos)

  # faz a escolha aleatória de uma das posições de memória que fazem parte do conjunto
  posicao_troca_memoria = random.choice(lista_posicoes)


  print('Posição de memória cache que será trocada é: {}'.format(posicao_troca_memoria))

  memoria_cache[posicao_troca_memoria] = posicao_memoria
