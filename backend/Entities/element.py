class Element:
    dependencies = []

    def __init__(self, name):
        self.name = name

    def add_dependencies(self, *elements):
        for element in elements:
            if not self.dependencies.__contains__(element):
                self.dependencies.append(element)

    def remove_dependencies(self, *elements):
        for element in elements:
            if self.dependencies.__contains__(element):
                self.dependencies.remove(element)








