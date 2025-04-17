class A:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print(f"Hello from A, {self.name}")
        
class B(A):
        
    def greet(self):
        print(f"Hello from B, {self.name}")
        super().greet()

class C(A):    
    def greet(self):
        print(f"Hello from C, {self.name}")
        super().greet()

class D(B, C):        
    def greet(self):
        print(f"Hello from D, {self.name}")
        super().greet()
        
        
d= D("Frank")
d.greet()
