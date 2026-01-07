class Vehicle:
    """
    Represents a vehicle in the Eco-Ride fleet
    """

    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
