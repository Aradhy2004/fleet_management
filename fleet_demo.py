from fleet_manager import FleetManager
from specialized_vehicles import ElectricCar, ElectricScooter


def run_demo():
    manager = FleetManager()

    manager.add_hub("Downtown")
    manager.add_hub("Airport")

    car = ElectricCar("CAR301", "Nissan Leaf", 80, 5)
    scooter = ElectricScooter("SCOOT401", "Ather 450X", 90, 30)

    manager.add_vehicle_to_hub("Downtown", car)
    manager.add_vehicle_to_hub("Airport", scooter)

    manager.display_hubs()


if __name__ == "__main__":
    run_demo()
