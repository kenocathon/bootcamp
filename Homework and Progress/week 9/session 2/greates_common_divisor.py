num_1 = int(input('Enter the first number '))
num_2 = int(input('Enter the second number '))



def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)




print(gcd(num_1, num_2))

