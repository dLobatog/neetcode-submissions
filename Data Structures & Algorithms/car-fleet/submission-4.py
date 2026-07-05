class Car:
    def __init__(self, speed, position):
        self.speed = speed
        self.position = position

    def hours_to_target(self, target: int) -> int:
        return (target-self.position) / self.speed # miles / (miles/h) = h



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [Car(speed[i], position[i]) for i in range(len(position))]
        cars.sort(key=lambda x: x.position, reverse=True)

        fleets = 0
        time_to_beat = 0
        for car in cars:
            t = car.hours_to_target(target)
            if t > time_to_beat:
                fleets += 1
                time_to_beat = t

        return fleets

