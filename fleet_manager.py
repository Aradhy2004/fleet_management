class FleetManager:
    """
    Manages fleet hubs and vehicles in the Eco-Ride system
    """

    def __init__(self):
        # Dictionary: hub_name -> list of vehicles
        self.hubs = {}

    def add_hub(self, hub_name):
        """
        Add a new fleet hub
        """
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added successfully.")
        else:
            print(f"Hub '{hub_name}' already exists.")

    def add_vehicle_to_hub(self, hub_name, vehicle):
        """
        Add a vehicle to an existing hub
        """
        if hub_name in self.hubs:
            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} added to hub '{hub_name}'.")
        else:
            print(f"Hub '{hub_name}' does not exist.")

    def display_hubs(self):
        """
        Display all hubs and their vehicles
        """
        for hub_name, vehicles in self.hubs.items():
            print(f"\nHub: {hub_name}")
            if not vehicles:
                print("  No vehicles available.")
            for vehicle in vehicles:
                print(f"  - {vehicle.vehicle_id} ({vehicle.model})")
