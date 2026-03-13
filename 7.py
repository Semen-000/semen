a = int(input())
b = int(input())
n = int(input())

total_kop = (a * 100 + b) * n
rub = total_kop // 100
kop = total_kop % 100

print(rub, kop)