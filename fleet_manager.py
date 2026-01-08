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

        def add_vehicle_to_hub(self, hub_name, vehicle):
       
            if hub_name not in self.hubs:
                print(f"Hub '{hub_name}' does not exist.")
                return

        # UC7: Duplicate vehicle check using list comprehension
            if any(existing_vehicle == vehicle for existing_vehicle in self.hubs[hub_name]):
                print(f"Duplicate vehicle ID '{vehicle.vehicle_id}' not allowed in hub '{hub_name}'.")
                return

            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} added to hub '{hub_name}'.")


        def search_by_hub(self, hub_name):
            """
            return all vehicles in a given hub
            """

        return self.hubs.get(hub_name,[])
    
        def search_high_battery_vehicles(self,threshold = 80):
            """
            return vehicles with battery greater then threshold
            """
            all_vehicles = [
                vehicle
                for vehicles in self.hubs.values()
                for vehicle in vehicles
            ]

            return list(
                filter(
                    lambda v: v.get_battery_percentage() > threshold,
                    all_vehicles

                )
    
            )
