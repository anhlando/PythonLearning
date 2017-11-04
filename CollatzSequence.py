def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


print('Input an integer to start the Collatz sequence: ',end=" ")
i = int(input())
while i != 1:
    i = collatz(i)
    print(str(i))


