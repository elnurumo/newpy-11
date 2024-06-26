# 71
# n = int(input())
# s = 0
# for i in range(0,n):
#     a = int(input())
#     s = s + a
# print(s/n)

# 72

# n = int(input())
# b = []
# for i in range(0,n):
#     a = int(input())
#     b.append(a)
# print(min(b))

# b = []
# for i in range(1,1000,2):
#     b.append(i)
# print(b)


# a = [15,12,16,11,9]
# for i in range(0,len(a)):
#     if i % 2 != 0 and a[i]%2 == 0:
#         print(a[i]**2)


# n = int(input())
# if n == 12 or n == 1 or n == 2:
#     print('Qışdadır')
# elif n == 3 or  n== 4 or n == 5:
#     print('Yazdir')
# elif n == 6 or n == 7 or n == 8:
#     print('Yaydir')
# elif n == 9 or n == 10 or n == 11:
#     print('Payizdadir')
# else:
#     print('Elə bir ay sırası yoxdur')


# # 79
# n = int(input())  # 12000
# s = 0
# while n % 10 == 0:
#     s = s + 1
#     n = n // 10
# print(s)

# 80
# n = int(input())
# flag = 0
# if n > 1:
#     for i in range(2,n//2+1):
#         if n % i == 0:
#             flag = 1
#     if flag == 1:
#         print('Murekkeb')
#     else:
#         print('Sade')


n = input().split()
print(n)
k = 0
b = 0
while b<=30:
    a = max(n)
    b = b + int(a)
    n.remove(a)
    c = int(a)//2
    n.append(c)
    k = k + 1
print(k)