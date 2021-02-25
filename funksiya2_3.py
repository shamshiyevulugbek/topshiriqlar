def maksimal(son):
    '''uchta sondan eng kattasini topuvchi funksiya
    '''
    maxs = son[0]
    for i in son:
        if i > maxs:
            maxs = i
    return maxs
k = int(input('k = '))
a = [int(input('son =')) for i in range(k)]
print(f'maksimal son :{maksimal(a)}')

