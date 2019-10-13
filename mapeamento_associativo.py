import mapeamento_associativo_conjunto as mac

def executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, politica_substituicao):
  """O mapeamento associativo é um tipo de mapeamento associativo por conjunto
  ou o número de conjunto é igual a 1

  Arguments:
    tam_cache {int} -- tamanho total de palavras da cache
    posicoes_acesso_memoria {list} - quais são as posições de memória que devem ser acessadas
    politica_substituicao {str} -- qual será a política de subistituição
  """
  # o número 1 indica que haverá apenas um único conjunto no modo associativo por conjunto
  # que é igual ao modo associativo padrão! :) SHAZAM
  mac.executar_mapeamento_associativo_conjunto(tam_cache, 1, posicoes_acesso_memoria, politica_substituicao)
