import functions
import random

def politica_substituicao_LFU(memoria_cache, num_conjuntos, posicao_memoria,contador_lfu):
  """Nessa politica de substituicao, o elemento menos acessado e removido. 
  A cada cache hit a posicao e incrementada, isso e usado para saber qual a proxima posicao deve ser removida
  """
  num_conjunto = functions.get_num_conjunto_posicao_memoria(posicao_memoria, num_conjuntos)
  lista_posicoes = functions.get_lista_posicoes_cache_conjunto(memoria_cache,num_conjunto, num_conjuntos)

  # descobre qual posicao da cache tem menos acesso
  posicao_substituir = 0
  if len(lista_posicoes) > 1:


    functions.imprimir_contador_lfu(contador_lfu)

    # descobre qual das posicoes e menos usada
    lista_qtd_acessos = []
    for qtd_acessos in lista_posicoes:
      lista_qtd_acessos.append(contador_lfu[qtd_acessos])

    posicoes_com_menos_acesso = min(lista_qtd_acessos)
    candidatos_lfu = []

    for qtd_acessos in lista_posicoes:
      if contador_lfu[qtd_acessos] == posicoes_com_menos_acesso:
        candidatos_lfu.append(qtd_acessos)

    # escolhe aleatoriamente uma posicao dentre as que possuem menor numero de acessos
    posicao_substituir = random.choice(candidatos_lfu)

  # zera o numero de acessos da posicao que foi substituida
  contador_lfu[posicao_substituir] = 0

  # altera a posicao de memoria na cache
  memoria_cache[posicao_substituir] = posicao_memoria
  
  return contador_lfu

  print('Posição Memória Lida No Arquivo: {}'.format(posicao_memoria))
  print('Conjunto: {}'.format(num_conjunto))
  print('Número de Acesso Da Posição com Menos Acesso: {}'.format(posicoes_com_menos_acesso))
  print('Lista Posições do  conjunto: {}'.format(lista_posicoes))
  print('Lista com as posições menos acessadas do conjunto: {}'.format(candidatos_lfu))
  print('Posição Cache Substituir: {}'.format(posicao_substituir))
  print('Posição de memória cache que será trocada é: {}'.format(posicao_substituir))
