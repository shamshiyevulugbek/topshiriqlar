def katta_kichik(a,b):
    """2 ta sondan kattasini  topib beruvchi funksiya :)"""
    if a > b:
        print(f'{a} soni katta')
    elif a==b:
        print(f'{a} soni {b} soniga teng')
    else:print(f'{b} soni katta')
katta_kichik(45,29)
katta_kichik(10,10)
katta_kichik(1,7)