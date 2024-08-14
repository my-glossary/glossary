class A:

    x = 'a'


class B(A):

    x = 'b'


class C(B):

    x = 'c'


class D(C):

    x = 'c'

    def super_x_of_a(self):
        return super(B, self).x

    def super_x_of_b(self):
        return super(C, self).x

    def super_x_of_c(self):
        return super().x
