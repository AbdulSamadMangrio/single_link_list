class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Single_linked_list:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_first(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n

    def show(self):
        e = self.head
        while e:
            print(e.data)
            e = e.next

    def search(self, e):
        n = self.head
        while n:
            if n.data == e:
                return n
            n = n.next
        return None
    
    def insert_at_a_specific_position(self, position, e):
        newnode = Node(e)
        n = self.search(position)
        newnode.next = n.next
        n.next = newnode


List = Single_linked_list()
List.insert_at_first(999)
List.insert_at_first(888)
List.insert_at_first(777)
List.insert_at_first(666)
List.insert_at_first(444)
List.insert_at_first(333)
List.insert_at_first(222)
List.insert_at_a_specific_position(666, 555)
List.show()

result = List.search(444)
if result:
    print(f"Element {result.data} Found.....")
else:
    print(f"Element is Not Found.....")



class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Single_linked_list:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_first(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n

    def show(self):
        e = self.head
        while e:
            print(e.data)
            e = e.next

    def search(self, e):
        n = self.head
        while n:
            if n.data == e:
                return n
            n = n.next
        return None
    
    def insert_at_a_specific_position(self, position, e):
        newnode = Node(e)
        n = self.search(position)
        newnode.next = n.next
        n.next = newnode

List = Single_linked_list()
List.insert_at_first(999)
List.insert_at_first(888)
List.insert_at_first(777)
List.insert_at_first(555)
List.insert_at_first(444)
List.insert_at_first(333)
List.insert_at_first(222)
List.insert_at_first(111)
List.insert_at_a_specific_position(555, 666)
List.show()

result = List.search(555)
if result:
    print(f"Element {result.data} Found.....")
else:
    print(f"Element is Not Found....")




class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Single_linked_list:
    def __init__(self) -> None:
        self.head =  None
        self.tail = None

    def insert_at_end(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            n.next = self.tail
            self.tail = n

    def show(self):
        e = self.tail
        while e:
            print(e.data)
            e = e.next

    def search(self, e):
        n = self.tail
        while n:
            if n.data == e:
                return n
            n = n.next
        return None
    
    def insert_at_a_specific_position(self, position, e):
        newnode = Node(e)
        n = self.search(position)
        newnode.next = n.next
        n.next = newnode

List = Single_linked_list()

List.insert_at_end(111)
List.insert_at_end(222)
List.insert_at_end(333)
List.insert_at_end(444)
List.insert_at_end(666)
List.insert_at_end(777)
List.insert_at_end(888)
List.insert_at_end(999)
List.insert_at_a_specific_position(666, 555)
List.show()

result = List.search(555)
if result:
    print(f"Element {result.data} Found....")
else:
    print(f"Element is Not Found......")
