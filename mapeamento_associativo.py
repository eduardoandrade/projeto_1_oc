import mapeamento_associativo_conjunto as mac

def executar_mapeamento_associativo(tam_cache, posicoes_acesso_memoria, politica_substituicao):
  """O mapeamento associativo e o caso do mapeamento associativo por conjunto
  onde o número de conjunto é igual a 1
  """
  mac.executar_mapeamento_associativo_conjunto(tam_cache, 1, posicoes_acesso_memoria, politica_substituicao)
