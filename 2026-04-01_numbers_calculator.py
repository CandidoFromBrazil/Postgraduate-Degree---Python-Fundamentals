def sum (a,b):
    x = int(a + b)
    return x
def difference (a,b):
    x = int(a - b)
    return x
def product (a,b):
    x = int(a * b)
    return x
def quotient (a,b):
    x = int(a / b)
    return x

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = input('Enter the operation you want to perform (sum, difference, product, quotient): ')

if c == 'sum':
    print(sum(a, b))
elif c == 'difference':
    print(difference(a, b))
elif c == 'product':
    print(product(a, b))
elif c == 'quotient':
    print(quotient(a, b))