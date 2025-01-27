def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result  * i
    return result

print(factorial(5))



factorial_lambda = lambda n: 1 if n == 1 else n * factorial_lambda(n - 1)


print(factorial_lambda(5))