import lifeeasy

iteration = 0

def fib(n):
    global iteration
    iteration += 1
    if n == 1 or n == 2:
        result = 1
    elif n > 2:
        result = fib(n-1) + fib(n-2)
    else:
        result = "Not a positive number"
    #print(result)
    return(result)

print("What's the number you want to get from Fibonacci?")
n = int(input('> '))
lifeeasy.clear()

print(fib(n))