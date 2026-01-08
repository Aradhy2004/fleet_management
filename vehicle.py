from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Abstract base class for all vehicle types in Eco-Ride
    """

    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model

        # UC2: Encapsulation & Security
        self.__battery_percentage = None
        self.__maintenance_status = "Available"
        self.__rental_price = 0.0

        self.set_battery_percentage(battery_percentage)

    # ---------- Battery Percentage ----------
    def get_battery_percentage(self):
        return self.__battery_percentage

    def set_battery_percentage(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    # ---------- Maintenance Status ----------
    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    # ---------- Rental Price ----------
    def get_rental_price(self):
        return self.__rental_price

    def set_rental_price(self, price):
        if price >= 0:
            self.__rental_price = price
        else:
            raise ValueError("Rental price cannot be negative")

    # ---------- UC4: Abstraction ----------
    @abstractmethod
    def calculate_trip_cost(self, value):
        """
        Calculate trip cost based on distance or time.
        Must be implemented by all subclasses.
        """
        pass

        def __eq__(self, other):
            if isinstance(other, Vehicle):
                return self.vehicle_id == other.vehicle_id
        return False
        def __str__(self):
            return (
                f"ID: {self.vehicle_id}, "
                f"Model: {self.model}, "
                f"Battery: {self.get_battery_percentage()}%, "
                f"Status: {self.get_maintenance_status()}"
            )

