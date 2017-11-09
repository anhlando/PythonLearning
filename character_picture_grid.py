grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


#function to convert original list a*b to a result list b*a
def reverse_list(original):
    val = ''
    rows = len(original)
    cols = len(original[0])
    #loop through the original list's cols
    for j in range(cols):
        #loop through rows
        for i in range(rows):
            if original[i][j] == 'O':
                val += 'x '
            else:
                val +=  '  '
        print(val)
        val = ''



#main
print('Original list: ', end='')
print(grid)
print('Reverse list: ')
reverse_list(grid)




