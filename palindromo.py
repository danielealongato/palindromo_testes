lista_palavras_palindromo =['Rotator', 'bob', 'madam', 'mAlAyAlam', '1', 'Able was I, ere I saw Elba', 'Madam I’m Adam', 'Step on no pets.', 'Top spot!', '02/02/2020']


def palindrome_verify(frase):
    # text = str(input('Digite uma frase para validarmos se ela é Palìndromo: ')).strip().upper()
    text = frase.strip().upper()
    palavras = text.split()
    juntar = ''.join(palavras)
    inverso = juntar[::-1]

    if inverso == juntar:
        return True
        # print('Temos um palindromo!')
    else:
        return False
        # print("A frase digitada não é um palíndromo!")

def verify_function():


    for word in lista_palavras_palindromo:
        result = palindrome_verify(frase=word)
        print(f"Retorno:  {word} {result}")


if __name__ == '__main__':
    test = verify_function()