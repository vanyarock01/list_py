# list_py
Реализация связного списка на языке python

```python
list_ = List(value=1, next_=List(value=2, next_=List(value=3)))
list_.print() # output: 1 2 3
list_.append(4)
list_.print() # output: 1 2 3 4
tail = List(value=5, next_=List(value=6))
list_ += tail # shallow copy, see examples below
list_.print() # output: 1 2 3 4 5 6
tail._value = 0
tail.print() # output: 0 6; element 5 in tail is changed
list_.print() # output: 1 2 3 4 5 6; element 5 in list_ is NOT changed
list_ += [7, 8]
list_.print() # output: 1 2 3 4 5 6 7 8
for elem in list_:
  print(2 ** elem) # output: 2 4 8 16 32 64 128 256
list_.print_reversed() # output: 8 7 6 5 4 3 2 1
```
