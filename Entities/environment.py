from Entities.activity import *
from Agents.categorizer import *

class Environment:
    def __init__(self, elements, activities, rules, rules_params, student, categorizer):
        self.elements = elements
        self.activities = activities
        self.rules = rules
        self.rules_params = rules_params
        self.student = student
        self.done_activities = []
        self.categorizer = categorizer

    def perform_activity(self, activity):
        self.done_activities.append(activity)
        for element in activity.elements.keys():
            if self.student.categories[element] != "Not_learned":
                x = (randint(0, 100) * activity.elements[element]) / 100
                self.student.edit_element_points(element, x)
                for i in self.activities:
                    if i is activity:
                        i.elements[element] -= x
                        break
        self.categorizer.recheck_categories(self.student.elements.keys(), self)
        return estimate_time(self.student, activity, 10)

    def clone_environment(self):
        elements = copy(self.elements)
        rules = copy(self.rules)
        rules_params = copy(self.rules_params)
        student = copy(self.student)
        student.categories = dict(self.student.categories)
        student.elements = dict(self.student.elements)
        activities = []
        categorizer = Categorizer()
        for i in self.activities:
            activity = Activity(i.name, i.estimated_time)
            activity.elements = dict(i.elements)
            activities.append(activity)
        return Environment(elements, activities, rules, rules_params, student, categorizer)
