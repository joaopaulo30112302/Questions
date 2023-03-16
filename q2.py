def fib(number):
    fibList = [0, 1]
    while fibList[-1] < number:
        fibList.append(fibList[-1] + fibList[-2])
    return number in fibList

userInput = 15

if fib(userInput):
    print(str(userInput) + " pertence à sequência de Fibonacci")
else:
    print(str(userInput) + " não pertence à sequência de Fibonacci")