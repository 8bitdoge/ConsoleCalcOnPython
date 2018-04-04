x = int(input("Первое число: "))
y = int(input("Второе число: "))
action = input('Выберите действие (+ - * ** /): ')

if action == "+":
    z = x + y
elif action == "-":
    z = x - y
elif action == "*":
    z = x * y
elif action == "**":
    z = x ** y
elif action == "/":
    if y == 0:
        z = "На ноль делить нельзя!"
    else:
        z = round(x / y, 2)
else:
    z = "Ошибка"
    
print(x, " ", action, " ", y, " = ", z)
