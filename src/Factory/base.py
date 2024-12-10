from abc import ABC, abstractmethod
from uuid import uuid4


class Courier(ABC):

    def __init__(self, manufacture=None):
        self.uuid = uuid4()
        self.remark = manufacture

    @abstractmethod
    def go(self):
        print("abstract method instance may define its own behavior")
        pass

    def get_description(self):
        return {"uuid": self.uuid, "manufacture": self.remark}


class LogisticCenter(ABC):
    @abstractmethod
    def create_courier(self) -> Courier:
        pass

    @abstractmethod
    def create_fast_courier(self) -> Courier:
        pass

    def dispatch_delivery(self):
        courier = self.create_courier()
        courier.go()
        print(
            f"Courier {courier.get_description()} is produced inside {self.__class__.__name__}. and has been "
            f"dispatched, it is polymorphic"
        )

    def dispatch_fast_delivery(self):
        courier = self.create_fast_courier()
        courier.go()
        print(
            f"Fast Courier {courier.get_description()} is produced inside {self.__class__.__name__}. and has been "
            f"dispatched, it is polymorphic"
        )
