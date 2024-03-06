from functools import wraps

from linked_list import LinkedList


class PythonicLinkedList(LinkedList):

    def __iter__(self):

        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_generator()
    
    def __len__(self):

        length = 0
        for _ in self:
            length += 1
        
        return length
    
    def __getitem__(self, index):

        return list(self)[index]
    
    def __eq__(self, reference):

        if not isinstance(reference, PythonicLinkedList):
            return False

        if len(self) != len(reference):
            return False

        for value1, value2 in zip(self, reference):
            if value1 != value2:
                return False

        return True
    
    def add_multiple(function):
        
        @wraps(function)
        def wrapper(values, *args, **kwargs):
            for value in values:
                function(value, *args, **kwargs)

        return wrapper

    @add_multiple
    def insert_multiple(self, value):
        super().insert(value)
