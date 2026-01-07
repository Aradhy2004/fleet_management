from vehicle import Vehicle


class ElectricCar(Vehicle):
    """
    Specialized vehicle: Electric Car
    """

    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance_km):
        return 5.0 + (0.50 * distance_km)


class ElectricScooter(Vehicle):
    """
    Specialized vehicle: Electric Scooter
    """

    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, minutes):
        return 1.0 + (0.15 * minutes)
