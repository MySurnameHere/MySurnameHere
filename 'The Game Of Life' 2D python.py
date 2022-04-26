import time
import random

a = 110
def count_neighbords(ss, ii, gg):
    res = 0
    if ss[ii - 1][gg - 1] == 1:
        res += 1
    if ss[ii - 1][gg] == 1:
        res += 1
    if ss[ii - 1][(gg + 1) % n] == 1:
        res += 1
    if ss[ii][gg - 1] == 1:
        res += 1
    if ss[ii][(gg + 1) % n] == 1:
        res += 1
    if ss[(ii + 1) % z][gg - 1] == 1:
        res += 1
    if ss[(ii + 1) % z][gg] == 1:
        res += 1
    if ss[(ii + 1) % z][(gg + 1) % n] == 1:
        res += 1
    if False:
        for v in s:
            print(v)
        print('count_neighbords: ii,gg= {0},{1} res= {2} '.format(ii, gg, res))
    return res
     
s = []
c = [1]
while a != 1 and s != c: # while чтобы программа могла работать бесконечное количество раз
    s = []
    print("Введите количесво поколений")
    q = int(input())
    print('Введите длинну мира.')
    z = int(input())
    print('Введите количество символов в строках.') # Прием ограничений мира
    n = int(input())
    u = []
    for i in range(z):
        for i in range(n):
            u.append(random.randint(0, 1)) # Создание рандомного начала жизни
        s.append(u)
        u = []
    for x in range(q):
        c = []
        for i in range(z):
            k = []
            for g in range(n):
                neighboards = count_neighbords(s, i, g)
                if neighboards == 3:
                    k.append(1)
                elif s[i][g] == 1 and neighboards == 2:
                    k.append(1)
                else:
                    k.append(0)
                # print('n,k: ', neighboards, k)
            t = s[i]
            r = [str(w) for w in t]
            r = ''.join(r)
            # print(r) # Вывод одной строки жизни
            r = r.replace('1', '■')
            r = r.replace('0', ' ') # Несколько строчек кода для перевода жизни из 1, 0 в "∎", " "
            print(r) # Вывод одной строки жизни
            c.append(k)
        s = c
        print('')
        print('-' * 50)
        time.sleep(0.5) # Подготовка к следующей строке
    print('Хотите продолжить? Введите yes, если да, no, если нет.')
    if input() != 'yes': # Перезапуск программы по просьбе пользователя
        a = 1
