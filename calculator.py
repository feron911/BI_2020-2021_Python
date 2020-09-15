def calcul (a, b, c):
    if c == 0 and b == '/':
        return "Zero division error"
    #sigh = {'+': a+c, '-': a-c, '*':a*c, '/':a/c}
    return eval(a+b+c)
print('Insert first number and press enter:')
fn = input()
print('Insert math symbol(+,-,*,/) and press enter:')
ms = input()
print('Insert second number and press enter:')
sn = input()
print('Answer is', calcul(fn,ms,sn))