# creating class A
class A:
    def decorators(func):
        def inner(self):
            print('Decoration started.')
            func(self)
            print('Decoration of function completed.\n')

        return inner

    @decorators
    def fun1(self):
        print('Decorating - Class A methods.')


# creating class B
class B(A):
    @A.decorators
    def fun2(self):
        print('Decoration - Class B methods.')


obj = B()
obj.fun1()
obj.fun2()
