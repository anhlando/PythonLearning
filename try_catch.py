def divide_func(a):
    try:
        return 42 / a
    except ZeroDivisionError:
        print('Invalid argument!!! Cannot divide by 0')


print(divide_func(2))
print(divide_func(4))
print(divide_func(7))
print(divide_func(0))
print(divide_func(5))