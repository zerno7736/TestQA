s = 'Hel5lo'
w = '0123456789'
flag = False
for i in range(len(s)):
    if s[i] in w:
        flag = True
if flag:
    print('Цифра')
else:
    print('Цифр нет')