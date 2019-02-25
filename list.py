class List(object):
    """Linked list"""

    def __init__(self, value, next_=None):
        self._value = value
        self.next = next_

    def print(self):
        print(self._value)
        if self.next:
            self.next.print()


if __name__ == '__main__':
    ll = List(value=5, next_=List(value=1))
    ll.print()
