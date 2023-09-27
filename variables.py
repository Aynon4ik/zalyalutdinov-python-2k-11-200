name = input("Введите имя: ")
age = float(input("Введите возраст: "))
is_working_now = input("Работает сейчас? (1 или 0) ") == "1"
workplace = None

if is_working_now:
    workplace = input("Место работы: ")

if is_working_now and not workplace:
    print("не заполнено место работы!")
#одно и тоже, но не нужно будет менять на str, например
# print("Имя: " + name)
# print("Возраст: " + str(age))
# print("Работает сейчас: " + str(is_working_now))
print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Работает сейчас: {is_working_now}")
if is_working_now:
    print("Место работы: " + workplace)

if age >= 20:
    print("Пользователю больше 20 лет")
elif age >= 18:
    print("Совершеннолетний")
else:
    print("Несовершеннолетний")

str_template = "Информация о пользователе: {0} - {1}"
print(str_template.format(name, age))

print(name.upper())
print(name.lower())
print(name.find("а"))
print(name.replace("я", "ян"))


a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(5 // a)