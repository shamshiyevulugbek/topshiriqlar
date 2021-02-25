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
person1 = person_info('Ulug\'bek','Shamshiyev',1999,'Samarqand',21,'developerprogrammer@gmail.com','+998979269566')
person2 = person_info('Axmadjon','Isoqov',2000,'Farg\'ona',20)
print(person1['fname'])
print(person2['age'])