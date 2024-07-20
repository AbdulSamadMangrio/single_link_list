class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Slist:
    def __init__(self) -> None:
        self.count = 0
        self.head = None 
        self.tail = None
    
    def is_empty(self):
        return (self.head is None) or (self.count == 0)

    def insert_at_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1
    
    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def search(self, e):
        if not self.is_empty():
            x = self.head
            while x:
                if x.data == e:
                    return x
                x = x.next
        return None
            
    def show(self):
        if not self.is_empty():
            x = self.head
            while x:
                print(x.data)
                x = x.next
        else:
            return None
        
    def insert_after(self, per_node, data):
        if per_node is None:
            return None
        new_node = Node(data)
        new_node.next = per_node.next
        per_node.next = new_node
        if per_node == self.tail:
            self.tail = new_node
        self.count += 1

    def insert_after_value(self, value, data):
        per_node = self.search(value)
        if per_node is not None:
            self.insert_after(per_node, data)
         
    def delete_at_beginning(self):
        if self.is_empty():
            return None
        elif self.count == 1:
            self.head = None
            self.tail = None
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
        else:
            x = self.head
            while x.next != self.tail:
                x = x.next
            self.tail = x
            self.tail.next = None
        self.count -= 1
    
    def delete_at_specific_value(self, e):
        if self.is_empty():
            return None
        x = self.head
        if x.data == e:
            self.delete_at_beginning()
            return
        while x.next:
            if x.next.data == e:
                x.next = x.next.next
                self.count -= 1
                return 
            x = x.next
        return None

# Testing the Slist
s = Slist()
print(s.is_empty())  # True

s.insert_at_first(222)
s.insert_at_first(22332)
s.insert_at_first(2222)
s.insert_at_last("mao she she")
s.insert_at_last("ponka")
s.insert_at_first(2221434)

pervious_node = s.search("mao she she")
s.insert_after(pervious_node, "khushka")
s.insert_after_value(2222, 9990999)
s.delete_at_beginning()
s.delete_at_end()
s.delete_at_specific_value(22332)

s.show()
print(s.count)  # should reflect the correct count of elements






class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:  # LIFO
    def __init__(self) -> None:
        self.top = None
        self.count = 0
    
    def is_empty(self):
        return self.top is None
    
    def push(self, e):
        newnode = Node(e)
        if self.is_empty():
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
        self.count += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            self.count -= 1
            return popped_node.data

# Testing the Stack
s = Stack()
print(s.is_empty())  # True

s.push(33)
s.push("aljjflsd")
s.push("djfk")
s.push("Zaki")

print(s.pop())  # Zaki
print(s.pop())  # djfk
print(s.is_empty())  # False
print(s.pop())  # aljjflsd
print(s.pop())  # 33
print(s.is_empty())  # True
