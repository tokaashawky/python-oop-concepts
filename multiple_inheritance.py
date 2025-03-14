class A:
    def show(self): print("A")

class B(A):
    def show(self): print("B")

class C(A):
    def show(self): print("C")

class D(B, C):
    pass

d = D()
d.show()  # Output: B (follows MRO: D → B → C → A)
print(D.__mro__)  # (D, B, C, A, object)