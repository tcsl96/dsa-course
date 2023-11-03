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

    def append(self, value) -> None:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value) -> None:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self) -> None:
        if self.length == 0:
            print("\nThe LL is empty.")
            return None
        elif self.length == 1:
            self.clear()
        else:
            node_n = self.head
            while (node_n.next != self.tail):
                node_n = node_n.next
            node_n.next = None
            self.tail = node_n
            self.length -= 1

    def insert(self, index) -> None:
        pass

    def remove(self, index) -> None:
        pass

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_info(self) -> None:
        # Printing LL information.
        # Example output at "ll_out.txt".
        print("\nLL INFO")
        print("-"*60)
        print("LL Head: ", self.head)
        print("LL Tail: ", self.tail)
        print("LL Length: ", self.length)
        if self.length == 0:
            print("-"*60)
            return
        node_n = self.head
        for n in range(1, self.length + 1):
            print(f"Node {n} Value: {node_n.value}")
            print(f"Node {n} Pointer: {node_n.next}")
            node_n = node_n.next
        print("-"*60)

if __name__ == "__main__":
    # Creating the linked list.
    ll = LinkedList(3)
    ll.print_info()

    # Applying the methods.
    ll.append(5)
    ll.print_info()

    ll.prepend(1)
    ll.print_info()

    ll.append(2)
    ll.print_info()

    ll.pop()
    ll.print_info()

    ll.clear()
    ll.print_info()

    ll.pop()