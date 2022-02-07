class Activity:
    def __init__(self, name, estimated_time):
        self.name = name
        self.elements = dict()
        self.estimated_time = estimated_time

    def add_element(self, element, points):
        if not self.elements.keys().__contains__(element):
            self.elements.__setitem__(element, points)
            return True
        return False
