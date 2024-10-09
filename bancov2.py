from datetime import datetime

# Variáveis iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10
numero_conta_sequencial = 1
usuarios = []
contas = []

# Função para criar um novo usuário
def novo_usuario(nome, data_nascimento, cpf, endereco, usuarios):
    # Verifica se o CPF já existe
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: CPF já cadastrado.")
            return
    # Adiciona o novo usuário à lista
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário criado com sucesso!")

# Função para criar uma nova CC
def nova_conta(usuarios, agencia, numero_conta_sequencial, cpf_usuario, contas):
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            conta = {
                'agencia': agencia,
                'numero_conta': str(numero_conta_sequencial).zfill(4),
                'usuario': usuario
            }
            contas.append(conta)
            print("Conta corrente criada com sucesso!")
            return
    print("Erro: Usuário não encontrado.")

# Função para listar contas
def listar_contas(contas):
    if not contas:
        print("Não há contas cadastradas.")
        return
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        print(f"""
  Agência: {conta['agencia']}
  Número da Conta: {conta['numero_conta']}
  Usuário: {conta['usuario']['nome']}
  CPF: {conta['usuario']['cpf']}
""")
    print("===================================================")

# Função para depositar
def depositar(saldo, valor, extrato, /):
    saldo += valor
    hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato += f"Depósito: R$ {valor:.2f} | Data: {hora}\n"
    print("Depósito realizado com sucesso!")
    return saldo, extrato

# Função para sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques por dia excedido.")
    elif valor > 0:
        saldo -= valor
        hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"Saque: R$ {valor:.2f} | Data: {hora}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

# Função para exibir extrato
def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Menu
menu = """
================ Você está usando o BancoVS ================

Qual operação deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo, extrato = depositar(saldo, valor, extrato)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato,
                                              limite=limite, numero_saques=numero_saques,
                                              limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Informe o CPF: ")
        endereco = input("Informe o endereço (logradouro, nro, bairro, cidade, estado): ")
        novo_usuario(nome, data_nascimento, cpf, endereco, usuarios)

    elif opcao == "nc":
        agencia = input("Informe a agência: ")
        cpf_usuario = input("Informe o CPF do usuário: ")
        nova_conta(usuarios, agencia, numero_conta_sequencial, cpf_usuario, contas)
        numero_conta_sequencial += 1  # Incrementa o número da conta

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

#Criado por Victor Vieira dos Santos para o desafio da DIO