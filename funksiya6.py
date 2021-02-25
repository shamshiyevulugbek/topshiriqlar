def son_darajasi(x ,y = 2):
    """x ning y darajasini hisoblovchi funksiya
    x : required -> float
    y: optional -> float, default -> y = 2    """
    return x ** y
a1 = son_darajasi(13)
a2 = son_darajasi(5,3)
a3 = son_darajasi(3,4)
print(a1)
print(a2)
print(a3)