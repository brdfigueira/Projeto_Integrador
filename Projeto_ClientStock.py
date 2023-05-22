contador_clientes = 0  # Variável para armazenar o contador de clientes cadastrados

# Dicionário que representa o estoque de peças
estoque = {
    "Lâmpada de farol": {"quantidade": 0, "valor_unitario": 25.00},
    "Vela de ignição": {"quantidade": 0, "valor_unitario": 25.00},
    "Pastilha de freio": {"quantidade": 0, "valor_unitario": 25.00},
    "Fusível": {"quantidade": 0, "valor_unitario": 25.00}
}

# Adicionando cliente padrão
lista_clientes = [
    {
        "codigo": "000",
        "nome": "Cliente não cadastrado",
        "documento_identidade": "12.345.678-9",
        "cpf": "123.456.789-00"
    }
]


def cadastrar_cliente():
    """
    Função para cadastrar um novo cliente.
    """
    global contador_clientes  # Acessando a variável global

    contador_clientes += 1  # Incrementando o contador de clientes

    nome = input("Digite o nome completo do cliente: ")
    documento_identidade = input("Digite o número do documento de identidade: ")
    cpf = input("Digite o CPF do cliente (11 dígitos): ")

    # Validando o número do documento de identidade
    if len(documento_identidade) != 9 or not documento_identidade[:-1].isdigit() or documento_identidade[-1] not in ("X", "x", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        print("Número do documento de identidade inválido. O número deve ter 9 dígitos numéricos, sendo o último dígito igual a 'X' ou um dígito numérico.")
        return

    # Validando o CPF
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. O CPF deve ter 11 dígitos numéricos.")
        return

    # Formatando o documento de identidade e o CPF
    documento_identidade_formatado = f"{documento_identidade[:2]}.{documento_identidade[2:5]}.{documento_identidade[5:8]}-{documento_identidade[8]}"
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    # Criando um novo cliente
    cliente = {
        "codigo": f"{contador_clientes:03d}",
        "nome": nome,
        "documento_identidade": documento_identidade_formatado,
        "cpf": cpf_formatado
    }
    lista_clientes.append(cliente)

    print("Cadastro realizado com sucesso!")
    print("Dados do cliente:")
    print(f"Numero de cadastro: {cliente['codigo']}")
    print(f"Nome do Cliente: {cliente['nome']}")
    print(f"Documento de identidade: {cliente['documento_identidade']}")
    print(f"CPF: {cliente['cpf']}")
    print()


def entrada_estoque():
    """
    Função para registrar a entrada de peças no estoque.
    """
    print("Opções de peças para adicionar ao estoque:")
    print("1. Lâmpada de farol")
    print("2. Vela de ignição")
    print("3. Pastilha de freio")
    print("4. Fusível")

    opcao = input("Escolha uma opção de peça para adicionar ao estoque (1-4): ")
    if opcao not in ["1", "2", "3", "4"]:
        print("Entrada inválida. Por favor, selecione uma opção válida (1-4).")
        return

    quantidade = input("Digite a quantidade de peças a ser adicionada ao estoque: ")
    if not quantidade.isdigit():
        print("Quantidade inválida. Por favor, digite um valor numérico.")
        return

    quantidade = int(quantidade)
    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")

    # Atualizando a quantidade de peças no estoque
    if opcao == "1":
        estoque["Lâmpada de farol"]["quantidade"] += quantidade
    elif opcao == "2":
        estoque["Vela de ignição"]["quantidade"] += quantidade
    elif opcao == "3":
        estoque["Pastilha de freio"]["quantidade"] += quantidade
    elif opcao == "4":
        estoque["Fusível"]["quantidade"] += quantidade

    print("Estoque atualizado:")
    consultar_estoque()


def consultar_estoque():
    """
    Função para consultar o estoque de peças.
    """
    print("Estoque:")
    print(f"{'Peça':<20} {'Quantidade':<12} {'Valor Unitário':<15} {'Valor Total':<15}")
    print("-" * 60)

    for peca, info in estoque.items():
        quantidade = info["quantidade"]
        valor_unitario = info["valor_unitario"]
        valor_total = quantidade * valor_unitario
        print(f"{peca:<20} {quantidade:<12} R${valor_unitario:<14.2f} R${valor_total:<14.2f}")

    print()


def realizar_venda():
    """
    Função para realizar uma venda de peças.
    """
    codigo_cliente = input("Digite o código do cliente (000 a 999): ")

    cliente_encontrado = False
    cliente_selecionado = None

    # Procurando o cliente na lista de clientes cadastrados
    for cliente in lista_clientes:
        if cliente["codigo"] == codigo_cliente:
            cliente_encontrado = True
            cliente_selecionado = cliente
            break

    if not cliente_encontrado:
        print("Cliente não encontrado. Verifique o código digitado.")
        return

    print("Ficha do cliente:")
    print(f"Numero de cadastro: {cliente_selecionado['codigo']}")
    print(f"Nome do Cliente: {cliente_selecionado['nome']}")
    print(f"Documento de identidade: {cliente_selecionado['documento_identidade']}")
    print(f"CPF: {cliente_selecionado['cpf']}")
    print()

    confirmacao = input("O cliente selecionado está correto? (S/N): ")
    if confirmacao.upper() != "S":
        print("Venda cancelada.")
        return

    print("Produtos disponíveis no estoque:")
    print("1. Lâmpada de farol")
    print("2. Vela de ignição")
    print("3. Pastilha de freio")
    print("4. Fusível")

    opcao = input("Escolha uma opção de peça para adicionar à venda (1-4): ")
    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Por favor, selecione uma opção válida (1-4).")
        return

    quantidade = input("Digite a quantidade de peças a ser vendida: ")
    if not quantidade.isdigit():
        print("Quantidade inválida. Por favor, digite um valor numérico.")
        return

    quantidade = int(quantidade)
    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    # Verificando se há peças suficientes no estoque
    if opcao == "1":
        peca = "Lâmpada de farol"
    elif opcao == "2":
        peca = "Vela de ignição"
    elif opcao == "3":
        peca = "Pastilha de freio"
    elif opcao == "4":
        peca = "Fusível"

    if quantidade > estoque[peca]["quantidade"]:
        print("Quantidade insuficiente no estoque.")
        return

    # Calculando o valor total da venda
    valor_unitario = estoque[peca]["valor_unitario"]
    valor_total = valor_unitario * quantidade

    # Atualizando a quantidade de peças no estoque
    estoque[peca]["quantidade"] -= quantidade

    print("Venda realizada com sucesso!")
    print(f"Peça vendida: {peca}")
    print(f"Quantidade vendida: {quantidade}")
    print(f"Valor unitário: R${valor_unitario:.2f}")
    print(f"Valor total: R${valor_total:.2f}")
    print()


# Programa principal

while True:
    print("Sistema de Vendas de Peças")
    print("1. Cadastrar cliente")
    print("2. Registrar entrada de peças no estoque")
    print("3. Consultar estoque de peças")
    print("4. Realizar venda de peças")
    print("0. Sair")

    opcao = input("Digite a opção desejada (0-4): ")
    print()

    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        entrada_estoque()
    elif opcao == "3":
        consultar_estoque()
    elif opcao == "4":
        realizar_venda()
    else:
        print("Opção inválida. Por favor, selecione uma opção válida (0-4).")
        print()