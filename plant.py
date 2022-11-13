from abc import ABC, abstractmethod


class IPlant(ABC):
    @abstractmethod
    def compute(self, input_point):
        pass


class Tank(IPlant):
    def __init__(self):
        self.__sum = 0

    def compute(self, input_point):
        self.__sum += input_point
        return self.__sum
