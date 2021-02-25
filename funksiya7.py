def bolinish_alomatlari(son):
    '''Berilgan sonni 2 dan 10 gacha bo\'lgan sonlarga bo\'linishini tekshiradi'''
    for i in range(2,11):
        if not son % i:
            print(f'{son} soni {i}ga qoldiqsiz bo\'linadi!')
bolinish_alomatlari(60)
bolinish_alomatlari(36)            