from abc import ABC, abstractmethod

from transfer_function import TransferFunction


class IController(ABC):
    def __init__(self, param):
        self._param = param

    @abstractmethod
    def run(self, input_signal):
        pass

    @abstractmethod
    def change_param(self, param):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._param})'


class ProportionalController(IController, TransferFunction):
    def __init__(self, param):
        super().__init__(param)

    def compute(self, error):
        return self._param * error

    def change_param(self, param):
        self._param = param

    def simulate(self, input_array):
        pass

    def run(self, input_array):
        pass


# class ControllerMethod:
#     @classmethod
#     def compute(cls, input_point, controller:IController):
#         if isinstance(controller, PController):
#             pass
#         elif isinstance(controller, DController):
#             pass
#         elif isinstance(controller, IntegralController):
#             pass
#
#     @classmethod
#     def simulation(cls, input_array, controller:IController):
#         if isinstance(controller, PController):
#             pass
#         elif isinstance(controller, DController):
#             pass
#         elif isinstance(controller, IntegralController):
#             pass
#
#     @classmethod
#     def adapt(cls, param, controller:IController):
#         if isinstance(controller, PController):
#             pass
#         elif isinstance(controller, DController):
#             pass
#         elif isinstance(controller, IntegralController):
#             pass


if __name__ == '__main__':
    controller = ProportionalController(5)
    print(controller)


