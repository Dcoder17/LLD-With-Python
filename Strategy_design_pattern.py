from abc import ABC, abstractmethod

class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def speed(self) -> int:
        pass



class NormalDrive(DriveStrategy):
    def speed(self):
        return 50

    def drive(self):
        print("Driving normally on the road.")

class OffRoadDrive(DriveStrategy):
    def speed(self):
        return 200

    def drive(self):
        print("Driving off-road on rough terrain.")

class SportsDrive(DriveStrategy):
    def speed(self):
        return 400

    def drive(self):
        print("Driving fast in sports mode.")


class Vehicle:
    def __init__(self, drive_strategy: DriveStrategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()

    def set_drive_strategy(self, drive_strategy: DriveStrategy):
        """Change driving strategy at runtime"""
        self.drive_strategy = drive_strategy

    def DrivingSpeed(self):
        return self.drive_strategy.speed()



class Car(Vehicle):
    def __init__(self):
        super().__init__(NormalDrive())

class OffRoadCar(Vehicle):
    def __init__(self):
        super().__init__(OffRoadDrive())

class SportsCar(Vehicle):
    def __init__(self):
        super().__init__(SportsDrive())



if __name__ == "__main__":
    car = Car()
    car.drive()  # Driving normally on the road.

    sports_car = SportsCar()
    sports_car.drive()  # Driving fast in sports mode.

    # Changing strategy at runtime
    print("\n--- Changing Car's strategy at runtime ---")
    car.set_drive_strategy(OffRoadDrive())
    car.drive()  # Driving off-road on rough terrain.

    Off_RoadCar = OffRoadCar()
    Off_RoadCar.set_drive_strategy(SportsDrive())
    Off_RoadCar.drive()
    print(Off_RoadCar.DrivingSpeed())

