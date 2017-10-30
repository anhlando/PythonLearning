#program that uses functions of Random module and Sys module.
import random, sys
for i in range(0,20,2):
    j = (random.randint(1,10))
    if j==7:
        while True:
            print('Enter E to exit')
            response = input()
            if response=='E':
                sys.exit()
            print ('You typed: ' + response + '. Please try again.')
    print (j)
        
