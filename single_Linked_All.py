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
    
# 1. **Insertion:**
#    - Insert at the beginning
#    - Insert at the end
#    - Insert at a specific position

    def insert_at_First(self, data):
        newnode = Node(data)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.count += 1

    def show(self):
        if not self.is_empty():
            x = self.head
            while x:
                print(x.data)
                x = x.next
            else:
                return None
            
    def insert_at_Last(self, data):
        newnode = Node(data)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.count += 1

    def insert_at_after(self, previous_node, data):
        if self.is_empty():
            return None
        else:
            newnode = Node(data)
            newnode.next = previous_node.next
            previous_node.next = newnode
        self.count += 1

    def insert_at_After_Value(self, value, data):
        if self.is_empty():
            return None
        else:
            newnode = Node(data)
            previous_node = self.search(value)
            newnode.next = previous_node.next
            previous_node.next = newnode

# 4. **Search:**
#    - Search by value

    def search(self, e):
        if not self.is_empty():
            x = self.head
            while x:
                if x.data == e:
                    return x
                x = x.next
        else:
            return None

# 2. **Deletion:**
#    - Delete from the beginning
#    - Delete from the end
#    - Delete from a specific position
#    - Delete by value

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

    def delete_at_End(self):
        if self.is_empty():
            return None
        elif self.count == 1:
            self.head = None
            self.tail = None
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
                return x
            x = x.next
        return None
            


Slist = Single_Linked_List()
Slist.is_empty()
Slist.insert_at_First(111)
Slist.insert_at_First(222)
Slist.insert_at_First(333)
Slist.insert_at_First(444)
Slist.insert_at_First(555)
Slist.insert_at_Last(666)
Slist.insert_at_Last(555)
Slist.insert_at_Last(444)
Slist.insert_at_Last(333)
Slist.insert_at_Last(222)
Slist.insert_at_Last(111)
Slist.delete_at_begining()
Slist.delete_at_End()
Slist.insert_at_After_Value(444, 5685)
previous_nod = Slist.search(333)
Slist.insert_at_after(previous_nod, 2323)
Slist.delete_at_specific_value(333)
Slist.show()
Slist.count

