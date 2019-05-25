#!/usr/bin/python3
# -*- coding: utf-8 -*-


class MarkovChain:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    # el @classmethod me permite acceder a las variables de la clase
    # With classmethods, the class of the object instance is implicitly passed as the first argument instead of self.
    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))

    # With staticmethods, neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument.
    # They behave like plain functions except that you can call them from an instance or the class:
    @staticmethod
    def say_hello():
        print("I robot I'm great")
