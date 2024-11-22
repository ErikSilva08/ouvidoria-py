from operacoesbd import *

def listarManifestacao(conexao):
    manifestacaoListar = listarBancoDados(conexao, "select * from manifestacoes")

    if len(manifestacaoListar) > 0: #Se a quantidade de manifestaçoes for maior que 0
        for index in manifestacaoListar:
            print(index[0], "-", index[1], "-", index[2], "-", index[3])

    else:
        print("Nenhuma manifestação disponível")

def pesquisarTipo (conexao,tipo):
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

def adidicionarManifestacao(conexao,perguntaNome,perguntaManifestacao,perguntaTipo):
    manifestacaoInserir = "insert into manifestacoes (nome,manifestacao,tipo) values (%s,%s,%s);"
    valores = [perguntaNome, perguntaManifestacao, perguntaTipo]
    insertNoBancoDados(conexao, manifestacaoInserir, valores)
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
