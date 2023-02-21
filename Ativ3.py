ida = int(input('Quantos anos você têm? '))
aut = input('Você tem autorização dos seus pais? (s/n) ')

if ida < 18 and aut == 'n':
    print ('Você não pode entrar.')
else:
    print ('Você pode entrar!')