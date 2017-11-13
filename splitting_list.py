#spam = ['apples', 'bananas', 'tofu', 'cats']
#program to split a list of values into a string of child items, separated by ',' and a space
import copy


def split_list(list):
    result = ''
    i = 1
    result += list[0]
    while i < len(list) - 1:
        #string concat
        result +=  ', ' + list[i]
        i += 1

    result += ' and ' + list[i]
    return result


#main program:
input_List = []
while True:
    print('Add a new item to the list(Enter :q to finish):')
    item = input()
    if item == ':q':
        break
    else:
        input_List.append(str(item))



print('Your input list is: ', end='')
print(input_List)
print('Splitting input list into: ')
print(split_list(input_List))




