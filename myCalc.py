##간단 계산기##

def Plus(x, y):
    return x+y

def Minus(x, y):
    return x-y

def Multi(x, y):
    return x*y

def Divi(x, y):
    return x//y

while True:
    n1 = int(input(' 첫번째 수 : '))
    if n1 == 0:
        print(' Bye-Bye!! ')
        break
    op = input(' [+, -, *, / ] : ')
    n2 = int(input(' 두번째 수 : '))

    if op == '+':
        r = Plus(n1, n2)
    elif  op == '-':
        r = Minus(n1, n2)
    elif  op == '*':
        r = Multi(n1, n2)
    elif  op == '/':
        r = Divi(n1, n2)
    else:
            continue
    print(' {} {} {} = {}'.format(n1, op, n2, r))
    
