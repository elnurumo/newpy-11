# n = int(input())  # 121
# n = str(n)
# a = list(n)
# a.reverse()
# a = ''.join(a)
# if n == a:
#     print('Polimdromdur')
# else:
#     print('Deyil')
# # print(a)


#  Sehvvvv!!!! Sətirlərin simvollarını bu şəkildə dəyişmək olmaz amma List-də olar.
# n = input()  # C3mpi3n
# for i in range(len(n)):
#     n[i] = 'a'
# print(n)

# bele olar
# n = 'salam'
# # n = 'necesen'
# print(n)

# n = input()
# # reqemler = '0123456789'
# s = ''
# for i in range(len(n)):
#     if '0'<= n[i] <='9':
#         s = s + 'a'
#     else:
#         s = s + n[i]
# print(s)


# a = int(input())
# b = int(input())
# while a!=b:
#     if a>b:
#         a = a-b
#     else:
#         b = b - a
# if a == 1:
#     print('Q.Sadedir')
# else:
#     print('Sade deyil')


# n = int(input()) #2344
# n = str(n)
# b = []
# for i in n:
#     c = n.count(i)
#     b.append(c)
# print(b)
# print(max(b))


# Klaviaturadan daxil edilmiş 1<a<b şərtini ödəyən a və b tam ədədləri üçün [ a,b ]
#  parçasındakı sadə ədədlərin cəmini hesablayan proqramı Python dilində yazın.

# a=int(input())
# b=int(input())
# e=0
# if b>a:
#     for i in range(a,b+1):
#         s=0
#         t=i
#         c=2
#         while i>1:
#             if i%c==0:
#                 s=s+1
#                 i=i//c
#             else:
#                 c=c+1
#         if s==1:
#             e=e+t
#     print(e)
