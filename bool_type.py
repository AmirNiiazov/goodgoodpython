x = round(float(input()), 2)
print((x - int(x)) > 0.5)


a, b = map(int, input().split())

print(a%b == 0)


a, b, c = map(int, input().split())
print(a + b > c and b + c > a and a + c > b)
#print(a + b + c - max(a, b, c) > max(a, b, c)

x = float(input())
print(0 <= x <= 2 or 10 <= x <= 20)