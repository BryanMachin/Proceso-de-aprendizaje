from tools import *

class Categorizer:
    def check_rules(self, env, element):
        env.student.categories[element] = env.rules[env.student.categories[element]](env, element)
        # esto significa: la nueva categoria de este elemento para el estudiante
        # va a ser el resultado de evaluar la regla de la categoria actual del elemento

    def recheck_categories(self, elements, env):
        add_attributes(elements, "visited", None)
        for element in elements:
            if element.visited is None:
                self.recheck_cat_visit(element, env)
        delete_attributes(elements, "visited")

    def recheck_cat_visit(self, v, env):
        v.visited = 1
        for u in v.dependencies:
            if u.visited is None:
                self.recheck_cat_visit(u, env)
        self.check_rules(env, v)
