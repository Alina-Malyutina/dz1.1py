a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

if ((a+b)>c and (b+c)>a and (c+a)>b):
    print("This triangle can exist")
    if a == b == c:
        print("This triangle is isosceles") #равнобедренный
    elif (a == b or a ==c or b == c):
        print("This triangle is equilateral") #равносторонний
    else:
        print("This triangle is versatile") #разносторонний
else:
    print("This triangle can't exist")
