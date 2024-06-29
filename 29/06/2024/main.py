# n = int(input()) #5
# # n = 5
# s = 0
# for i in range(2,n//2+1):
#     if n%i==0:
#         s = s + 1
# if s == 0:
#     print('Sadedir')
# else:
#     print('Murekkeb')



# n=int(input())
# s=0
# for i in range(2,n//2+1):
#     if n%i==0:
#         s=1
# if s==0:
#     print("sadedi")
# else:
#     print("murekkeb")


# n = int(input())
# x=[]
# for i in range(n):
#     a = int(input())
#     x.append(a)
# print(min(x))


# n=[5,6,22,114,62,14]
# min = n[0]
# for i in n:
#     if min>i:
#         min = i
# print(min)


# n=[5,6,22,114,62,14]
# for i in range(len(n)):
#     n[i] = '1'
# print(n)

# 1-ci metod
# n= 'Feqan'
# s = ''
# for i in range(len(n)):
#     if n[i] == 'e':
#         s = s + 'a'
#     else:
#         s= s + n[i]
# n = s
# print(n)

# 2 - ci metod
# n= 'Feqan'
# n = n.replace('e','a')
# print(n)

# 81
# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + (-1)**(i+1) * i*(i+1)
# print(s) 





# 84
# a = [3,4,2,1,6,9,7,8,12,10,5,14]
# edediOrta = 0
# say = 0
# for i in range(len(a)):
#     if i % 2 != 0 and a[i] % 2 == 0:
#         edediOrta = edediOrta + a[i]
#         say = say + 1
#     elif i % 2 == 0 and  a[i] % 2 != 0:
#         edediOrta = edediOrta + a[i]
#         say = say + 1
# print(edediOrta/say)





a = [3,4,15,9,18,16]
for i in a:
    c = i ** 0.5
    if c == int(c):
        print(i)
