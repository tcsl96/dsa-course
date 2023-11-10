class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> bool:
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self) -> None | Node:
        if (self.length == 0):
            print("\nThe DLL is empty.")
            return None
        elif (self.length == 1):
            popped_node = self.tail
            self.clear()
            return popped_node
        else:
            popped_node = self.tail
            before = popped_node.prev
            before.next = None
            popped_node.prev = None
            self.tail = before
            self.length -= 1
            return popped_node

    def pop_first(self) -> None | Node:
        if (self.length == 0):
            print("\nThe DLL is empty.")
            return None
        elif (self.length == 1):
            popped_node = self.head
            self.clear()
            return popped_node
        else:
            popped_node = self.head
            self.head = popped_node.next 
            self.head.prev = None
            popped_node.next = None
            self.length -= 1
            return popped_node
    
    def get(self, index: int) -> None | Node:
        if (index < 0) or (index >= self.length):
            print("\nIndex Out of Range.")
            return None
        if (index*2 >= self.length):
            ref = self.tail
            for _ in range(self.length - index - 1):
                ref = ref.prev
        else:
            ref = self.head
            for _ in range(index):
                ref = ref.next
        return ref

    def set(self, index: int, value) -> bool:
        ref = self.get(index)
        if (ref is not None):
            ref.value = value
            return True
        return False

    def insert(self, index: int, value) -> bool:
        if (index < 0) or (index > self.length):
            print("\nIndex Out of Range.")
            return False
        if (index == 0):
            return self.prepend(value)
        elif (index == self.length):
            return self.append(value)
        else:
            new_node = Node(value)
            ref = self.get(index)
            before = ref.prev
            new_node.prev = before
            new_node.next = ref
            before.next = new_node
            ref.prev = new_node
            self.length += 1
            return True

    def remove(self, index: int) -> None | Node:
        if (index < 0) or (index >= self.length):
            print("\nIndex Out of Range.")
            return None
        if (index == 0):
            return self.pop_first()
        elif (index == self.length - 1):
            return self.pop()
        else:
            removed_node = self.get(index)
            before = removed_node.prev
            after = removed_node.next
            before.next = removed_node.next
            after.prev = removed_node.prev
            removed_node.prev = None
            removed_node.next = None
            self.length -= 1
            return removed_node

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_info(self) -> None:
        # Printing LL information.
        # Example output at "ll_out.txt".
        print("\nDLL INFO")
        print("-"*60)
        print("DLL Head: ", self.head)
        print("DLL Tail: ", self.tail)
        print("DLL Length: ", self.length)
        if (self.length == 0):
            print("-"*60)
            return None
        node_n = self.head
        for n in range(1, self.length + 1):
            print(f"Node {n} Value: {node_n.value}")
            print(f"Node {n} Prev: {node_n.prev}")
            print(f"Node {n} Next: {node_n.next}")
            node_n = node_n.next
        print("-"*60)

    # Leetcode Exercises.
    # By changing pointers.
    def swap_first_last_pointers(self) -> bool:
        if (self.length <= 1):
            return False
        elif (self.length == 2):
            self.head.prev = self.tail
            self.tail.next = self.head
            self.head.next = None
            self.tail.prev = None
            self.head = self.head.prev
            self.tail = self.tail.next
        else:
            after_first = self.head.next
            before_last = self.tail.prev
            after_first.prev = self.tail
            before_last.next = self.head
            self.head.prev = before_last
            self.head.next = None
            self.tail.prev = None
            self.tail.next = after_first
            self.head = after_first.prev
            self.tail = before_last.next
        return True
    
    # By changing values.
    def swap_first_last_value(self) -> bool:
        if (self.length <= 1):
            return False
        else:
            temp = self.head.value
            self.head.value = self.tail.value
            self.tail.value = temp
        return True

    def revert(self) -> None:
        ref = self.head
        self.head = self.tail
        self.tail = ref
        while (ref is not None):
            before = ref.prev
            ref.prev = ref.next
            ref.next = before
            before = ref
            ref = ref.prev

    def is_palindrome(self) -> bool:
        if (self.length > 1):
            forward = self.head
            backward = self.tail
            while (forward != backward):
                if (forward.value != backward.value):
                    return False
                forward = forward.next
                backward = backward.prev
        return True

    # TODO: Implement this method.
    def swap_pairs(self) -> None:
        pass
            
if __name__ == "__main__":
    pass