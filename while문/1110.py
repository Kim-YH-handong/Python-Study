a = int(input())
begin = a
count = 0

while True:
    count += 1
    second = int(a/10) + (a%10)
    first = a%10
    a = (first*10) + second%10
    if a == begin:
        break

print(count)