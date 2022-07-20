def perguntar():
    return input("O que deseja realizar ?: \n" +
          "<I> - Para inserir um usuário: \n" +
          "<P> - Para pesquisar um usuário: \n" +
          "<E> - Para excluir um usuário: \n" +
          "<L> - Para listar um usuário: ").upper()


def inserir(dicionario):
    dicionario[input("Digite seu login: ").upper()] = [input("Digite seu nome: ").upper(),
                                                     input("Digite sua data de acesso: "),
                                                     input("Digite sua estação de acesso: ")]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)