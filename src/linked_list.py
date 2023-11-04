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
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value) -> None:
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get(self, index: int) -> None | Node:
        if (index < 0) or (index >= self.length):
            print("\nThe LL is empty.")
            return None
        node_n = self.head
        for _ in range(index):
            node_n = node_n.next
        return node_n

    def set(self, index: int, value) -> None:
        node_n = self.get(index)
        if node_n is None:
            return None
        node_n.value = value

    def pop(self) -> None | Node:
        if (self.length == 0):
            print("\nThe LL is empty.")
            return None
        elif (self.length == 1):
            popped_node = self.tail
            self.clear()
            return popped_node
        else:
            node_n = self.head
            while (node_n.next != self.tail):
                node_n = node_n.next
            popped_node = node_n.next
            node_n.next = None
            self.tail = node_n
            self.length -= 1
            return popped_node

    def pop_first(self) -> None | Node:
        if (self.length == 0):
            print("\nThe LL is empty.")
            return None
        elif (self.length == 1):
            popped_node = self.head
            self.clear()
            return popped_node
        else:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node

    def insert(self, index: int) -> None:
        pass

    def remove(self, index: int) -> None:
        pass

    def clear(self) -> None:
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
        if (self.length == 0):
            print("-"*60)
            return None
        node_n = self.head
        for n in range(1, self.length + 1):
            print(f"Node {n} Value: {node_n.value}")
            print(f"Node {n} Pointer: {node_n.next}")
            node_n = node_n.next
        print("-"*60)

if __name__ == "__main__":
    # Creating the linked list.
    print("Creating LL with node equals to 3.")
    ll = LinkedList(3)
    ll.print_info()

    # Applying the methods.
    print("\nMethod = append\tValue = 5")
    ll.append(5)
    ll.print_info()

    print("\nMethod = prepend\tValue = 1")
    ll.prepend(1)
    ll.print_info()

    popped_node_1 = ll.pop()
    print(f"\nMethod = pop\tValue = {popped_node_1.value}\tNext = {popped_node_1.next}")
    ll.print_info()

    popped_node_2 = ll.pop_first()
    print(f"\nMethod = pop_first\tValue = {popped_node_2.value}\tNext = {popped_node_2.next}")
    ll.print_info()

    ll.set(0, 9)
    node_n = ll.get(0)
    print(f"\nMethods = set and get\tValue = {node_n.value}")
    ll.print_info()

    print("\nMethods = clear, get, set, pop and pop_first.")
    ll.clear()
    ll.get(0)
    ll.set(0, 1)
    ll.pop()
    ll.pop_first()
    ll.print_info()