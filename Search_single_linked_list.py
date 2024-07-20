class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

n1 = Node("Karachi")
n2 = Node([1, 2, 3, 4])
n3 = Node({"English":5})
n4 = Node(8)

n1.next= n2
n2.next = n3
n3.next = n4

print(n1.next.next.next.data)

