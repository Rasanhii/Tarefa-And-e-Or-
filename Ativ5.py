ida = int(input('Digite a idade da pessoa: '))
alfa = input('A pessoa sabe ler e escrever? (s/n): ')

if ida > 25 and alfa == 's':
    print('A pessoa é alfabetizada e tem mais de 25 anos.')
elif ida < 25 and alfa == 's':
    print('A pessoa é alfabetizada e tem menos que 25 anos.')
else:
    print('A pessoa não é alfabetizada e/ou tem menos que 25 anos.')