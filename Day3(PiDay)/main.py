def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return(answer)

def Leibniz(goto):
    pi = 0
    sign = 1
    for i in range(1, 1+goto):
        pi += 1/((2*i-1)*sign)
        sign = -sign
    pi = pi*4
    return(pi)

def AbrahamSharp(goto):
    pi = 0
    for i in range(goto+1):
        a = 2*(-1**i)
        b = (1/2)-i
        c = 3**b
        d = (2*i)-1
        n = a*c/d
        pi += n
    return(pi)

def Euler(goto):
    pi = 0
    for i in range(goto+1):
        pi += factorial(i)/factorial(factorial(2*i+1))
    return(pi)

def Bellard(goto):
    pi = 0
    for i in range(goto+1):
        a = (-1**i)
        b = 2**(10*i)
        pi += a/b
    return(pi/(2**6))

print('Happy Pi Day, World!')
print('Pi:')
print('Leibniz`s formula:', Leibniz(1000))
print('Abraham`s Sharp formula:', AbrahamSharp(1000))
print('Eulet`s formula:', Leibniz(3))
print('Bellard`s formula:', Leibniz(1000))