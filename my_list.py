class List(object):
    """Linked list"""

    def __init__(self, value=None, next_=None):
        self._value = value
        self.prev = None
        if next_:
            self.next = next_.copy()
            self.next.prev = self
        else:
            self.next = None

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current != None:
            self.current, result = self.current.next, self.current._value
            return result
        else:
            raise StopIteration()

    def __reversed__(self):
        current = self
        while current.next:
            current = current.next
        while current:
            yield current._value
            current = current.prev

    def __add__(self, tail):
        result = self.copy()
        for item in tail:
            result.append(item)
        return result

    def copy(self):
        result = List()
        current = result
        prev = None
        for item in self:
            current._value = item
            current.prev = prev
            current.next = List()
            prev = current
            current = current.next
        prev.next = None
        return result

    def print(self):
        for item in self:
            print(item)

    def print_reversed(self):
        for item in reversed(self):
            print(item)

    def append(self, value):
        if self.next == None:
            self.next = List(value)
            self.next.prev = self
        else:
            self.next.append(value)

if __name__ == '__main__':
    # (1, (2, (3, None) ) )
    sample = List(1)
    sample += [10, 11, 12]
    sample += List(9, next_=List(5))
    sample.print()
    sample.print_reversed()
    print(list(sample))
    # for item in reversed(sample):
    #    print(item)
