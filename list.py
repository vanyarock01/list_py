class List(object):
    """Linked list"""

    def __init__(self, value=None, next_=None):
        self._value = value
        self.next = next_.copy() if next_ else next_

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current != None:
            self.current, result = self.current.next, self.current._value
            return result
        else:
            raise StopIteration()

    def __add__(self, tail):
        result = self.copy()
        for item in tail:
            result.append(item)
        return result

    def copy(self):
        result = List()
        curr = result
        prev = result
        for item in self:
            curr._value = item
            curr.next = List()
            prev = curr
            curr = curr.next
        prev.next = None
        return result

    def print(self):
        for item in self:
            print(item)

    def append(self, value):
        if self.next == None:
            self.next = List(value)
        else:
            self.next.append(value)

if __name__ == '__main__':
    # (1, (2, (3, None) ) )
