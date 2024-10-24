class TracingMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print("TracingMeta.__prepare__")
        print(f" {mcs = }")
        print(f" {name = }")
        print(f" {bases = }")
        print(f" {kwargs = }")

        namespace = super().__prepare__(name, bases)
        print(f" -> {namespace = }")
        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs):
        print("TracingMeta.__new__")
        print(f" {mcs = }")
        print(f" {name = }")
        print(f" {bases = }")
        print(f" {namespace = }")
        print(f" {kwargs = }")

        cls = super().__new__(mcs, name, bases, namespace)
        print(f" -> {cls = }")
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        print("TracingMeta.__init__")
        print(f" {cls = }")
        print(f" {name = }")
        print(f" {bases = }")
        print(f" {namespace = }")
        print(f" {kwargs = }")

        super().__init__(name, bases, namespace)


class Widget(metaclass=TracingMeta):
    the_answer = 42

    def action(self, message):
        print(message)
