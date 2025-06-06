from operacoesbd import *
from Metodos import  *
conexão = criarConexao('127.0.0.1','root','12345','manifestacoes')

opcao = 1
filmes = [ ]
while opcao !=7:
    print("\n1) Listagem das Manifestações, 2) Listagem de Manifestações por Tipo, 3) Criar uma nova Manifestação, 4) Exibir quantidade de manifestações, 5) Pesquisar uma manifestação por código, 6) Excluir uma Manifestação pelo Código, 7) Sair do Sistema. ")
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        ListarManifestacoes(conexão)

    elif opcao == 2:
        ListarPorTipo(conexão)

    elif opcao == 3:
        AdicionarManifestacoes(conexão)

    elif opcao == 4:
        Quantidademanifestações(conexão)

    elif opcao == 5:
        PesquisarManifestacao(conexão)

    elif opcao == 6:
        RemoverManifestacao(conexão)

    elif opcao  != 7:
        print("opção invalida")
print("Obrigado por acessar as manifestações")
encerrarConexao(conexão)