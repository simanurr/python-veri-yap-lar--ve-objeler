"""
2. dereceden bir bilinmeyenli denklemlerin köklerini bulma
denklem = a * x**2 + b*x + c
delta hesabı = b**2 - 4*a*c
1.kök = (-b - delta**0.5) / 2*a
2.kök = (-b + delta**0.5) / 2*a
"""
a = int(input("a değerini girin:"))
b = int(input("b değerini girin:"))
c = int(input("c değerini girin:"))
delta = b**2 - 4*a*c
kök_1 = int((-b - delta**0.5)/2*a)
kök_2 = int((-b + delta**0.5)/2*a)
print("denklemin 1. kökü:",kök_1)
print("denklemin 2. kökü:",kök_2)