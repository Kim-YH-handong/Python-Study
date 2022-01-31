input = int(input())

if input >= 90:
    print('A')
elif input >= 80 and input < 90:
    print('B')
elif input >= 70 and input < 80:
    print('C')
elif input >= 60 and input < 70:
    print('D')
else:
    print('F')