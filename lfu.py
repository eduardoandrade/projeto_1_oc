import functions

def politica_substituicao_LFU(memoria_cache, num_conjuntos, posicao_memoria):
  """Nessa politica de substituição, o elemento que é menos acessado é removido da
  memória cache quando ocorrer um CACHE MISS. A cada CACHE HIT a posição do HIT ganha um ponto
  de acesso, isso é usado como contador para saber qual posição deve ser removida no caso de
  CACHE MISS.

  Arguments:
    memoria_cache {list} -- memóiria cache
    num_conjuntos {int} -- quantidade de conjuntos
    posicao_memoria {int} -- posição de memória que será acessada
  """
  num_conjunto = get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)
  lista_posicoes = get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, num_conjuntos)

  # descobrir dentro do conjunto qual posição da cache tem menos acesso
  posicao_substituir = 0
  if len(lista_posicoes) > 1:


    imprimir_contador_lfu()

    # descobrir qual das posições é menos usada
    lista_qtd_acessos = []
    for qtd_acessos in lista_posicoes:
      lista_qtd_acessos.append(contador_lfu[qtd_acessos])

    posicoes_com_menos_acesso = min(lista_qtd_acessos)
    candidatos_lfu = []

    for qtd_acessos in lista_posicoes:
      if contador_lfu[qtd_acessos] == posicoes_com_menos_acesso:
        candidatos_lfu.append(qtd_acessos)

    # para garantir ordem aleatória de escolha caso duas ou mais posições
    # tenham o mesmo número de acessos
    posicao_substituir = random.choice(candidatos_lfu)

  # zera o número de acessos a posição que foi substituida
  contador_lfu[posicao_substituir] = 0

  # altera a posição de memória que está na cache
  memoria_cache[posicao_substituir] = posicao_memoria

  print('Posição Memória Lida No Arquivo: {}'.format(posicao_memoria))
  print('Conjunto: {}'.format(num_conjunto))
  print('Número de Acesso Da Posição com Menos Acesso: {}'.format(posicoes_com_menos_acesso))
  print('Lista Posições do  conjunto: {}'.format(lista_posicoes))
  print('Lista com as posições menos acessadas do conjunto: {}'.format(candidatos_lfu))
  print('Posição Cache Substituir: {}'.format(posicao_substituir))
  print('Posição de memória cache que será trocada é: {}'.format(posicao_substituir))
