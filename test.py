class A:
    def fun(self):
        print("A:")
        return

class B(A):
    pass
class C(A):
    def fun(self):
        print("C:")
        return
class D(B,C):
    pass
class access:
    def main():
        obj=D()
        return
access.main()