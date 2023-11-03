class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self):
        pass

    def pop(self):
        pass

    def insert(self, index):
        pass

    def remove(self, index):
        pass

if __name__ == "__main__":
    ll = LinkedList(3)
    print("LL Head: ", ll.head)
    print("LL Tail: ", ll.tail)
    print("LL Length: ", ll.length)
    print("Node 1 Value: ", ll.head.value)
    print("Node 1 Pointer: ", ll.head.next)

    ll.append(5)
    print("\n")
    print("LL Head: ", ll.head)
    print("LL Tail: ", ll.tail)
    print("LL Length: ", ll.length)
    print("Node 1 Value: ", ll.head.value)
    print("Node 1 Pointer: ", ll.head.next)
    print("Node 2 Value: ", ll.tail.value)
    print("Node 2 Pointer: ", ll.tail.next)

    ll.append(2)
    print("\n")
    print("LL Head: ", ll.head)
    print("LL Tail: ", ll.tail)
    print("LL Length: ", ll.length)
    print("Node 1 Value: ", ll.head.value)
    print("Node 1 Pointer: ", ll.head.next)
    print("Node 2 Value: ", ll.head.next.value)
    print("Node 2 Pointer: ", ll.head.next.next)
    print("Node 3 Value: ", ll.tail.value)
    print("Node 3 Pointer: ", ll.tail.next)