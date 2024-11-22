from operacoesbd import *

def listarManifestacao(conexao):
    manifestacaoListar = listarBancoDados(conexao, "select * from manifestacoes")

    if len(manifestacaoListar) > 0: #Se a quantidade de manifestaçoes for maior que 0
        for index in manifestacaoListar:
            print(index[0], "-", index[1], "-", index[2], "-", index[3])

    else:
        print("Nenhuma manifestação disponível")

def pesquisarTipo (conexao,tipo): #Metodo para pesquisar por tipo
    if tipo > 0 and tipo <= 3: #Limitar se o tipo está dentro do intervalo válido

        if tipo == 1:
            consultaListagemTipo = 'select * from manifestacoes where tipo like "Recla%"' #puxar no banco de dados determinada manifestacao pelo tipo selecionado
            manifestacoes = listarBancoDados(conexao, consultaListagemTipo)
            quantidadeTipo = 'select count(tipo) from manifestacoes where tipo like "Recla%"' #conferir a quantidade de manifestacao por tipo
            if len(quantidadeTipo) > 0:
                for index in manifestacoes:
                    print(index[0], "-", index[1], "-", index[2], "-", index[3])
            else:
                print("Não tem nenhuma manifestaçao disponivel pelo tipo informado")

        elif tipo == 2:
            consultaListagemTipo = 'select * from manifestacoes where tipo like "Suge%"' #puxar no banco de dados determinada manifestacao pelo tipo selecionado
            manifestacoes = listarBancoDados(conexao, consultaListagemTipo)
            quantidadeTipo = 'select count(tipo) from manifestacoes where tipo like "Suge%"' #conferir a quantidade de manifestacao por tipo
            if len(quantidadeTipo) > 0:
                for index in manifestacoes:
                    print(index[0], "-", index[1], "-", index[2], "-", index[3])
                print("Não tem nenhuma manifestaçao disponivel pelo tipo informado")
            else:
                print("Não tem nenhuma manifestaçao disponivel pelo tipo informado")

        elif tipo == 3:
            consultaListagemTipo = 'select * from manifestacoes where tipo like "Feed%"' #puxar no banco de dados determinada manifestacao pelo tipo selecionado
            manifestacoes = listarBancoDados(conexao, consultaListagemTipo)
            quantidadeTipo = 'select count(tipo) from manifestacoes where tipo like "Feed%"' #conferir a quantidade de manifestacao por tipo
            if len(quantidadeTipo) > 0:
                for index in manifestacoes:
                    print(index[0], "-", index[1], "-", index[2], "-", index[3])
            else:
                print("Não tem nenhuma manifestaçao disponivel pelo tipo informado")

    else:
        print("Opção indisponivel")

def adidicionarManifestacao(conexao,perguntaNome,perguntaManifestacao,perguntaTipo,):

    if perguntaTipo > 0 and perguntaTipo <=3:  #Limitar se o Perguntatipo está dentro do intervalo válido
        if perguntaTipo == 1:
            manifestacaoInserir = "insert into manifestacoes (nome,manifestacao,tipo) values (%s,%s,%s);"
            valores = [perguntaNome, perguntaManifestacao, "Reclamação"] #completa o tipo da manifestacao com a opcao selecionada
            insertNoBancoDados(conexao, manifestacaoInserir, valores)
        elif perguntaTipo == 2:
            manifestacaoInserir = "insert into manifestacoes (nome,manifestacao,tipo) values (%s,%s,%s);"
            valores = [perguntaNome, perguntaManifestacao, "Sugestaçao"] #completa o tipo da manifestacao com a opcao selecionada
            insertNoBancoDados(conexao, manifestacaoInserir, valores)
        elif perguntaTipo == 3:
            manifestacaoInserir = "insert into manifestacoes (nome,manifestacao,tipo) values (%s,%s,%s);"
            valores = [perguntaNome, perguntaManifestacao, "Feedback"] #completa o tipo da manifestacao com a opcao selecionada
            insertNoBancoDados(conexao, manifestacaoInserir, valores)
    else:
        print("Opçao Invalido")


    print('Manifestacao adicionada com sucesso!')

def quantidadeManifestacoes(conexao):
    consultaManifestacoes = 'select count(*) from manifestacoes'
    qntManif = listarBancoDados(conexao, consultaManifestacoes)

    for b in qntManif:
        if b[0] == 0:
            print("Nenhuma manifestação registrada no sistema.")
        elif b[0] == 1: #Caso tenha apenas uma manifestaçao
            print("Apenas uma manifestação registrada no sistema.")
        elif b[0] > 1: #Caso tenham varias manifestaçoes
            print(f"{b[0]} manifestações registradas no sistema.")

def buscarManifestacao(conexao,codigoPesquisado):
        consultaListagem = 'select * from manifestacoes where codigo = %s'
        valores = [codigoPesquisado]
        manifestacoes = listarBancoDados(conexao, consultaListagem, valores)

        if len(manifestacoes) > 0:
            for index in manifestacoes:
                print(index[0], "-", index[1], "-", index[2], "-", index[3])
        else:
            print('Não tem manifestacoes disponiveis')


def removerManifestacao(conexao,codigoRemover):

        excluir = 'delete from manifestacoes where codigo = %s'
        valores = [codigoRemover]
        linhhasAfetadas = excluirBancoDados(conexao, excluir, valores)

        if linhhasAfetadas > 0:
            print('Manifestacao removida com sucesso!')
        else:
            print("Não tem manifestações disponiveis com o codigo informado!")
