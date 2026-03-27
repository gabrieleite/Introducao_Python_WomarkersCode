# Desafio Prático: Sistema de Cadastro e Análise de Estudos

'''
Objetivo
Construir um programa que organiza informações de
participantes de um curso e gera pequenos relatórios de
desempenho. É a oportunidade perfeita para ver como
listas, dicionários e laços de repetição trabalham
em equipe
'''

# Dados fixos (Nome do curso, duração em meses, carga horária)
curso = ("Python para Iniciantes", 2, 70)

# Menu interativo
alunas = []
opcao = 0
nome = input("Qual o seu nome? ")
while opcao != 4:
    print("-" * 50)
    print(f"Curso: {curso[0]} | Carga horária: {curso[2]}")
    print(f"Olá, {nome}! Seja bem vinda ao nosso menu!")
    print("1 - Cadastrar participante")
    print("2 - Mostrar participantes")
    print("3 - Mostrar análises")
    print("4 - Sair")
    opcao = int(input("Escolha uma das opções: "))

    if opcao == 1: 
        print("\nCADASTRO DE PARTICIPANTE")
        nome_participante = input("Nome da participante: ")
        idade = int(input("Idade da participante: "))
        if idade <= 0:
            print("\nNão é permitido idade negativa! Digite uma idade válida")
            idade = int(input("Idade da participante: "))
        horas_estudo = float(input("Horas de estudo: "))
        if horas_estudo < 0:
            print("\nNão é permitido horas de estudo negativas! Digite horas válidas: ")
            horas_estudo = float(input("Horas de estudo: "))
        area_interesse = input("Área de interesse da participante: ")

        aluna = {
            "nome": nome_participante,
            "idade": idade,
            "horas_estudo": horas_estudo,
            "area_interesse": area_interesse
        }

        # Apenas exercício
        dobro_idade = aluna["idade"] * 2
        idade_quadrado = aluna["idade"] ** 2

        
        alunas.append(aluna)
        print("\nCadastro finalizado com sucesso!")

    elif opcao == 2: 
        if not alunas:
            print("Nenhuma aluna cadastrada!")
        else: 
            print("\nLista de participantes:")
            for a in alunas:
                print("-" * 40)
                print(f"Nome: {a['nome']}")
                print(f"Idade: {a['idade']}")
                print(f"Horas de Estudo: {a['horas_estudo']}")
                print(f"Área de Interesse: {a['area_interesse']}")

    elif opcao == 3: 
        if not alunas:
            print("\nNão há dados para análise!")
        else: 
            total_alunas = len(alunas)
            maioridade = 0 
            soma_horas = 0
            for a in alunas:
                soma_horas += a["horas_estudo"]

            media = soma_horas / total_alunas

            print("\n---- Análises ----")
            print(f"\nTotal de participantes: {total_alunas}")
            for a in alunas:
                if a["idade"] >= 18:
                    maioridade += 1
            print(f"\nMaiores de idade: {maioridade}")
            print(f"\nMédia de horas de estudo: {round(media, 2)}")

            minimo = 5

            print("\nParticipantes com bom ritmo de estudos (>= 5):")
            for a in alunas:
                if a["horas_estudo"] >= minimo:
                    print("-",a["nome"])
            areas = []

            for a in alunas:
                if a["area_interesse"] not in areas:
                    areas.append(a["area_interesse"])
            print("\nÁreas de interesse:")
            for area in areas:
                print("-", area)
    elif opcao == 4: 
        print("Saindo...")
    elif opcao < 1 or opcao > 4:
        print("\nOPÇÃO INVÁLIDA!")


