number = int(input('Enter your number. It must be positive and less than 100000: '))
if number < 0 or number > 100000:
    print("Your number is uncorrect")
    exit()

count = 0
for i in range(2, number // 2+1):
    if (number % i == 0):
        count += 1
if (count <= 0):
    print("Number is prime")
else:
    print("Number isn't prime")