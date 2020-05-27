def fib(n): 
    a = 0
    b = 1
    if n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
        
def productFib(prod):
    for i in range(0,prod+2):
        if fib(i)*fib(i+1)>=prod:
            return [fib(i), fib(i+1), True if fib(i)*fib(i+1)==prod else False]


