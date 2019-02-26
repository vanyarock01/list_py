import sys


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
        # Случай, когда список пустой
        if self.next == None and \
                self._value == None and self.prev == None:
            raise StopIteration()

        if self.current != None:
            self.current, result = self.current.next, self.current._value
            return result
        else:
            raise StopIteration()

    def __reversed__(self):
        # Случай, когда список пустой
        if self.next == None and \
                self._value == None and self.prev == None:
            return
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
        if prev:
            prev.next = None
        return result

    def print(self):
        for item in self:
            sys.stdout.write(str(item) + " ")
        sys.stdout.write("\n")

    def print_reversed(self):
        for item in reversed(self):
            sys.stdout.write(str(item) + " ")
        sys.stdout.write("\n")

    def append(self, value):
        # Случай, когда список пустой
        if self.next == None and \
                self._value == None and self.prev == None:
            self._value = value
        # Cлучай, когда текущий узел является последним
        elif self.next == None:
            self.next = List(value)
            self.next.prev = self
        # Случай, когда текущий узел не является последним
        else:
            self.next.append(value)

if __name__ == '__main__':
    list_ = List(
        value=1, next_=List(value=2, next_=List(value=3)))
    list_.print()  # output: 1 2 3

    list_.append(4)
    list_.print()  # output: 1 2 3 4

    tail = List(value=5, next_=List(value=6))
    list_ += tail  # shallow copy, see examples below
    list_.print()  # output: 1 2 3 4 5 6

    tail._value = 0
    tail.print()  # output: 0 6; element 5 in tail is changed
    # output: 1 2 3 4 5 6; element 5 in list_ is NOT
    # changed
    list_.print()

    list_ += [7, 8]
    list_.print()  # output: 1 2 3 4 5 6 7 8

    for elem in list_:
        print(2 ** elem)  # output: 2 4 8 16 32 64 128 256

    list_.print_reversed()  # output: 8 7 6 5 4 3 2 1
