pi = 3.14
def aylana(radius):
    '''Aylananing radiusini kiriting:'''
    doira = {
        'radius':radius,
        'diametr': 2 * radius,
        'perimetr': pi * 2 *radius,
        'yuza': pi * radius ** 2
    }
    return doira
a = float(input('aylana radiusini kiriting:'))
print(aylana(a))