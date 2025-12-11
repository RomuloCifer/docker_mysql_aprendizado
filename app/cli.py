from app.repository import criar_tabela_clientes_se_nao_existir, resetar_tabela_clientes, inserir_cliente, listar_clientes, listar_clientes_acima_idade, informacoes_idade


def obter_nome_idade():
    """Pega o nome e idade do usuário através do input."""
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    return nome, idade

def menu():
    opcoes = {
        "1": ("Criar tabela de clientes se não existir", criar_tabela_clientes_se_nao_existir),
        "2": ("Resetar tabela de clientes", resetar_tabela_clientes),
        "3": ("Inserir novo cliente", lambda: inserir_cliente(*obter_nome_idade())),
        "4": ("Listar todos os clientes", lambda: print(listar_clientes())),
        "5": (
            "Listar clientes acima de certa idade",
            lambda: print(listar_clientes_acima_idade(int(input("Idade mínima: ")))),
        ),
        "6": ("Mostrar informações de idade", informacoes_idade),
        "0": ("Sair", None),
    }
    while True:
        print("\nMenu:")
        for chave, (descricao, _) in opcoes.items():
            print(f"{chave} - {descricao}")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Saindo...")
            break

        acao = opcoes.get(escolha)
        if acao is None:
            print("Opção inválida. Tente novamente.")
            continue

        _, func = acao
        if func is not None:
            func()