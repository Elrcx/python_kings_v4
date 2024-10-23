class X:
    def __init__(self, value: str):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not (2 < len(value) < 10):
            raise ValueError("Value must be between 1 and 10")
        self._value = value


x = X('Amelinium')
print(x.value)
x.value = "Tego nie pomalujesz!"
#print(x.value)
