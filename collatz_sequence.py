def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


print('Input an integer to start the Collatz sequence: ',end=" ")
count = 0
i = int(input())
while i != 1:
    count = count + 1
    i = collatz(i)
    print(str(i))

print('Total attemp(s) to reach 1: ' + str(count))

