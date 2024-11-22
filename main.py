'''
1) Listagem das manifestações
2) Criar uma nova manifestação
3) Exibir quantidade de manifestações
4) Pesquisar uma manifestação por codigo
5) Excluir uma manifestação
6) Sair do sistema
'''
from operacoesbd import *
from service import *

opcao = 1

conexao = criarConexao('127.0.0.1', 'root', 'fELIPE2025!', 'ouvidoriaBD')

while opcao != 7:
    print("\nSeja bem vindo a ouvidoria da Universidade XYZ \nOpções:")
    print(
        "1) Listagem das manifestações \n2) Buscar por tipo \n3) Criar uma nova manifestação \n4) Exibir quantidade de manifestações \n5) Pesquisar uma manifestação por codigo \n6) Excluir uma manifestação \n7) Sair do sistema \n")
    opcao = int(input("Digite a opção escolhida:"))

    if opcao == 1:  # Listar

        listarManifestacao(conexao)


    elif opcao == 2:  # Buscar pelo tipo
        tipo = int(input("Selecione o tipo da manifestação a ser pesquisada \n1) Reclamação \n2) Sugestão \n3) Feedback\n"))
        pesquisarTipo(conexao,tipo)


    elif opcao == 3:  # Criar1
        perguntaNome = input("Digite seu nome: ")
        perguntaManifestacao = input("Digite sua manifestacao: ")
        perguntaTipo =  int(input("Selecione o tipo da manifestação a ser adicionada: \n1) Reclamação \n2) Sugestão \n3) Feedback\n"))
        adidicionarManifestacao(conexao, perguntaNome, perguntaManifestacao, perguntaTipo)


    elif opcao == 4:  # Quantidade

        quantidadeManifestacoes(conexao)

    elif opcao == 5:  # Buscar
        codigoPesquisado = int(input("Insira o código da manifestação: "))
        buscarManifestacao(conexao,codigoPesquisado)

    elif opcao == 6:  # Excluir
        codigoRemover = int(input("Insira o código da manifestação para removê-la: "))
        removerManifestacao(conexao, codigoRemover)

    elif opcao == 7:
        print("Saindo do sistema!")

    else:
        print("Opção invalida.")

encerrarConexao(conexao)
