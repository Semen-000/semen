n = int(input())
sotni = n // 100
desyatki = (n // 10) % 10
edinici = n % 10
summa = sotni + desyatki + edinici
print(summa)