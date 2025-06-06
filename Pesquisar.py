from operacoesbd import *

codigo = input("Digite o código da manifestação ser pesquisado: ")
consulta = 'select * from manifestacoes where codigo_manifestacao = %s'
dados = [codigo]
manifestacoes = listarBancoDados(conexão,consulta,dados)
if len(manifestacoes) == 0:
    print("Não existe manifestações para o código informado.")
else:
    print("Manifestação encontrada")
    print("-Titulo da manifestação:",manifestacoes[0][1],",Descrição:",manifestacoes[0][2],",Autor:",manifestacoes[0][3],",Tipo:",manifestacoes[0][4])
