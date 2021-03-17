lst_produtos = ['MOUSE', 'TECLADO']
lst_precos = [30, 70]
lst_qtds = [8, 23]

def write(string):
    return input(string).upper()

def erro():
    return input('ERRO CRITICO [ENTER - VOLTA MENU]')

def get_index(lista, string):
    if string in lista:
        return lista.index(string)

def get_prod():
    for prod in lst_produtos:
        print(prod)
    return write('Escolha um dos produtos acima: ')

def remove_prod(lists, index):
    for array in lists:
        array.pop(index)

def imprimir_um_produto():
    escolher = get_prod()
    if escolher in lst_produtos:
        index = get_index(lst_produtos, escolher)
        print(f"    --> Produto {lst_produtos[index]} - Quantidade {lst_qtds[index]} - Preço R${lst_precos[index]:.2f}")
        return input('[ENTER - VOLTA MENU]')
    else:
        return erro()

def deletar_um_produto():
    escolher = get_prod()
    if escolher in lst_produtos:
        index = get_index(lst_produtos, escolher)
        remove_prod([lst_produtos,lst_precos,lst_qtds], index)
        return input('Exclusão concluida [ENTER - VOLTA MENU]')
    else:
        return erro()

def cadastra_produto():
    try:
        name = write("Digite o nome do novo produto: ")
        if name in lst_produtos:
            return input('Item já cadastrado... [ENTER - VOLTA MENU]')
        qtd = int(write("Digite a quantidade do novo produto: "))
        valor = float(write("Digite o valor do novo produto: "))
        if len(name) > 0 and qtd is not None and valor is not None:
            lst_produtos.append(name)
            lst_qtds.append(qtd)
            lst_precos.append(valor)
            return input('PRODUTO CADASTRADOS COM SUCESSO [ENTER - VOLTA MENU]')
    except:
        return erro()

print('----------MENU----------')

while(True):
    choose = input('''
Escolha o número de uma das opções abaixo:
0 - Terminar o programa
1 - Cadastrar produto
2 - Imprimir um produto
3 - Retirar um produto
Escolha: ''')
    if choose == '0':
        break
    elif choose == '1':
        cadastra_produto()
    elif choose == '2':
        imprimir_um_produto()
    elif choose == '3':
        deletar_um_produto()
    else:
        input('Entrada Inválida... [ENTER - VOLTA MENU]')
