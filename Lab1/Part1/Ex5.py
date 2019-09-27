T = (1, 2, 3, 4) # A 4-item tuple
len(T) # Length
T + (5, 6) # Concatenation
T[0] # Indexing, slicing, and more
T.index(4) # Tuple methods: 4 appears at offset 3
T.count(4) # 4 appears once
T[0] = 2 # Tuples are immutable
...error text omitted...
TypeError: 'tuple' object does not support item assignment
T = (2,) + T[1:] # Make a new tuple for a new value
T
T = 'spam', 3.0, [11, 22, 33]
T[1]
T[2][1] 
