"""
Req
-------
enterance
exit
parking lot 
vehicale (2W or 4W)
ticket 
Prices based on hours 


Entites
------------
Vehicale (vehicale_Number , Price, Interface) --> 2W_Vehicale and 4w_Vehicale 
Ticket (vehicale, EntranceTime, Price)
ParkingManager(addSpot, RemoveSpot, IsEmpty, parkVehicale, RemoveVehicale, FindSpace) ---> 
PakringSpot(spotNumber, vehicaleType, isFree)
parkingStrategy (Interface) --> NearToEnrance , RandomSpot
ExistGate (UpdateParkingStatus, CalculatePrice)


"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Vehicale(ABC):
    def __init__(self, vehicale_number):
        self.vehicale_number  = vehicale_number 
    
    @abstractmethod 
    def get_type(self):
        pass 

    @abstractmethod 
    def get_price_per_hour(self):
        pass 

class TwoWheeler(Vehicale):
    def get_type(self):
        return "2W"
    
    def get_price_per_hour(self):
        return 10
    
class FourWheeler(Vehicale):
    def get_type(self):
        return "4W"
    
    def get_price_per_hour(self):
        return 20
    
class Ticket: 
    def __init__(self,  vehicale: Vehicale):
        self.enteranceTime = datetime.now() 
        self.vehicale = vehicale 
        self.price = 0 
        self.isActie = True 
    
    def close_ticket(self):
        self.exitTime = datetime.now()
        self.isActie = False 
        

class ExitGate:
    def __init__(self, vehicale: Vehicale, ticket: Ticket):
        self.vehicale = vehicale
        self.ticket = ticket 
    
    def calculate_price(self, ticket: Ticket):
        if ticket.isActie:
            time_diff = datetime.now() - ticket.enteranceTime
            hours_parked = time_diff.total_seconds() / 3600
            ticket.price = hours_parked * ticket.vehicale.get_price_per_hour()
            ticket.close_ticket()
            return ticket.price
        else:
            return ticket.price
        
    def update_parking_status(self, parking_manager, ticket: Ticket):
        parking_manager.remove_vehicale(ticket.vehicale)
        self.calculate_price(ticket)
        print(f"Vehicale {ticket.vehicale.vehicale_number} exited. Total price: {ticket.price}")


class ParkingSpot:
    def __init__(self, spot_number, vehicale_type):
        self.spot_number = spot_number
        self.vehicale_type = vehicale_type
        self.is_free = True
        self.current_vehicale = None 
    
    def park_vehicale(self, vehicale: Vehicale):
        if self.is_free and vehicale.get_type() == self.vehicale_type:
            self.current_vehicale = vehicale
            self.is_free = False
            return True
        return False
    
    def remove_vehicale(self):
        if not self.is_free:
            self.current_vehicale = None
            self.is_free = True
            return True
        return False
    
class ParkingManager:
    def __init__(self, parking_spots):
        self.parking_spots = parking_spots 
    
    def add_spot(self, spot: ParkingSpot):
        self.parking_spots.append(spot)
    
    def remove_spot(self, spot: ParkingSpot):
        self.parking_spots.remove(spot)
    
    def is_empty(self, vehicale_type):
        for spot in self.parking_spots:
            if spot.is_free and spot.vehicale_type == vehicale_type:
                return False
        return True
    
    def find_space(self, vehicale: Vehicale):
        for spot in self.parking_spots:
            if spot.is_free and spot.vehicale_type == vehicale.get_type():
                return spot
        return None
    
    def park_vehicale(self, vehicale: Vehicale):
        spot = self.find_space(vehicale)
        if spot:
            if spot.park_vehicale(vehicale):
                ticket = Ticket(vehicale)
                print(f"Vehicale {vehicale.vehicale_number} parked at spot {spot.spot_number}. Ticket issued.")
                return ticket
        print(f"No available spot for vehicale {vehicale.vehicale_number}.")
        return None
    
    def remove_vehicale(self, vehicale: Vehicale):
        for spot in self.parking_spots:
            if not spot.is_free and spot.current_vehicale.vehicale_number == vehicale.vehicale_number:
                spot.remove_vehicale()
                print(f"Vehicale {vehicale.vehicale_number} removed from spot {spot.spot_number}.")
                return True
        print(f"Vehicale {vehicale.vehicale_number} not found in parking lot.")
        return False
    



if __name__ == "__main__":
    ParkingLot = [] 
    for i in range(1, 6):
        ParkingLot.append(ParkingSpot(i, "2W"))

    for i in range(6, 11):
        ParkingLot.append(ParkingSpot(i, "4W"))

    parking_manager = ParkingManager(ParkingLot)