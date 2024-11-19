'''
1) Listagem das manifestações
2) Criar uma nova manifestação
3) Exibir quantidade de manifestações
4) Pesquisar uma manifestação por codigo
5) Excluir uma manifestação
6) Sair do sistema
'''
from operacoesbd import *
opcao = 1

conexao = criarConexao('127.0.0.1', 'root','root','ouvidoriaBD')

while opcao != 7:
    print("\nSeja bem vindo a ouvidoria da Universidade XYZ \nOpções:")
    print("1) Listagem das manifestações \n2) Buscar por tipo \n3) Criar uma nova manifestação \n4) Exibir quantidade de manifestações \n5) Pesquisar uma manifestação por codigo \n6) Excluir uma manifestação \n7) Sair do sistema \n")
    opcao = int(input("Digite a opção escolhida:"))

    if opcao == 1: #Listar
        manifestacaoListar = listarBancoDados(conexao, "select * from manifestacoes")

        if len(manifestacaoListar) > 0:
            for index in manifestacaoListar:
                print(index[0], "-", index[1], "-", index[2], "-", index[3])

        else:
            print("Nenhuma manifestação disponível")

    elif opcao == 2: #Buscar pelo tipo
        tipo = int(
            input("Selecione o tipo da manifestação a ser pesquisada \n1) Reclamação \n2) Sugestão \n3) Feedback\n"))

        if tipo > 0 and tipo <= 3:

            if tipo == 1:
                consultaListagemTipo = 'select * from manifestacoes where tipo like "recla%"'
                manifestacoes = listarBancoDados(conexao, consultaListagemTipo)
                for index in manifestacoes:
                    print(index[0], "-", index[1], "-", index[2], "-", index[3])

            elif tipo == 2:
                consultaListagemTipo = 'select * from manifestacoes where tipo like "suge%"'
                manifestacoes = listarBancoDados(conexao, consultaListagemTipo)
                for index in manifestacoes:
                    print(index[0], "-", index[1], "-", index[2], "-", index[3])

            elif tipo == 3:
                consultaListagemTipo = 'select * from manifestacoes where tipo like "feed%"'
                manifestacoes = listarBancoDados(conexao, consultaListagemTipo)
                for index in manifestacoes:
                    print(index[0], "-", index[1], "-", index[2], "-", index[3])

        else:
            print("Opção indisponivel")

    elif opcao == 3: #Criar
        perguntaNome = input("Digite seu nome: ")
        perguntaManifestacao = input("Digite sua manifestacao: ")
        perguntaTipo = input("Qual o tipo da sua manifestação: ")

        manifestacaoInserir = "insert into manifestacoes (nome,manifestacao,tipo) values (%s,%s,%s);"
        valores = [perguntaNome, perguntaManifestacao, perguntaTipo]
        insertNoBancoDados(conexao, manifestacaoInserir, valores)

        print('Manifestacao adicionada com sucesso!')

    elif opcao == 4:  #Quantidade
        consultaManifestacoes = 'select count(*) from manifestacoes'
        manifestacoes = listarBancoDados(conexao, consultaManifestacoes)
        quantidadeManifestacao = manifestacoes[0][0]

        if len(manifestacoes) > 0:
            print(quantidadeManifestacao, "manifestações disponiveis")

        else:
            print('Nenhuma manifestação disponivel')


    elif opcao == 5: #Buscar
        codigoBuscar = int(input('Digite o codigo da manifestacao:'))

        consultaListagem = 'select * from manifestacoes where codigo = %s'
        valores = [codigoBuscar]
        manifestacoes = listarBancoDados(conexao, consultaListagem, valores)

        if len(manifestacoes) > 0:
            for index in manifestacoes:
                print(index[0], "-", index[1], "-", index[2], "-", index[3])
        else:
            print('Não tem manifestacoes disponiveis')

    elif opcao == 6: #Excluir
        codigoRemover = int(input('Digite o codigo pra remover: '))

        excluir = 'delete from manifestacoes where codigo = %s'
        valores = [codigoRemover]
        linhhasAfetadas = excluirBancoDados(conexao, excluir, valores)

        if linhhasAfetadas > 0:
            print('Manifestacao removida com sucesso!')
        else:
            print("Não tem manifestações disponiveis com o codigo informado!")

    elif opcao == 7:
        print("Saindo do sistema!")

    else:
        print("Opção invalida.")

encerrarConexao(conexao)