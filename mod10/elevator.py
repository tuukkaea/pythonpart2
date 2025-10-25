class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def move_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Hissi liikkui ylös. Kerros: {self.current_floor}")
        else:
            print("Hissi on jo ylimmässä")

    def move_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Hissi liikkui alas. Kerros: {self.current_floor}")
        else:
            print("Hissi on jo alimmassa kerroksessa")



    def move_to_floor(self, target):
        print(f"\n Siirrytään kerrokseen {target}")
        while self.current_floor < target:
            self.move_up()
        while self.current_floor > target:
            self.move_down()
        print(f"Ollaan kerroksessa {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range (num_elevators)]

    def use_elevator(self, elevator_num, target_floor):
        if elevator_num < 1 or elevator_num > len(self.elevators):
            return
        elevator = self.elevators[elevator_num -1]
        elevator.move_to_floor(target_floor)

    def fire_alarm(self):
        print("\nPalohälytys!")
        for i, elevator in enumerate(self.elevators, start=1):
            elevator.move_to_floor(self.bottom_floor)


def main():
    building = Building(1, 10, 3)

    building.use_elevator(1, 7)

    building.use_elevator(1, 4)

    building.fire_alarm()



main()