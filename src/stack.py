from out.utils import get_id

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    # Main methods.
    def __init__(self, value=None) -> None:
        if (value is not None):
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            self.make_clean()

    def push(self, value) -> None:
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self) -> None | Node:
        if (self.height == 0):
            print("\nThe Stack is empty.")
            return None
        popped_node = self.top
        self.top = popped_node.next
        popped_node.next = None
        self.height -= 1
        return popped_node
    
    def make_clean(self) -> None:
        self.top = None
        self.height = 0

    def print_info(self) -> None:
        # Printing Stack information.
        # Example output at "out/stack.txt".
        N_DASH = 97
        print("\n" + "-"*N_DASH + "\nStack Info" + "\n" + "-"*N_DASH)
        print(f"{'Top:':6}{get_id(self.top):<20}{'Height:':8}{get_id(self.height)}")
        if (self.height == 0):
            print("-"*N_DASH)
            return None
        node_n = self.top
        for n in range(self.height, 0, -1):
            print(f"{'Node:':6}{n:<20}{'Value:':8}{get_id(node_n.value):<20}Id: {get_id(node_n):<20}Next: {get_id(node_n.next)}")
            node_n = node_n.next
        print("-"*N_DASH)

if __name__ == "__main__":
    pass