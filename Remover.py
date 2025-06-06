from operacoesbd import *

codigo = input("Digite o código da manifestação a ser removida: ")
consulta = 'delete from manifestacoes where codigo_manifestacao = %s'
dados = [codigo]
linhasAfetadas = excluirBancoDados(conexão, consulta, dados)
if linhasAfetadas == 0:
     print("Não existe Manifestações para o código informado.")
else:
    print("Manifestação removida com sucesso!!!")