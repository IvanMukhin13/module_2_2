
first = int(input('Первое число '))
second = int(input('Второе число '))
third = int(input('Третье число '))
if first == second and second == third:
    print("3")
elif first == second != third or first != second == third or first == third != second:
    print("2")
else:
    print('0')
