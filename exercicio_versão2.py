def verificador_de_palindromo(supostos_palindromos):
    for suposto_palindromo in supostos_palindromos:
        suposto_palindromo = suposto_palindromo.lower().replace("’", "").replace('!', '').replace('.', '').replace(',', '').replace('/',
                                                                                                               '').replace(
            '-', '')
        palavras = suposto_palindromo.split()
        suposto_palindromo_tudo_junto = ''.join(palavras)
        inverso = suposto_palindromo_tudo_junto[::-1]
        if inverso != suposto_palindromo_tudo_junto:
            print(f'{suposto_palindromo} não é um palíndromo!')
        else:
            print(f'{suposto_palindromo} é um palíndromo!')


supostos_palindromos = ['Rotator', 'bob', 'madam', 'mAlAyAlam',
                        '1', 'Able was I, ere I saw Elba',
                        'Madam I’m Adam', 'Step on no pets.',
                        'Top spot!', '02/02/2020', 'xyz',
                        'elephant', 'Country', 'Top . post!',
                        'Wonderful-fool', 'Wild imagination!']

verificador_de_palindromo(supostos_palindromos=supostos_palindromos)