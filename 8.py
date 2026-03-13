n = int(input())

h = n // 3600
h = h % 24
m = (n - h * 3600) // 60
s = n % 60

print(h, ":", m // 10, m % 10, ":", s // 10, s % 10, sep="")