import sympy
from abc import ABC, abstractmethod


class TransferFunction(ABC):

    def __init__(self, tf):
        t, s = sympy.symbols('t, s')
        self.__domain = 's'
        self.__F = tf
        self.__f = sympy.inverse_laplace_transform(tf, s, t, noconds=True)
        self.__tf = tf

    def to_t_domain(self):
        self.__domain = 't'
        self.__tf = self.__f
        return self

    def to_s_domain(self):
        self.__domain = 's'
        self.__tf = self.__F
        return self

    def __mul__(self, other):
        if isinstance(other, TransferFunction):
            return TransferFunction(self.__F * other.__F)

        return TransferFunction(self.__tf * other)

    def __rmul__(self, other):
        if isinstance(other, TransferFunction):
            return TransferFunction(self.__F * other.__F)

        return TransferFunction(self.__tf * other)


if __name__ == '__main__':
    t, s = sympy.symbols('t, s')

    tf1 = TransferFunction(1/s)
    tf2 = TransferFunction(1/s)

    print(tf1 * 5.5)    # 5.5/s
    print(5.5 * tf1)    # 5.5/s
    print(tf1 * tf2)    # s**(-2)
    print('')

    tf1.to_t_domain()

    print(tf1 * tf2)
    print('')

    tf2.to_t_domain()

    print(tf1)          # Heaviside(t)
    print(tf2)          # Heaviside(t)
    print(tf1 * 5.5)    # Heaviside(t) * 5.5
    print(5.5 * tf1)    # Heaviside(t) * 5.5
    print('')

    tf3 = tf1 * tf2
    # tf3.to_t_domain()

    print(tf3.to_t_domain())    # t*Heaviside(t)


