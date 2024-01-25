import sys

# Cadastro de usuário:
def cadastrar_usuario():
    nome = input("Nome do titular da conta: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    cpf = input("CPF do titular da conta: ")
    endereco = input("Endereço do titular da conta: ")

    usuario = {
        'Nome': nome,
        'Data de Nascimento': data_nascimento,
        'CPF': cpf,
        'Endereço': endereco
    }

    print("Usuário criado com sucesso!")
    return usuario

#Cadastro da conta corrente
def cadastrar_conta_corrente(usuarios, contas):
    usuario_cpf = input("Informe o CPF do titular da conta: ")

    # Verifica o CPF da pessoa:
    usuario_existente = next((user for user in usuarios if user['CPF'] == usuario_cpf), None)

    if usuario_existente:
        agencia = "0001"
        numero_conta = len(contas) + 1

        conta_corrente = {
            'Agência': agencia,
            'Número da Conta': numero_conta,
            'Usuário': usuario_existente,
            'Saldo': 0,
            'Extrato': []
        }

        contas.append(conta_corrente)
        print("Conta corrente criada com sucesso!")

        # Exibe a conta corrente
        return conta_corrente
    else:
        print("Usuário não encontrado. Crie um usuário primeiro.")

#Saque:
def saque(saldo, valor, extrato, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# Depósito
def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# Extrato com extrato e saldo da conta
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("\n".join(extrato) if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("==========================================")


# Função principal do programa:
def main():
    saldo = 0
    numero_saques = 0
    limite_saques = 3
    extrato = []

    usuarios = []  # Lista para armazenar os usuários
    contas = []    # Lista para armazenar as contas correntes

    while True:
        print("\n[1] Criar Usuário")
        print("[2] Criar Conta Corrente")
        print("[3] Realizar Depósito")
        print("[4] Realizar Saque")
        print("[5] Exibir Extrato")
        print("[6] Sair")

        opcao = input("Escolha sua opção: ")

        if opcao == "1":
            usuario = cadastrar_usuario()
            usuarios.append(usuario)
        elif opcao == "2":
            conta_corrente = cadastrar_conta_corrente(usuarios, contas)
            if conta_corrente:
                print("\nDetalhes da Conta Corrente Criada:")
                print("Agência:", conta_corrente['Agência'])
                print("Número da Conta:", conta_corrente['Número da Conta'])
                print("Titular:", conta_corrente['Usuário']['Nome'])
                print("CPF do Titular:", conta_corrente['Usuário']['CPF'])
        elif opcao == "3":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "4":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(saldo, valor, extrato, numero_saques, limite_saques)
        elif opcao == "5":
            exibir_extrato(saldo, extrato)
        elif opcao == "6":
            print("Saindo do programa...Obrigado por utilizar nossos serviços!")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
