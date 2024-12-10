from abc import ABC, abstractmethod
from typing import Type

from src.Factory.base import Courier, LogisticCenter


class Ship(Courier):
    def go(self):
        print("ship: weee~")
        return None


class Truck(Courier):
    def go(self):
        print("Truck: weee~!")
        return None


class SeaLogistics(LogisticCenter):
    def create_courier(self) -> Ship:
        return Ship("sea port")

    def create_fast_courier(self) -> Ship:
        raise "not in this scope, fast ship not supported"


class RoadLogistics(LogisticCenter):

    def create_courier(self) -> Truck:
        return Truck("caterpillar company")

    def create_fast_courier(self) -> Truck:
        raise "not in this scope fast truck not supported"


if __name__ == "__main__":
    seas_distribution_center = SeaLogistics()
    land_distribution_center = RoadLogistics()

    seas_distribution_center.dispatch_delivery()
    land_distribution_center.dispatch_delivery()
