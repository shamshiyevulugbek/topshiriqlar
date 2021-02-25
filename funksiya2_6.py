def fibonachi(son):
    '''fibonachi sonlarning ro\'yxatini chiqrish funksiyasi
    son -> int'''
    a1 = 1 
    a2 = 1
    list1 =[1,1]
    for i in range(3,son + 1):
        a3 = a1 + a2 
        a1,a2 = a2,a3
        list1.insert(i,a3)
    return list1
a = int(input('a ='))
print('Fibonachi sonlar ro\'yxati:',fibonachi(a))