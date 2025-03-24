
print(f'{'\033[31m'}-={'\033[m'}'*30)
n = int(input(f'{'\033[4;31m'}Digite quantos termos você quer mostrar: {'\033[m'}'))
print(f'{'\033[31m'}-={'\033[m'}'*30)
t1 = 0
t2 = 1


cont = 3
print(f' {t1} → {t2}',end='')
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3} ',end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → Fim')
