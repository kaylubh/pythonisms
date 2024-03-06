class Node:
    """
    Instantiates a node with the input value.

    Attributes:
      value (any): value or data stored in node
      next (node object, default = None): next node in linked list

    Methods:
      __str__(): returns a string representation of value of node
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    """
    Instantiates a singly linked list.

    Attributes:
      head (node object, default = None): the head node in linked list

    Methods:
      __str__(): returns a string representation of values of nodes in linked list
      insert(value): no return, creates new node at head of linked list and assigns value attribute
      append(value): no return, creates new node at tail of linked list and assigns value attribute
      insert_before(target_node, new_value): no return, creates new node before target_node of linked list and assigns value attribute
      insert_after(target_node, new_value): no return, creates new node after target_node of linked list and assigns value attribute
      includes(value): returns True or False if input value exactly matches a node value in linked list
      kth_from_end(k): returns value of node k places from tail of linked list
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        linked_list_string = ''
        current_node = self.head

        while current_node:
            current_node_string = str(current_node)
            linked_list_string += f"{{ {current_node_string} }} -> "
            current_node = current_node.next

        linked_list_string += 'NULL'

        return linked_list_string

    def insert(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        current_node = self.head

        if current_node is not None:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

        else:
            self.head = new_node

    def insert_before(self, target_node, new_value):
        new_node = Node(new_value)
        current_node = self.head

        # raise exception if linked list is empty
        if current_node is None:
            raise TargetError("The linked list does not contain any nodes")

        # if head is target node
        if current_node.value == target_node:
            new_node.next = current_node
            self.head = new_node
            return

        # traverse linked list to find target node
        while current_node.next:
            if current_node.next.value == target_node:
                new_node.next = current_node.next
                current_node.next = new_node
                return

            else:
                current_node = current_node.next

        # raise exception if target not found
        raise TargetError("Target node not found in the linked list")

    def insert_after(self, target_node, new_value):
        new_node = Node(new_value)
        current_node = self.head

        # raise exception if linked list is empty
        if current_node is None:
            raise TargetError("The linked list does not contain any nodes")

        # traverse linked list to find target node
        while current_node:
            if current_node.value == target_node:
                new_node.next = current_node.next
                current_node.next = new_node
                return

            else:
                current_node = current_node.next

        # raise exception if target not found
        raise TargetError("Target node not found in the linked list")

    def includes(self, target_value):
        current_node = self.head

        while current_node:
            if current_node.value == target_value:
                return True
            current_node = current_node.next

        return False

    def kth_from_end(self, k):
        tail_pointer = self.head
        k_pointer = self.head

        # exceptions
        if tail_pointer is None: # linked list is empty
            raise TargetError("The linked list does not contain any nodes")
        if k < 0: # k is negative number
            raise TargetError("Cannot use a negative k-th value")

        # move tail pointer ahead "k" steps
        for _ in range(k):
            if tail_pointer.next:
                tail_pointer = tail_pointer.next
            else:
                raise TargetError("Out of range, k is larger than number of nodes in linked list")

        # traverse linked list with both pointers until end
        while tail_pointer.next:
            tail_pointer = tail_pointer.next
            k_pointer = k_pointer.next

        return k_pointer.value

class TargetError(Exception):
    pass
