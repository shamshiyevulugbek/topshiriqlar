def person_info(ism,familiya,tugilgan_yil,tugilgan_joy,yosh,email ='',tel =''):
    '''Foydalanuvchi shaxsiy ma\'lumotlarini kiriting!'''
    dict1 ={
        'fname':ism,
        'lname':familiya,
        'birthday':tugilgan_yil,
        'born_place':tugilgan_joy,
        'age':yosh,
        'email':email,
        'tel':tel     
    }
    return dict1
custumers = []
print('Mijozlar ro\'yxatini rivojlantiramiz:')
mijozlar_soni = 0
while True:
    mijozlar_soni += 1
    ism = input(f'{mijozlar_soni} - mijozning ismini kiriting:')
    familiya = input(f'{mijozlar_soni} - mijozning familiyasini kiriting:')
    tugilgan_joy = input(f'{mijozlar_soni} - mijozning tug\'ilgan joyini kiriting:')
    tugilgan_yil = input(f'{mijozlar_soni} -  mijozning tug\'ilgan yilini kiriting:')
    yosh = input(f'{mijozlar_soni} - mijozning yoshini kiriting:')
    em = input(f'{mijozlar_soni} - mijozning emailini kiritasimi?(yes/no)\n:')
    if em == 'yes':
        email = input(f'{mijozlar_soni} - mijozning emailini kiriting:')
    else:
        email ='Noma\'lum'
    te = input(f'{mijozlar_soni} - mijozning telefon raqamini kiritasimi?(yes/no)\n:')
    if te == 'yes':
        tel = input(f'{mijozlar_soni} - mijozning telefon raqamini kiriting:')
    else:
        tel = 'Noma\'lum'
    custumers.append(person_info(ism,familiya,tugilgan_yil,tugilgan_joy,yosh,email,tel))
    yana = input('Yana mijoz qo\'shasizmi? (yes/no) \n :')
    if yana == 'no':
        break
print(custumers)