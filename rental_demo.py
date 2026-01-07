from specialized_vehicles import ElectricCar, ElectricScooter


def run_demo():
    vehicles = [
        ElectricCar("CAR101", "Tesla Model 3", 85, 5),
        ElectricScooter("SCOOT201", "Xiaomi Pro", 70, 25)
    ]

    for vehicle in vehicles:
        cost = vehicle.calculate_trip_cost(10)
        print(f"{vehicle.model} trip cost: ${cost:.2f}")


if __name__ == "__main__":
    run_demo()
