expr_tree = ["*", "+", "-", "a", "b", "c", "d"]

# Breath-first (level order)

class LevelOrderIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration

        result = self._sequence[self._index]
        self._index += 1
        return result


# iterator = LevelOrderIterator(expr_tree)
# for element in iter(iterator):
#     print(element)


# Depth-first, pre-order traversal

def left_child(index):
    return 2 * index + 1

def right_child(index):
    return 2 * index + 2

def is_perfect_length(sequence):
    """True if sequence has length 2^n - 1, otherwise False."""
    n = len(sequence)
    return ((n + 1) & n == 0) and (n != 0)

class PreOrderIterator:
    def __init__(self, sequence):
        if not is_perfect_length(sequence):
            raise ValueError("Not a perfect binary tree with length 2^n - 1.")
        self._sequence = sequence
        self._stack = [0]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._stack) == 0:
            raise StopIteration

        index = self._stack.pop()
        result = self._sequence[index]

        if right_child(index) < len(self._sequence):
            self._stack.append(right_child(index))

        if left_child(index) < len(self._sequence):
            self._stack.append(left_child(index))

        return result


# iterator = PreOrderIterator(expr_tree)
# print(" ".join(iterator))


# In-order Traversal, Depth-first
