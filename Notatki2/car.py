class Car:
    acceleration = 10

    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.in_motion = False
        self.speed = 0

    def drive(self):
        self.in_motion = True

    def accelerate(self):
        # self.speed = self.speed + self.acceleration
        self.speed += self.acceleration

    def stop(self):
        self.in_motion = False
        self.speed = 0


if __name__ == "__main__":
    car1 = Car("BI55755")
    car2 = Car("W3434")
    print(car1.registration_number)
    print(car1.speed)
    print(car1.in_motion)
    car1.drive()
    print(car1.in_motion)
    car1.accelerate()
    print(f"speed: {car1.speed}")
    car1.accelerate()
    print(f"speed: {car1.speed}")


    print("Car2:", car2.in_motion)
    print("Car2:", car2.speed)


    # car2 = Car("W3434")
    # car3 = Car('K34354')
    # print(car1)
