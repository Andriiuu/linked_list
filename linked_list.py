from node import Node
import random

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        cur_node = self.head        # cur = current node
        if cur_node == None:        # if new list [] head = None
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + " "
            cur_node = cur_node.get_next()
        print(output)

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node != None:
            count += 1
            cur_node = cur_node.get_next()
        return count
    def push_front(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()

    def count(self,data):
        cur_node = self.head
        count = 0
        while cur_node != None:
            if data == cur_node.get_data():
                count += 1
            cur_node = cur_node.get_next()
        return count

    def value_at(self,index):
        cur_node = self.head
        count = 0
        while cur_node != None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()
        print("The index is out of range")

    def change_value_at(self,index,data):
        cur_node = self.head
        count = 0
        while cur_node != None:
            if count == index:
                return cur_node.set_data(data)
            count += 1
            cur_node = cur_node.get_next()
        print("The index is out of range")

    def insert(self,index,data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0:                #Add to head
                self.push_front(data)
                return
            elif count + 1 == index:
                the_node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count +=1
            cur_node = cur_node.get_next()
        print("Index is out of range")


        def insert(self, index, data):
            new_node = Node(data)
            cur_node = self.head
            count = 0
            while cur_node.get_next() != None:
                if index == 0:  # Add to head
                    self.push_front(data)
                    return
                elif count + 1 == index:
                    the_node_after_cur = cur_node.get_next()
                    cur_node.set_next(new_node)
                    new_node.set_next(the_node_after_cur)
                    return
                count += 1
                cur_node = cur_node.get_next()
            print("Index is out of range")

    def remove(self,index):
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                the_node_to_remove = cur_node.get_next()
                the_node_after_removed = the_node_to_remove.get_next()
                cur_node.set_next(the_node_after_removed)
                return
            count +=1
            cur_node = cur_node.get_next()
        print("Index is out of range")


    def input_by_keyboard(self):
        while True:
            try:
                n = int(input("Enter size of list : "))
                if not isinstance(n,int):
                    print("Size must be int value!")
                    continue
                i = 1
                while n >= i:
                    to_add = int(input("Enter " + str(i) + " digit : "))
                    self.append(to_add)
                    i += 1
                return
            except ValueError:
                print("This is not an int type!")
                continue

    def random_list(self):
        while True:
            try:
                n = int(input("Enter size of list : "))
                if not isinstance(n, int):
                    print("Size must be int value!")
                    continue

                print("Enter range [a,b]")
                a = int(input("Enter a : "))
                b = int(input("Enter b : "))
                if b < a:
                    print("'b' must be bigger than a")

                i = 0
                while n >= i:
                    to_add = random.randint(a, b)
                    self.append(to_add)
                    i += 1
                return
            except ValueError:
                print("This is not an int type!")
                continue

