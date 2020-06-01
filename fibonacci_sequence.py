import lifeeasy
import sys

sys.setrecursionlimit(10**6)

number_of_iteration = 10

fibonacci_sequence = [None] * number_of_iteration

memo = [None] * number_of_iteration

def fib(n):
    global memo
    if memo[n - 1] != None:
        result = memo[n - 1]
    elif n == 1 or n == 2:
        result = 1
    elif n > 2:
        result = fib(n-1) + fib(n-2)
    else:
        result = "Not a positive number"
    memo[n - 1] = result
    #print(result)
    return(result)

for i in range(number_of_iteration):
    if i == 0:
        fibonacci_sequence[i] == 0
        continue
    fibonacci_sequence[i] = fib(i)

for number in fibonacci_sequence:
    print(number)
