class X:
    def __new__(cls):
        return int(42)

    def __init__(self):
        self.value = 42

    def multiply_value(self, multiplier):
        return self.value * multiplier


x = X()

result = x.multiply_value(2)
# X.multiply_value(x, 2)
print(result)