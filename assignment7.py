# 1-3
import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if change < 0:
            self.current_speed = max(0, self.current_speed + change)
        else:
            self.current_speed = min(self.maximum_speed, self.current_speed + change)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


new_car = Car("ABC-123", 142)
print("Registration Number:", new_car.registration_number)
print("Maximum Speed:", new_car.maximum_speed)
print("Current Speed:", new_car.current_speed)
print("Travelled Distance:", new_car.travelled_distance)


new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print("Current Speed:", new_car.current_speed)


new_car.accelerate(-200)
print("Final Speed:", new_car.current_speed)


car_list = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    registration_number = "ABC-" + str(i)
    car = Car(registration_number, max_speed)
    car_list.append(car)

race_ongoing = True
while race_ongoing:
    for car in car_list:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
    for car in car_list:
        if car.travelled_distance >= 10000:
            race_ongoing = False
            break


print("\nCar Race Results:")
print("{:<15} {:<15} {:<15} {:<15}".format("Registration", "Max Speed (km/h)", "Current Speed", "Travelled Distance"))
for car in car_list:
    print("{:<15} {:<15} {:<15} {:<15}".format(car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance))

# 4-6


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print("Invalid floor")
            return
        if floor == self.current_floor:
            print("Already on floor", floor)
            return

        if floor > self.current_floor:
            self.floor_up(floor)
        else:
            self.floor_down(floor)

    def floor_up(self, floor):
        while self.current_floor < floor:
            self.current_floor += 1
            print("Elevator is on floor", self.current_floor)

    def floor_down(self, floor):
        while self.current_floor > floor:
            self.current_floor -= 1
            print("Elevator is on floor", self.current_floor)


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for _ in range(num_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_num, destination_floor):
        if elevator_num < 0 or elevator_num >= len(self.elevators):
            print("Invalid elevator number")
            return
        elevator = self.elevators[elevator_num]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


building = Building(1, 10, 2)
building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.fire_alarm()


# 7
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance_traveled = 0

    def drive(self):
        self.distance_traveled += self.speed


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.speed += random.randint(-5, 5)
            car.drive()

    def print_status(self):
        print(f"{'Name':<15}{'Speed':<15}{'Distance':<15}")
        for car in self.cars:
            print(f"{car.name:<15}{car.speed:<15}{car.distance_traveled:<15}")

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False


cars = [Car(f"Car{i}", random.randint(100, 150)) for i in range(1, 11)]


grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars)


hours = 0
while not grand_demolition_derby.race_finished():
    grand_demolition_derby.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\nStatus after {hours} hours:")
        grand_demolition_derby.print_status()

print("\nRace finished! Final status:")
grand_demolition_derby.print_status()

