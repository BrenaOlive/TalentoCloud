while True:
    nome_completo = input("Digite seu nome completo: ")

    while True:
        ano_nascimento_str = input("Digite o ano de nascimento (1922 a 2021): ")
        try:
            ano_nascimento = int(ano_nascimento_str)
            if 1922 <= ano_nascimento <= 2021:
                break
            else:
                print("Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    ano_atual = 2023
    idade = ano_atual - ano_nascimento

    print("Olá",nome_completo)
    print("Você completou ou completará",idade,"anos em 2022.")
    
    sair = input("Deseja sair? (Digite 's' para sair, ou pressione Enter para continuar): ")
    if sair == 's':
        print("Saindo. Até logo!")
        break