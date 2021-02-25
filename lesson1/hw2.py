a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
D = b ** 2 - 4 * a * c
x1 = (-b + D**0.5) / 2*a
x2 = (-b - D**0.5) / 2*a
print(x1, x2, sep=';')
