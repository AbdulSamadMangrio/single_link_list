class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Single_Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return (self.head is None) or (self.count == 0)
    
    def insert_at_First(self, data):
        newnode = Node(data)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.count += 1

    def insert_at_last(self, data):
        newnode = Node(data)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def insert_at_After(self, pervious_node, data):
        if self.is_empty():
            return None
        else:
            newnode = Node(data)
            newnode.next = pervious_node.next
            pervious_node.next = newnode
        self.count += 1

    def insert_at_After_Value(self, value, data):
        if self.is_empty():
            return None
        else:
            newnode = Node(data)
            pervious_node = self.search(value)
            newnode.next = pervious_node.next
            pervious_node.next = newnode
        self.count += 1

    def search(self, e):
        if not self.is_empty():
            x = self.head
            while x:
                if x.data == e:
                    return x
                x = x.next
        else:
            return None

    def show(self):
        if not self.is_empty():
            x = self.head
            while x:
                print(x.data)
                x = x.next
            else:
                return None

    def delete_at_begining(self):
        if self.is_empty():
            return None
        elif self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            s = self.head
            self.head = self.head.next
            s = None
            self.count -= 1

    def delete_at_end(self):
        if self.is_empty():
            return None
        elif self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            x = self.head
            while x.next != self.tail:
                x = x.next
            self.tail = x
            self.tail.next = None
            self.count -= 1

    def delete_at_specific_value(self, e):
        x = self.head
        while x:
            if x.next.data == e:
                x.next = x.next.next
                self.count -= 1
                return
            x = x.next
        return None
    

slist = Single_Linked_List()
slist.is_empty()
slist.insert_at_First(111)
slist.insert_at_First(112)
slist.insert_at_First(113)
slist.insert_at_First(114)
slist.insert_at_First(115)
slist.insert_at_First(116)
slist.insert_at_First(117)
slist.insert_at_last(119)
slist.insert_at_last(220)
slist.insert_at_After_Value(113, 1120)
pervious_node = slist.search(115)
slist.insert_at_After(pervious_node, 118)
slist.delete_at_begining()
slist.delete_at_end()
slist.delete_at_specific_value(114)
slist.show()
slist.count 
