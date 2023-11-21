from utils import get_id

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # Main Methods.
    def __init__(self, value=None) -> None:
        if (value is not None):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.make_clean()

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
            self.make_clean()
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
            self.make_clean()
        else:
            popped_node = self.head
            self.head = popped_node.next 
            self.head.prev = None
            popped_node.next = None
            self.length -= 1
        return popped_node
    
    def get(self, index: int) -> None | Node:
        if (index < 0) or (index >= self.length):
            print("\nIndex out of range.")
            return None
        elif (index*2 >= self.length):
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
            print("\nIndex out of range.")
            return False
        elif (index == 0):
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
            print("\nIndex out of range.")
            return None
        elif (index == 0):
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

    def make_clean(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def print_info(self) -> None:
        # Printing LL information.
        # Example output at "ll_out.txt".
        N_DASH = 126
        print("\n" + "-"*N_DASH + "\nDLL Info" + "\n" + "-"*N_DASH)
        print(f"Head: {get_id(self.head):<20}{'Tail:':7}{get_id(self.tail):<20}{'Length:':8}{self.length}")
        if (self.length == 0):
            print("-"*N_DASH)
            return None
        node_n = self.head
        for n in range(self.length):
            print(f"Node: {n:<20}{'Value:':7}{node_n.value:<20}{'Id:':8}{get_id(node_n):<20}Prev: {get_id(node_n.prev):<20}Next: {get_id(node_n.next)}")
            node_n = node_n.next
        print("-"*N_DASH)

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

    def swap_pairs(self) -> None:
        # Checking if the doubly linked list has less than two nodes.
        # In this situation, there no way to swap nodes.
        if (self.length < 2):
            return None
        
        # Defining the pointers. ref is pointing to the head, 
        # before is pointing to the node before ref,
        # and after is pointing to the node after ref.
        ref = self.head
        before = ref.prev
        after = ref.next

        # Adjusting the head of the doubly linked list.
        self.head = after

        while ((ref is not None) and (after is not None)):
            # Adjusting the next pointer of before node before swaping nodes.
            # After swap, it should be pointing to after node.
            # Ex.: (1) <-> (2) <-> (3)
            #       B       R       A
            # After swaping nodes 2 and 3, next pointer of node 1 should be pointing to node 3.
            if (before is not None):
                before.next = after

            # Swaping the nodes.
            ref.next = after.next
            after.prev = ref.prev
            ref.prev = after
            after.next = ref

            # Moving the pointers.
            before = ref
            ref = ref.next
            if (ref is not None):
                after = ref.next

                # Adjusting the prev pointer of the ref node after swaping nodes and moving pointers.
                # After this, it should be pointing to before node.
                # Ex.: (1) <-> (2) <-> (3) <-> (4) <-> (5)
                #       B       R       A
                #      (1) <-> (3) <-> (2) <-> (4) <-> (5)
                #       B       A       R
                # After swap nodes 2 and 3 and move the pointers,
                # prev pointer of node 4 will be pointing to node 3,
                # but it should be pointing to node 2.
                #      (1) <-> (3) <-> (2) <-> (4) <-> (5)
                #                       B       R       A
                ref.prev = before

        # Adjusting the tail of the doubly linked list.
        if (ref is None):
            self.tail = before
            
if __name__ == "__main__":
    # Creating the doubly linked list.
    print("Creating DLL with node equals to 3.")
    dll = DoublyLinkedList(3)
    dll.print_info()

    # Applying the methods.
    print("\nAppending 5.")
    dll.append(5)
    dll.print_info()

    print("\nPrepending 1.")
    dll.prepend(1)
    dll.print_info()

    popped_node_1 = dll.pop()
    print(f"\nPopping last node.\nValue: {popped_node_1.value:<5}Next: {get_id(popped_node_1.next):<20}Prev: {get_id(popped_node_1.prev)}")
    dll.print_info()

    popped_node_2 = dll.pop_first()
    print(f"\nPopping first node.\nValue: {popped_node_2.value:<5}Next: {get_id(popped_node_2.next):<20}Prev: {get_id(popped_node_2.prev)}")
    dll.print_info()

    print(f"\nSetting value 9 to node of index 0.")
    dll.set(0, 9)
    dll.print_info()

    print("\nCleaning the DLL.")
    dll.make_clean()
    dll.print_info()

    print("\nMethods pop, pop_first, remove, get and set in an empty DLL.")
    dll.pop()
    dll.pop_first()
    dll.remove(0)
    dll.get(0)
    dll.set(0, 1)

    print("\nAppending some values to DLL.")
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.print_info()

    node_n = dll.get(2)
    print(f"\nGetting node at index 2.\nValue: {node_n.value:<5}Next: {get_id(node_n.next):<20}Prev: {get_id(node_n.prev)}")

    print("\nInserting 25 at index 2.")
    dll.insert(2, 2.5)
    dll.print_info()

    removed_node = dll.remove(3)
    print(f"\nRemoving node at index 3.\nValue: {removed_node.value:<5}Next: {get_id(removed_node.next):<20}Prev: {get_id(removed_node.prev)}")
    dll.print_info()