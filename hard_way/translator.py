def translator(phares):
    transaltion=""
    for letter in phares:
        if letter in 'AEIOUaeiou':
            if letter.isupper():
                transaltion = transaltion + 'G'
            else:
                transaltion=transaltion+'g'
        else:
            transaltion=transaltion+letter
    return transaltion
#print(translator(input('Enter a phrase: ')))

try:

    number=int(input('Enter a number:'))
    number=number/0
    print(number)
except ZeroDivisionError:
    print('Divided by Zero')
except ValueError:
    print('Invalid number')

