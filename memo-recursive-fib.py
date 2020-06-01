import lifeeasy
import sys

sys.setrecursionlimit(10**6)

iteration = 0

def fib(n, memo):
    global iteration
    iteration += 1
    if memo[n - 1] != None:
        result = memo[n - 1]
    elif n == 1 or n == 2:
        result = 1
    elif n > 2:
        result = fib(n-1, memo) + fib(n-2, memo)
    else:
        result = "Not a positive number"
    memo[n - 1] = result
    #print(result)
    return(result)

print("What's the number you want to get from Fibonacci?")
n = int(input('> '))
lifeeasy.clear()

memo = [None] * n
print(fib(n, memo))
print("It took " + str(iteration) + ' iteration to get this result.')