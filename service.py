from operacoesbd import *

def listarManifestacao(conexao):
    manifestacaoListar = listarBancoDados(conexao, "select * from manifestacoes")

    if len(manifestacaoListar) > 0:
        for index in manifestacaoListar:
            print(index[0], "-", index[1], "-", index[2], "-", index[3])

    else:
        print("Nenhuma manifestação disponível")

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
