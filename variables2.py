list = [1, 2, 3]
list.append(4)
list.remove(3)

print(list)

print(list[0])
print(list[-1])

if 2 in list:
    print("2 есть в списке")
else:
    print("2 нет в списке")

# lst_console = input("Введите список через пробел: ")
# numbers = lst_console.split(" ")
# print(numbers)

tup = (2, 4, 7)
print(tup)
print(tup[0])
print(tup[-1])

first, second, third = tup
print("1", first)
print("2", second)
print("3", third)

print(3 in tup)

eng_rus_dict = {
    "cat" : "кот",
    "car" : "машина"
}

print(eng_rus_dict)
print(eng_rus_dict["cat"])
eng_rus_dict["cat"] = "Кошка"
print(eng_rus_dict["cat"])

print("car" in eng_rus_dict)
print(eng_rus_dict.values())
print("кот" in eng_rus_dict.values())
print(eng_rus_dict.keys())

print(eng_rus_dict.items())

print(eng_rus_dict.get("brother", "(нет перевода)"))

set_from_list = set(list)
set_example = {1, 2, 3}
print(set_from_list)
print(set_example)

set_example.add(5)
set_example.remove(2)
print(set_example)
print(set_example - {3, 5})
print(set_example.union({6, 7}))
print(set_example == {1, 3, 5})

print(len("brat"))
print(len(list))
print(len(eng_rus_dict))
print(len(set_example))