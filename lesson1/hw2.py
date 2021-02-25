a = int(input("Enter a:"))          # Variable a
b = int(input("Enter b:"))          # Variable b
c = int(input("Enter c:"))          # Variable c
D = b ** 2 - 4 * a * c              # Сalculation of discriminant
x1 = (-b + D**0.5) / 2*a            # Calculation of the first root
x2 = (-b - D**0.5) / 2*a            # Calculation of the second root
print(x1, x2, sep=';')              # Printing of roots
