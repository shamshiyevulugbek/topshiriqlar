def juft_toq(son):
    """Juft toqlikka tekshirish!"""
    if son % 2 == 0:
        print(f'{son} soni juft')
    else:
        print(f'{son} soni toq')
for i in list(range(10)):
    juft_toq(i)