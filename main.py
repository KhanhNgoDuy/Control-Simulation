import numpy as np
import sympy

import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

from plant import Tank
from controller import ProportionalController


class Error:
    def __init__(self, maxsize=5):
        self.queue = []
        self.maxsize = maxsize
        self.std = None

    def update(self, val):
        if len(self.queue) >= self.maxsize:
            self.queue.pop(0)

        self.queue.append(val)
        self.std = np.std(self.queue)

    def __mul__(self, other):
        return self.queue[-1] * other


class System:
    def __init__(self, reference, tf, controller=1, feedback=1, sampling_time: float = None):
        self.__input = reference
        self.__error = Error()
        self.__controller = controller
        self.__feedback = feedback
        self.__sampling_time = sampling_time
        self.__tf = tf
        self._record = []

    def forward(self, error):
        self.__error.update(error * self.__feedback)
        control_signal = self.__error * self.__controller
        output_s = control_signal * self.__tf
        output_t = control_signal
        self._record.append(s)

    def is_stable(self):
        pass


def run(ref, g, transf_func=lambda s: g(s) / (1 + g(s))):
    result = np.empty(0)
    output = 0
    reference = 3

    k = 1
    i = 0

    system.forward()

    t = np.arange(len(result))
    plt.plot(t, result)
    plt.show()


if __name__ == '__main__':
    t, s = sympy.symbols('t, s')
    controller = ProportionalController(param=1)
    plant = Tank()
    system = System(controller=controller, plant=plant)

    ref = 3

