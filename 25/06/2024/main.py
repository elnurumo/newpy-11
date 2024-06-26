# 1 ci sual həlli

n = int(input()) # 145
n = str(n)
n = list(n)
for i in range(1,len(n)+1,2):
    n.insert(i,'1')
n = ''.join(n)
print(int(n)**2)

#  2 - ci sual

a= [4,4,4,4]
b=[4,4,4] 
# s = 0
c = []
for i in b:
    if a.count(i) !=0 :
        c.append(i)
print(len(c))

# 12 - ci sual

def func(n):
    f = 0
    for i in range(2,(n//2)+1):
        if n % i == 0:
            f = 1
    return f
n = int(input())
if func(n) == 1:
    print('M')
    a = n - 1
    while func(a) == 1:
        a = a - 1
else:
    print('S')
    a = n + 1
    while func(a) == 1:
        a = a + 1
s = 0
for i in str(a):
    s = s + int(i)
print(s)