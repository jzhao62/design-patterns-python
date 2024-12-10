from __future__ import annotations
from abc import ABC, abstractmethod

from src.Factory.base import LogisticCenter, Courier


class Ship(Courier):
    def go(self):
        print("ship: weee~")
        return None


class Truck(Courier):
    def go(self):
        print("Truck: weee~!")
        return None


class FastTruck(Courier):
    def go(self):
        print("fast truck: WEE WEE WEE")
        return None


class FastShip(Courier):
    def go(self):
        print("fast ship: wee wee wee")
        return None


class SeaLogistics(LogisticCenter):

    def create_courier(self):
        return Ship("sea port")

    def create_fast_courier(self):
        return FastShip("sea port")


class LandLogistics(LogisticCenter):

    def create_courier(self):
        return Truck("caterpillar company")

    def create_fast_courier(self):
        return FastTruck("caterpillar company")


if __name__ == "__main__":
    seas_distribution_center = SeaLogistics()
    land_distribution_center = LandLogistics()

    seas_distribution_center.dispatch_delivery()
    land_distribution_center.dispatch_delivery()
    seas_distribution_center.dispatch_fast_delivery()
    land_distribution_center.dispatch_fast_delivery()
