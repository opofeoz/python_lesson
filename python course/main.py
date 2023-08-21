# n = int(input(' '))
# n1 = (n % 1000) // 100
# n2 = (n % 100) // 10
# n3 = n % 10

# m1 = (n % 1000000) // 100000
# m2 = (n % 100000) // 10000
# m3 = (n % 10000) // 1000


# sum1 = (n1 + n2 + n3)
# sum2 = (m1 + m2 + m3)
# if sum1 == sum2:
#     print ('yes')
# else:
#     print ('No')

# n = 385 916 -> yes
# n = 123456 -> no


a = int(input('В-те 1-ю сторону: '))
b = int(input('В-те 2-ю сторону: '))
c = int(input('В-те кол-во долек: '))
if c % a == 0 or c % b == 0:
    print('yes')
else:
    print('no')
