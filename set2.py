def serOrNot(number,n):




    if number & (1 << (n)):
        print('\nset')
    else:
        print('\nnot set')

number = int(input('enter number'))
n = int(input('enter bit number'))
serOrNot(number, n)