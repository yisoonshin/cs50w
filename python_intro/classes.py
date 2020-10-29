#!/usr/bin/env python3


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 8)
print(p.x, ',', p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = list()

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if self.open_seats() > 0:
            self.passengers.append(name)
            return True
        else:
            return False


flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f'Added {person} to flight.')
    else:
        print(f'no room for {person}.')
