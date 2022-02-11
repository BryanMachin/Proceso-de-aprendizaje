from backend.Entities.category import *


class Student:
    def __init__(self, name):
        self.name = name
        self.categories = dict()
        self.elements = dict()
        self.goals = []

    def set_category(self, element, category):
        if not self.categories.keys().__contains__(element):
            self.categories.__setitem__(element, Category.__getattribute__(Category, category))
            self.elements.__setitem__(element, 0)
            return True
        return False

    def edit_element_points(self, element, points):
        if self.elements.keys().__contains__(element):
            self.elements[element] += points
            if self.elements[element] > 10:
                self.elements[element] = 10
            return True
        return False

    def add_goal(self, element):
        self.goals.append(element)
