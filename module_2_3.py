my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_item = 0
while list_item <= len(my_list) - 1:
    if my_list[list_item] == 0:
        list_item = list_item + 1
        continue
    elif my_list[list_item] < 0:
        break
    print(my_list[list_item])
    list_item = list_item + 1