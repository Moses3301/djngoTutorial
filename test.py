def fib(arg):
    if arg<=2:
        return 1
    return fib(arg-1)+fib(arg-2)

print(fib(10))
