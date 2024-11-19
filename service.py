from operacoesbd import *

def listarManifestacao(conexao):
    manifestacaoListar = listarBancoDados(conexao, "select * from manifestacoes")

    if len(manifestacaoListar) > 0:
        for index in manifestacaoListar:
            print(index[0], "-", index[1], "-", index[2], "-", index[3])

    else:
        print("Nenhuma manifestação disponível")