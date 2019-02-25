class List(object):
    """Linked list"""

    def __init__(self, value, next_=None):
        self._value = value
        self.next = next_
        self.current = self

    def __iter__(self):
        return self

    def __next__(self):
        if self.current != None:
            self.current, result = self.current.next, self.current._value
            return result
        else:
            raise StopIteration()

    def print(self):
        for item in self:
            print(item)

    def append(self, value):
        if self.next == None:
            self.next = List(value)
        else:
            self.next.append(value)

if __name__ == '__main__':
    ll = List(
        value=5, next_=List(
            value=1, next_=List(
                value=2, next_=List(
                    value=4, next_=List(
                        value=9)))))
    # ll.print()
    # ll.append(4)
    ll.append(9)
    ll.append(11)
    ll.print()
