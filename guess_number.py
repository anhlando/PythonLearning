import random

count = 0  # global variable to store how many times user has guessed

def Guess(guess,number):
    #average = (min + max)//2
    if guess < number:
        print('Your number is too low!')
        return 0
    elif guess>number:
        print('Your number is too high!')
        return 0
    else:
        return 1

res = random.randint(1,20)
print('I am thinking of a number between 1 and 20. Take a guess.')
ans = input()
while Guess(int(ans),res)!= 1 and count < 6:
    count = count + 1
    print('Please guess again: ',end=" ")
    ans = input()

if count < 6:
    print('Congratulation!!!! You have successfully guessed the number after ' + str(count+1) + ' tries')
else:
    print('You have used all of 6 attemps to guess. The correct answer is: ' +  str(res))


