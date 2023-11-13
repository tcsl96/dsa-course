from utils import get_id

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    # Main methods.
    def __init__(self, value=None) -> None:
        if (value is not None):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.make_clear()

    def append(self, value) -> bool:
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self) -> None | Node:
        if (self.length == 0):
            print("\nThe LL is empty.")
            return None
        elif (self.length == 1):
            popped_node = self.tail
            self.make_clear()
        else:
            ref = self.head
            while (ref.next != self.tail):
                ref = ref.next
            popped_node = ref.next
            ref.next = None
            self.tail = ref
            self.length -= 1
        return popped_node

    def pop_first(self) -> None | Node:
        if (self.length == 0):
            print("\nThe LL is empty.")
            return None
        elif (self.length == 1):
            popped_node = self.head
            self.make_clear()
        else:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
            self.length -= 1
        return popped_node

    def get(self, index: int) -> None | Node:
        if (index < 0) or (index >= self.length):
            print("\nIndex Out of Range.")
            return None
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
            ref = self.get(index - 1)
            new_node.next = ref.next
            ref.next = new_node
            self.length += 1
            return True

    def remove(self, index: int) -> None | Node:
        if (index < 0) or (index >= self.length):
            print("\nIndex Out of Range.")
            return None
        if (index == 0):
            return self.pop_first()
        elif (index == (self.length - 1)):
            return self.pop()
        else:
            ref = self.get(index - 1)
            removed_node = ref.next
            ref.next = removed_node.next
            removed_node.next = None
            self.length -= 1
            return removed_node

    def make_clear(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def print_info(self) -> None:
        # Printing LL information.
        # Example output at "ll_out.txt".
        N_DASH = 100
        print("\n" + "-"*N_DASH + "\nLL Info" + "\n" + "-"*N_DASH)
        print(f"{'Head:':6}{get_id(self.head):<20}{'Tail:':7}{get_id(self.tail):<20}{'Length:':8}{self.length}")
        if (self.length == 0):
            print("-"*N_DASH)
            return None
        node_n = self.head
        for n in range(self.length):
            print(f"{'Node:':6}{n:<20}{'Value:':7}{node_n.value:<20}{'Id:':8}{get_id(node_n):<20}Next: {get_id(node_n.next)}")
            node_n = node_n.next
        print("-"*N_DASH)

    # Leetcode Exercises.
    def revert(self) -> None:
        ref = self.head
        self.head = self.tail
        self.tail = ref
        before = None
        while (ref is not None):
            after = ref.next
            ref.next = before
            before = ref
            ref = after

    def find_middle_node(self) -> None | Node:
        slow = self.head
        fast = self.head
        while (fast.next is not None) and (fast is not None):
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self) -> bool:
        """
        Floyd's cycle-finding algorithm, often referred to as the "tortoise and the hare" technique.
        """
        slow = self.head
        fast = self.head
        while (fast.next is not None) and (fast is not None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False

    def find_kth_from_end(self, index: int) -> None | Node:
        ref = self.head   
        after = self.head 
        for _ in range(index):
            if (after is None):
                return None
            after = after.next
        while (after is not None):
            ref = ref.next
            after = after.next
        return ref

    def partition_list(self, value) -> bool:
        if (self.length <= 1):
            return False
        dummy1 = Node(0)
        dummy2 = Node(0)
        next1 = dummy1
        next2 = dummy2
        ref = self.head
        while (ref is not None):
            if (ref.value < value):
                next1.next = ref
                next1 = ref
            else:
                next2.next = ref
                next2 = ref
            ref = ref.next
        next1.next = dummy2.next
        next2.next = None
        self.head = dummy1.next
        return True

    def remove_duplicates(self) -> None:
        nodes = {}
        ref = self.head
        before = None
        while (ref is not None):
            if (nodes.get(ref.value) is not None):
                before.next = ref.next
                ref.next = None
                ref = before.next
                self.length -= 1
            else:
                nodes[ref.value] = 0
                before = ref
                ref = ref.next

    def binary_to_decimal(self) -> None | int:
        if (self.length == 0):
            return None
        dec = 0
        ref = self.head
        for index in range(1, self.length + 1):
            dec += ref.value*2**(self.length - index)
            ref = ref.next
        return dec

    # TODO: Implement this method.
    def reverse_between(self, start_index: int, end_index: int) -> None:
        pass

if __name__ == "__main__":
    # Creating the linked list.
    print("Creating LL with node equals to 3.")
    ll = LinkedList(3)
    ll.print_info()

    # Applying the methods.
    print("\nAppending 5.")
    ll.append(5)
    ll.print_info()

    print("\nPrepending 1.")
    ll.prepend(1)
    ll.print_info()

    popped_node_1 = ll.pop()
    print(f"\nPopping last node.\nValue: {popped_node_1.value:<5}Next: {get_id(popped_node_1.next)}")
    ll.print_info()

    popped_node_2 = ll.pop_first()
    print(f"\nPopping first node.\nValue: {popped_node_2.value:<5}Next: {get_id(popped_node_2.next)}")
    ll.print_info()

    print(f"\nSetting value 9 to node of index 0.")
    ll.set(0, 9)
    ll.print_info()

    print("\nCleaning the LL.")
    ll.make_clear()
    ll.print_info()

    print("\nMethods pop, pop_first, remove, get and set in a empty LL.")
    ll.pop()
    ll.pop_first()
    ll.remove(0)
    ll.get(0)
    ll.set(0, 1)

    print("\nAppending some values to LL.")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.print_info()

    node_n = ll.get(2)
    print(f"\nGetting node at index 2.\nValue: {node_n.value:<5}Next: {get_id(node_n.next)}")

    print("\nInserting 25 at index 2.")
    ll.insert(2, 2.5)
    ll.print_info()

    removed_node = ll.remove(3)
    print(f"\nRemoving node at index 3.\nValue: {removed_node.value:<5}Next: {get_id(removed_node.next)}")
    ll.print_info()