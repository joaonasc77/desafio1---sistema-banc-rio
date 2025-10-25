menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[a] Cadastrar Conta Bancária
[q] Sair

=> """

saldo = 0
limite = 500        #limite máximo por saque
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3   #limite diário de saques
lista_clientes = []
lista_contas = []

#função que realiza depósito 
def deposito_bancario(valor, saldo, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

#função que realiza Saque
def saque_bancario(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

#função que mostra o Extrato Bancário
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

#função que cadastra cliente
def cadastrar_cliente(lista_clientes):
    nome = input("Digite o nome do novo cliente: ")
    data_nascimento = input("Digite a data de nascimento (DD-MM-AAAA): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ")
    cpf = input("Digite o CPF (somente números): ")
    
    #verificando se o cpf já existe
    for i in lista_clientes:
        if i["cpf"] == cpf:
            print("\nCPF já cadastrado no sistema!")
            return
        
    lista_clientes.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "cpf": cpf
    })
    
    print("Cliente cadastrado com sucesso!\n")

#função que cadastra conta bancária vinculada a um cliente
def cadastrar_conta_bancaria(lista_contas):
    agencia = "0001"
    cpf = input("Digite o CPF do cliente: ")

    #localizando o cliente pelo cpf
    cliente_encontrado = None
    for i in lista_clientes:
        if i["cpf"] == cpf:
            cliente_encontrado = i
            break
    
    if cliente_encontrado is None:
        print("\nCliente não encontrado. Cadastre o cliente antes de criar a conta!\n")
        return
    
    #numero da conta sequencial
    numero_conta = len(lista_contas) + 1

    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": cliente_encontrado
    }

    lista_contas.append(conta)

    print("\nConta criada com sucesso!")
    print(f"Agência: {agencia}, Conta: {numero_conta}, Titular: {cliente_encontrado}\n")
    

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do depósito: "))
        saldo, extrato = deposito_bancario(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Valor do saque: "))
        saldo, extrato, numero_saques = saque_bancario(
            saldo = saldo, 
            extrato = extrato, 
            valor = valor, 
            limite = limite, 
            numero_saques = numero_saques, 
            limite_saques = LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato = extrato)

    elif opcao == "c":
        cadastrar_cliente(lista_clientes)

    elif opcao == "a":
        cadastrar_conta_bancaria(lista_contas)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")