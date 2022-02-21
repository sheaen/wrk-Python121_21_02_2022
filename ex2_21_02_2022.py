class Human:
    def __init__(self, age, gender, height):
        self.age = str(age)
        self.gender = str(gender)
        self.height = str(height)
        
# class Builder(Human):
#     def __init__(self, age, gender, height, favorite_tools, specialization):
#         super(Builder, self).__init__( age, gender, height)
#         self.favorite_tools = str(favorite_tools)
#         self.specialization = str(specialization)
class Builder(Human):
    def __init__(self, age, gender, height):
        super(Builder, self).__init__( age, gender, height)
        self.favorite_tools = ''


# class Sailor(Human):
#     def __init__(self, age, gender, height, ship, how_long, when_swam):
#         super(Sailor, self).__init__( age, gender, height)
#         self.ship = str(ship)
#         self.how_long = str(how_long)
#         self.when_swam = str(when_swam)
class Sailor(Human):
    def __init__(self, age, gender, height):
        super(Sailor, self).__init__( age, gender, height)
        self.ship = 'Корабль не указан'

# class Pilot(Human):
#     def __init__(self, age, gender, height, plane, type, num_departures):
#         super(Pilot, self).__init__( age, gender, height)
#         self.plane = str(plane)
#         self.type = str(type)
#         self.num_departurers = str(num_departures)
class Pilot(Human):
    def __init__(self, age, gender, height, airship_type,airship):
        super(Pilot, self).__init__( age, gender, height)
        self.airship_type = str(airship_type)
        self.airship = str(airship)


if __name__ == '__main__':
    person1 = Human(27, 'male', 1.74)

    person2_b = Builder(45,'male', 1.89)
    person2_b.favorite_tools = 'Шпатель'

    person3_s = Sailor(56,'female', 1.70)
    person3_s.ship = 'Линкор'

    person4_p = Pilot(23,'female', 1.66, 'Вертолёт', 'Красный')

    print(isinstance(person1,Builder)) #False
    print(isinstance(person2_b, Sailor)) #False
    print(isinstance(person2_b, Human)) #True

# if __name__ == '__main__':
#     hum = Human(21, 'male', 190)
#     build = Builder(27, 'male', 185, 'hammer', 'house')
#     sail = Sailor(34, 'female', 165, 'battleship', 1000, 'January')
#     avi = Pilot(29, 'male', 183, 'boeng', 'CommercialPilot', 100)
#
#     print(isinstance(hum, Human))
#     print(isinstance(build, Builder))
#     print(isinstance(hum, Builder))
#     print(isinstance(sail, Pilot))
#     print(isinstance(hum, Pilot))
#     print(isinstance(avi, Human))





