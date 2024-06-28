n = list(input())
if len(n) >= 3:
    n.sort()
    d = int(n[1]) - int(n[0])
    result = 'Ededi silsiledir'
    for i in range(2,len(n)):
        if int(n[i]) - int(n[i-1]) != d:
            result = 'Ededi silsile deyil'
    print(result)

n = input()
reqemler = '0123456789'
m = []
k = []
for i in n:
    if reqemler.count(i) == 1:
        if int(i) % 2 == 0 :
            m.append(i)
        else:
            k.append(i)
result = int(max(m)) + int(min(k))
print(result)



n = int(input()) # 264
n = str(n)
n = list(n)
if len(n) >= 3:
    n.sort()
    d = int(n[1]) - int(n[0])
    answer = 'Ededi silsiledir'
    for i in range(2,len(n)-1):
        if int(n[i]) - int(n[i-1]) != d:
            answer = 'Deyil'
    print(answer)

# Klaviaturadan daxil edilmiş A ədədindən B ədədinədək (hər ikisi daxil olmaqla), neçə ədədin həm özünün, 
# həm də rəqəmlərinin əks sırada yazılmasından alınan ədədin sadə olduğunu tapan Python kodunu yazın.
# Məsələn:
# Giriş : 10 25
# Çıxış: 3
# (11,13,17 ədədlərinin həm özləri sadədir, həm də 11, 31, 71 , yəni əks ardıcıllıqla yazılan ədədlər də sadədir)

def sade(x):
    f = 0
    for i in range(2,x // 2):
        if x % i == 0:
            f = 1
    return f

a = int(input())
b = int(input())
s = 0
for i in range(a, b+1):
    if sade(i) == 0:
        i = str(i)
        i = list(i)
        i.reverse()
        i = ''.join(i)
        if sade(int(i)) == 0:
            s = s+1
print(s)



a = int(input())
b = int(input())
s = (a*b)/2
print(s)