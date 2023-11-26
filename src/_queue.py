from out.utils import get_id

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue:
    # Main methods.
    def __init__(self, value=None) -> None:
        if (value is not None):
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.make_clean()

    def enqueue(self, value) -> None:
        new_node = Node(value)
        if (self.length == 0):
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self) -> None | Node:
        if (self.length == 0):
            print("\nThe Queue is empty.")
            return None
        elif (self.length == 1):
            popped_node = self.first
            self.make_clean()
        else:    
            popped_node = self.first
            self.first = popped_node.next
            popped_node.next = None
            self.length -= 1
        return popped_node
    
    def make_clean(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def print_info(self) -> None:
        # Printing Queue information.
        # Example output at "out/queue.txt".
        N_DASH = 101
        print("\n" + "-"*N_DASH + "\nQueue Info" + "\n" + "-"*N_DASH)
        print(f"{'First:':7}{get_id(self.first):<20}{'Last:':7}{get_id(self.last):<20}{'Length:':8}{self.length}")
        if (self.length == 0):
            print("-"*N_DASH)
            return None
        node_n = self.first
        for n in range(self.length):
            print(f"{'Node:':7}{n:<20}{'Value:':7}{node_n.value:<20}{'Id:':8}{get_id(node_n):<20}Next: {get_id(node_n.next)}")
            node_n = node_n.next
        print("-"*N_DASH)

if __name__ == "__main__":
    pass