class A:
    def magic(self):
        print('Class A')


class B(A):
    def magic(self):
        print('Class B')


class C(B):
    def magic(self):
        print('Class C')


class X(C, A):
    pass


class Y(A, C):
    pass


print(X.__mro__) # to działa
print(Y.__mro__) # to już nie, nie da się utworzyć drzewka!
