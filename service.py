from operacoesbd import *

def listarManifestacao(conexao):
    manifestacaoListar = listarBancoDados(conexao, "select * from manifestacoes")

    if len(manifestacaoListar) > 0:
        for index in manifestacaoListar:
            print(index[0], "-", index[1], "-", index[2], "-", index[3])

    else:
        print("Nenhuma manifestação disponível")

def pesquisarTipo (conexao):
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

def adidicionarManifestacao(conexao):
    perguntaNome = input("Digite seu nome: ")
    perguntaManifestacao = input("Digite sua manifestacao: ")
    perguntaTipo = input("Qual o tipo da sua manifestação: ")

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
        elif b[0] == 1:
            print("Apenas uma manifestação registrada no sistema.")
        elif b[0] > 1:
            print(f"{b[0]} manifestações registradas no sistema.")

def buscarManifestacao(conexao):
    qntManif = listarBancoDados(conexao, "select count(codigo) from manifestacoes")
    for count in qntManif:
        if count[0] == 0:
            print("Nenhuma manifestação registrada no sistema. ")
        else:
            resultado = -1

            while resultado < 1:
                listarManifestacao(conexao)
                consulta = f"select * from manifestacoes WHERE codigo = {codigoPesquisado} "
                buscaCodigo = listarBancoDados(conexao, consulta)
                resultado = len(buscaCodigo)

                if resultado < 1:
                    print("Nenhuma manifestação disponível com o código informado. Digite um código válido")

                else:
                    for c in buscaCodigo:
                        print(f"{c[1]} - {c[2]} - {c[3]}")
                        break

def removerManifestacao(conexao):
    qntManif = listarBancoDados(conexao, "select count(codigo) from manifestacoes")
    for count in qntManif:
        if count[0] == 0:
            print("Nenhuma manifestação registrada no sistema. ")
        else:
            manifRemovid = -1

            while manifRemovid < 1:
                listarManifestacao(conexao)

                consulta = "DELETE FROM manifestacoes where codigo = %s"
                valores = [removerManif]
                manifRemovid = excluirBancoDados(conexao, consulta, valores)

                if manifRemovid < 1:
                    print("ERRO! Nenhuma manifestação registrada com o código informado.")
                else:
                    print("Manifestação removida com sucesso. ")
                    break
