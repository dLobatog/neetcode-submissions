class Car:
    def __init__(self, speed, position):
        self.speed = speed
        self.position = position

    def hours_to_target(self, target: int) -> int:
        return (target-self.position) / self.speed # miles / (miles/h) = h



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleets = []
        time_to_beat = float('inf')
        for i in range(len(position)):
            cars.append(Car(speed[i], position[i]))
            time_to_beat = min(time_to_beat, cars[-1].hours_to_target(target))

        time_to_beat -= 1
        cars.sort(key=lambda x: x.position, reverse=True)
        fleets = 0
        for car in cars:
            if car.hours_to_target(target) > time_to_beat:
                fleets += 1
                time_to_beat = car.hours_to_target(target)

        return fleets

