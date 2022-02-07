import sys

from Entities.element import *
from Entities.student import *
from Entities.activity import *
from tools import *
from Simulation.simulation import *
from Entities.category import *
from Entities.environment import *
from Simulation.learningStrategy import *

filosofia = Element("filosofia")
algebra = Element("algebra")
geometria = Element("geometria")
programacion = Element("programacion")
analisis = Element("analisis")
logica = Element("logica")
discreta = Element("discreta")
edo = Element("edo")
mo = Element("mo")
eda = Element("eda")

elements = [filosofia, algebra, geometria, logica, programacion, analisis, discreta, edo, mo, eda]

analisis.dependencies = [algebra, geometria]
discreta.dependencies = [algebra, logica]
eda.dependencies = [logica, programacion]
mo.dependencies = [analisis, programacion]
edo.dependencies = [analisis, programacion]
programacion.dependencies = [logica]

targets = [discreta, edo, mo]

student = Student("Edalberto")
student.goals = targets
for i in range(0, 4):
    student.set_category(elements[i], Category.Learnable)
for i in range(4, 10):
    student.set_category(elements[i], Category.Not_learned)

conferencia_filosofia = Activity("conferencia_filosofia", 1.5)
conferencia_filosofia.add_element(filosofia, 1)

conferencia_programacion = Activity("conferencia_programacion", 1.5)
conferencia_programacion.add_element(programacion, 0.5)
conferencia_programacion.add_element(logica, 0.1)

conferencia_geometria = Activity("conferencia_geometria", 1.5)
conferencia_geometria.add_element(geometria, 0.3)
conferencia_geometria.add_element(algebra, 8)

conferencia_eda = Activity("conferencia_eda", 1.5)
conferencia_eda.add_element(eda, 0.2)
conferencia_eda.add_element(programacion, 0.2)

clase_practica_eda = Activity("clase_practica_eda", 2.5)
clase_practica_eda.add_element(eda, 0.5)
clase_practica_eda.add_element(programacion, 0.1)

conferencia_mo = Activity("conferencia_mo", 1)
conferencia_mo.add_element(mo, 0.2)
conferencia_mo.add_element(analisis, 0.05)

proyecto_mo = Activity("proyecto_mo", 1.5)
proyecto_mo.add_element(mo, 0.32)

conferencia_edo = Activity("conferencia_edo", 1.5)
conferencia_edo.add_element(edo, 0.1)
conferencia_edo.add_element(analisis, 0.15)

clase_practica_edo = Activity("clase_practica_edo", 2)
clase_practica_edo.add_element(edo, 0.17)
clase_practica_edo.add_element(analisis, 0.2)

conferencia_discreta = Activity("conferencia_discreta", 2)
conferencia_discreta.add_element(discreta, 0.35)
conferencia_discreta.add_element(filosofia, 0.15)

clase_practica_discreta = Activity("clase_practica_discreta", 2.85)
conferencia_discreta.add_element(discreta, 0.6)


conferencia_logica = Activity("conferencia_logica", 1)
conferencia_logica.add_element(logica, 0.35)

clase_practica_logica = Activity("clase_practica_logica", 0.45)
clase_practica_logica.add_element(logica, 0.15)

conferencia_algebra = Activity("conferencia_algebra", 1.5)
conferencia_algebra.add_element(algebra, 3)

clase_practica_algebra = Activity("clase_practica_algebra", 1)
clase_practica_algebra.add_element(algebra, 3)


activities = [conferencia_filosofia, conferencia_programacion, conferencia_geometria, conferencia_eda,
              clase_practica_eda, conferencia_mo, proyecto_mo, conferencia_edo, clase_practica_edo,
              conferencia_discreta, conferencia_logica, clase_practica_logica, conferencia_algebra,
              clase_practica_algebra]


def notlearned(env, element):
    count = 0
    for i in element.dependencies:
        if env.student.categories[i] is Category.Learned:
            count += 1
    if count >= len(element.dependencies) * env.rules_params[0]:
        return Category.Learnable
    return Category.Not_learned


def learnable(env, element):
    if env.student.elements[element] >= env.rules_params[1]:
        return Category.Learned
    return Category.Learnable


def learned(student, element):
    return Category.Learned


rules = {Category.Not_learned: notlearned, Category.Learnable: learnable, Category.Learned: learned}
rules_params = [0.5, 6]
env = Environment(elements, activities, rules, rules_params, student, Categorizer())


print(general(env))
"""
print("Activities:")
for i in a[2]:
    print(i.name)

print("Categories:")
for i in a[0].elements:
    print(i.name,":",a[0].student.categories[i])

print("Skill Points:")
for i in a[0].elements:
    print(i.name, ":", a[0].student.elements[i])
print("Goal Reached:", a[3])

print("Elapsed Time: ", a[1])
"""