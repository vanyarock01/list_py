

class ListIter:

    def __init__(self, list_):
        self.current = list_

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        res = self.current._value
        self.current = self.current._next
        return res


class List(object):
    """Linked list"""

    def __init__(self, value, next_=None):
        self._value = value
        self._next = next_

    def __iter__(self):
        return ListIter(self)

    def __next__(self):
        # Случай, когда список пустой
        if self._next == None and \
                self._value == None:
            raise StopIteration()

        if self.current != None:
            self.current, result = self.current._next, self.current._value
            return result
        else:
            raise StopIteration()

    def __reversed__(self):
        # Случай, когда список пустой
        if self._next == None and \
                self._value == None:
            return
        if self._next:
            yield from reversed(self._next)
        yield self._value

    def __add__(self, tail):
        result = List(list(self)[0])
        for item in list(self)[1:]:
            result.append(item)
        for item in tail:
            result.append(item)
        return result

    def print(self):
        print(list(self)[0], end='')
        for elem in list(self)[1:]:
            print(' ', elem, end='')
        print()

    def print_reversed(self):
        print(list(reversed(self))[0], end='')
        for elem in list(reversed(self))[1:]:
            print(' ', elem, end='')
        print()

    def append(self, value):
        # Случай, когда список пустой
        if self._next == None and \
                self._value == None:
            self._value = value
        # Cлучай, когда текущий узел является последним
        elif self._next == None:
            self._next = List(value)
        # Случай, когда текущий узел не является последним
        else:
            self._next.append(value)

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
