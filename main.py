import random
cim = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLNOPQRSTUVWXYZ1234567890'

number = int(input('Number of passwords: '))
lenght = int(input('Length password: '))

for x in range( number ):
    password = ''

    for i in range( lenght ):
        password += random.choice( cim )

    print( password)
input()
