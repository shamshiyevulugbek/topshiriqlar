def tub_son(son):
    ''' sonni tublikka tekshiradi
    son -> int'''
    if son != 1:    
        tub = True
    else:tub = False
    if tub:
        for i in range(2,int(son ** (1 / 2)+1)):
            if not son % i:
                tub = False
                break
    return tub
def oraliqda_tub_sonlar(a,b):
    '''interval kiriting:
    a -> int
    b -> int'''
    tub_sonlar = []
    for i in range(a,b+1):
        if tub_son(i):
            tub_sonlar.append(i)
    return tub_sonlar
print('Oraliqlarni kiriting:')
a = int(input('a :'))
b = int(input('b:'))
list1 = oraliqda_tub_sonlar(a,b)
print(f'{a} va {b} sonari orasidagi tub sonlar:',list1)
# a = int(input('a ='))
# print(f'{a} soni tub :{tub_son(a)}')