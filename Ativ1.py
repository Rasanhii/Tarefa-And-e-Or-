while True:
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    num3 = float(input("Insira o terceiro número: "))

    if num1 > num2 + num3:
        maior = str(num1)
        print(maior + ' é maior do que a soma dos outros números.')
    elif num2 > num1 + num3:
        maior = str(num2)
        print(maior + ' é maior do que a soma dos outros números.')
    elif num3 > num1 + num2:
        maior = str(num3)
        print(maior + ' é maior do que a soma dos outros números.')
    else:
        print("Nenhum dos números é maior do que a soma dos outros dois.")

    fim = input("Deseja inserir novos números? Digite 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break

print("Obrigado por usar este programa!")