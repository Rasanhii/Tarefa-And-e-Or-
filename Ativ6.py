ida = int(input('Digite a idade: '))
cat = input('Digite a categoria da pessoa (estudante, aposentado, etc.): ')
dia = input('Digite o dia da semana: ')

if ida >= 70:
    print('A pessoa tem direito a 30% de desconto')
elif cat == dia != 'quinta' and dia != 'domingo':
    print('A pessoa tem direito a 20% de desconto')
elif cat == 'aposentado' and 'estudante':
    print('A pessoa tem direito a 10% de desconto')
else:
    print('A pessoa não tem direito a desconto')