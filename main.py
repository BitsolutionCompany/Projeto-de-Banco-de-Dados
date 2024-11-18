import scripts.query

# n = input("Database Name: ")
# n =scripts.query.create_database(n)
# print(n)

while True:
        print("\nMenu")
        print("1. Criar Criar Banco de Dados")
        print("2. Criar Tabela")
        print("3. Inserir Dados")
        print("0. Sair")

        escolha = input("Selecione uma Opção: ")
        
        if escolha == '1':
            n = input("Nome do Banco de Dados: ")
            n = scripts.query.create_database(n)
            print(n)
        elif escolha == '2':
            dbs = scripts.query.listDB()
            print("\n\n")
            for db in dbs:
                print(db)
            db = input("Selecione o Banco de Dados: ")
            
            if db not in dbs:
                print(f"O banco de dados '{db}' não existe. Por favor, selecione um banco de dados válido.")
                continue
            
            table = input("Nome da Tabela: ")
            colunas = []
            while True:
                res = input("Nome da Coluna (ex.: Id int not null primary key auto-increment) digite 'fim' para finalizar: ")
                
                if res.lower() == 'fim':
                    break
                
                colunas.append(res)
            r = scripts.query.createTable(db, table, colunas)
            print(r)
        elif escolha == '3':
            dbs = scripts.query.listDB()
            print("\n")
            for db in dbs:
                print(db)
            print("\n")
            
            db = input("Selecione o Banco de Dados: ")
            
            if db not in dbs:
                print(f"O banco de dados '{db}' não existe. Por favor, selecione um banco de dados válido.")
                continue
            
            tbs = scripts.query.listTable(db)
            print("\n")
            for tb in tbs:
                print(tb)
            print("\n")
            tb = input("Selecione a Tabela(Nome da Tabela): ")
            
            if tb not in tbs:
                print(f"A tabela '{tb}' não existe nesse banco de dados. Por favor, selecione uma Tabela válida.")
                continue
            
            valores = []
            columns = scripts.query.getColumn(db, tb)
            for col in columns:
                value = input(f"Informe o valor da coluna {col}: ")
                valores.append(value)
            a = scripts.query.insertDados(db, tb, columns, valores)
            print(a)
            print("\n")
            
            
        elif escolha == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção Inválida!")