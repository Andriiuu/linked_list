
from linked_list import LinkedList

def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    for i in range(list_to_replace.length()):
        if list_to_replace.value_at(i) == item_to_replace:
            list_to_replace.change_value_at(i,item_to_replace_with)
    return list_to_replace

def input_list():
    choice = 0
    while True:
        try:
            choice = int(input("1.Input list by keyboard\n2.Generate random list from a to b\n3.Exit\n"))
            if choice < 1 or choice > 3:
                print("Enter 1,2 or 3")
                continue

            my_list = LinkedList()
            if choice == 1:
                my_list.input_by_keyboard()
            if choice == 2:
                my_list.random_list()
            if choice == 3:
                return False

            my_list.show()
            print('------------------------------')
            my_list = replace_values(my_list, 0, 'ZERO')
            return my_list
        except ValueError:
            print("This is not an int type!")
            continue

def result_after_transformation(my_list):
    donttouch = LinkedList()
    i = 0
    while i < my_list.length():
        j = 0
        temp = 0
        while j < my_list.length():
            if my_list.value_at(i) == my_list.value_at(j):
                temp += 1
            j += 1
        if temp < 2:
            my_list.change_value_at(i, 0)
            donttouch.append(i)
        i += 1
    print(" ")
    print("1. Removing solo numbers...")
    list_cl = LinkedList()
    list_cl = replace_values(my_list, 'ZERO', 0)
    list_cl.show()

    i = 0
    while i < my_list.length():
        j = 0
        group = LinkedList()
        while j < my_list.length():
            if my_list.value_at(i) == my_list.value_at(j):
                if donttouch.count(j) == 0:
                    group.append(j)
                    donttouch.append(j)
            j += 1
        i += 1
        if group.length() != 0:
            my_list.change_value_at(group.value_at(0), 1)
            my_list.change_value_at(group.value_at(group.length()-1), 1)
            c = 1
            while c < group.length() - 1:
                my_list.change_value_at(group.value_at(c), 0)
                c += 1

    return my_list


list_c = LinkedList()
list_c = input_list()

if list_c != False:
    list_c = result_after_transformation(list_c)
    print('------------------------------')
    print(' ')
    print("2. First & last repeatable number changes to 1, all same numbers between them changes to 0...")
    list_c.show()
    print('------------------------------')
    print(' ')
    print("3. Counting 0 and 1...")
    print("Number '1' appears - " + str(list_c.count(1)) + "  times.")
    print("Number '0' appears - " + str(list_c.count(0)) + "  times.")
    print('------------------------------')