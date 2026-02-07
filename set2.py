def serOrNot(number,n):




    if number & (1 << (n-1)):
        print('\nset')
    else:
        print('\not set')

number = int(input('enter number'))
n = int(input('enter bit number'))
serOrNot(number, n)