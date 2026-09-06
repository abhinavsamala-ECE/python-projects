# Python Collection Types

## List
Ordered, mutable collection of items. Allows duplicates and indexing.
```python
my_list = [1, 2, 3, 2]
```

## Tuple
Ordered, immutable collection of items. Allows duplicates but cannot be changed after creation.
```python
my_tuple = (1, 2, 3, 2)
```

## Set
Unordered, mutable collection of unique items. No duplicates allowed.
```python
my_set = {1, 2, 3}
```

## Dictionary
Unordered, mutable collection of key-value pairs. Keys must be unique.
```python
my_dict = {'a': 1, 'b': 2}
```

## Key Differences

| Type | Ordered | Mutable | Duplicates | Indexable |
|------|---------|---------|-----------|-----------|
| List | ✓ | ✓ | ✓ | ✓ |
| Tuple | ✓ | ✗ | ✓ | ✓ |
| Set | ✗ | ✓ | ✗ | ✗ |
| Dictionary | ✗ | ✓ | ✗ (keys) | ✓ (keys) |