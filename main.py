import scripts.query

# n = input("Database Name: ")
# n =scripts.query.create_database(n)
# print(n)

while True:
        print("\nMenu")
        print("1. Criar Tabela")
        print("2. Inserir Dados")
        print("3. Sair")

        # Aqui você pode adicionar lógica para pegar a entrada do usuário
        # no futuro, mas por enquanto, apenas exiba o menu.
        
        # Para sair do loop, você pode usar um comando fixo como:
        escolha = input("Selecione uma Opção: ")
        
        if escolha == '1':
            n = input("Nome do Banco de Dados: ")
            n = scripts.query.create_database(n)
            print(n)
        elif escolha == '2':
            dbs = scripts.query.listDB()
            for db in dbs:
                print(db)
            db = input("Selecione o Banco de Dados: ")
            
        elif escolha == '3':
            print("Saindo do programa.")
            break