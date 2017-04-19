my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if i == 3:
        print("Item found")
        break
    print(i)
else:
    print("Item not found")