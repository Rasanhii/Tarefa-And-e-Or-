while True:
    nota1 = float(input("Insira a primeira nota (entre 0 e 100): "))
    nota2 = float(input("Insira a segunda nota (entre 0 e 100): "))

    loone = nota1 + nota2
    if loone >= 60 and nota1 >= 40 and nota2 >= 40:
        print("Parabéns, o aluno passou!")
    else:
        print("Infelizmente, o aluno não passou.",)

  
    fim = input("Deseja inserir novas notas? ('s' para sim ou 'n' para não)")

    if fim.lower() == "n":
        break
print("Obrigado por usar este programa!")