import sys

from backend.Entities.element import *
from backend.Entities.student import *
from backend.Entities.activity import *
from backend.tools import *
from backend.Simulation.simulation import *
from backend.Entities.category import *
from backend.Entities.environment import *
from backend.Simulation.learningStrategy import *

tipos_basicos = Element("tipos_basicos")
operadores = Element("operadores")
colecciones = Element("colecciones")
metodos_de_lista = Element("metodos_de_lista")
metodos_de_diccionario = Element("metodos_de_diccionario")
comprension_de_lista = Element("comprension_de_lista")
condicionales = Element("condicionales")
ciclos = Element("ciclos")
metodos_de_cadena = Element("metodos_de_cadena")
funciones = Element("funciones")
decoradores = Element("decoradores")
funciones_lambda = Element("funciones_lambda")
generadores = Element("generadores")
objetos = Element("objetos")
herencia = Element("herencia")
herencia_multiple = Element("herencia_multiple")
clases_decoradoras = Element("clases_decoradoras")


elements = [tipos_basicos, operadores, colecciones, metodos_de_lista, metodos_de_cadena, metodos_de_diccionario,
            comprension_de_lista, condicionales, ciclos, funciones, funciones_lambda, generadores, decoradores,
            objetos, herencia, herencia_multiple, clases_decoradoras]


funciones.dependencies = [tipos_basicos]
operadores.dependencies = [tipos_basicos]
condicionales.dependencies = [tipos_basicos]
colecciones.dependencies = [tipos_basicos]
metodos_de_lista.dependencies = [colecciones]
metodos_de_diccionario.dependencies = [colecciones]
comprension_de_lista.dependencies = [colecciones]
metodos_de_cadena.dependencies = [operadores]
decoradores.dependencies = [funciones]
funciones_lambda.dependencies = [funciones]
generadores.dependencies = [funciones]
objetos.dependencies = [funciones]
herencia.dependencies = [objetos]
herencia_multiple.dependencies = [herencia]
ciclos.dependencies = [condicionales]
clases_decoradoras.dependencies = [objetos, decoradores]

targets = [ciclos, clases_decoradoras, herencia_multiple, comprension_de_lista]

student = Student("Edalberto")
student.goals = targets

student.set_category(elements[0], Category.Learnable)
for i in range(1, 17):
    student.set_category(elements[i], Category.Not_learned)

#tipos basicos 1
video_tutorial_tipos_basicos = Activity("video_tutorial_tipos_basicos", 0.5)
video_tutorial_tipos_basicos.add_element(tipos_basicos, 2)

documento_conferencia_tipos_basicos = Activity("documento_conferencia_tipos_basicos", 1)
documento_conferencia_tipos_basicos.add_element(tipos_basicos, 3)

ejercicios_practicos_tipos_basicos = Activity("ejercicios_practicos_tipos_basicos", 2)
ejercicios_practicos_tipos_basicos.add_element(tipos_basicos, 3)

#operadores 2
video_tutorial_operadores = Activity("video_tutorial_operadores", 0.5)
video_tutorial_operadores.add_element(operadores, 2)

documento_conferencia_operadores = Activity("documento_conferencia_operadores", 1)
documento_conferencia_operadores.add_element(operadores, 3)

ejercicios_practicos_operadores = Activity("ejercicios_practicos_operadores", 2)
ejercicios_practicos_operadores.add_element(operadores, 3)

#colecciones 3
video_tutorial_colecciones = Activity("video_tutorial_colecciones", 0.5)
video_tutorial_colecciones.add_element(colecciones, 2)

documento_conferencia_colecciones = Activity("documento_conferencia_colecciones", 1)
documento_conferencia_colecciones.add_element(colecciones, 3)

ejercicios_practicos_colecciones = Activity("ejercicios_practicos_colecciones", 2)
ejercicios_practicos_colecciones.add_element(colecciones, 3)

#metodos de lista 4
video_tutorial_metodos_de_lista = Activity("video_tutorial_metodos_de_lista", 0.5)
video_tutorial_metodos_de_lista.add_element(metodos_de_lista, 2)

documento_conferencia_metodos_de_lista = Activity("documento_conferencia_metodos_de_lista", 1)
documento_conferencia_metodos_de_lista.add_element(metodos_de_lista, 3)

ejercicios_practicos_metodos_de_lista = Activity("ejercicios_practicos_metodos_de_lista", 2)
ejercicios_practicos_metodos_de_lista.add_element(metodos_de_lista, 3)

#metodos de diccionario 5
video_tutorial_metodos_de_diccionario = Activity("video_tutorial_metodos_de_diccionario", 0.5)
video_tutorial_metodos_de_diccionario.add_element(metodos_de_diccionario, 2)

documento_conferencia_metodos_de_diccionario = Activity("documento_conferencia_metodos_de_diccionario", 1)
documento_conferencia_metodos_de_diccionario.add_element(metodos_de_diccionario, 3)

ejercicios_practicos_metodos_de_diccionario = Activity("ejercicios_practicos_metodos_de_diccionario", 2)
ejercicios_practicos_metodos_de_diccionario.add_element(metodos_de_diccionario, 3)

#comprension de lista 6
video_tutorial_comprension_de_lista = Activity("video_tutorial_comprension_de_lista", 0.5)
video_tutorial_comprension_de_lista.add_element(comprension_de_lista, 2)

documento_conferencia_comprension_de_lista = Activity("documento_conferencia_comprension_de_lista", 1)
documento_conferencia_comprension_de_lista.add_element(comprension_de_lista, 3)

ejercicios_practicos_comprension_de_lista = Activity("ejercicios_practicos_comprension_de_lista", 2)
ejercicios_practicos_comprension_de_lista.add_element(comprension_de_lista, 3)

#condicionales 7
video_tutorial_condicionales = Activity("video_tutorial_condicionales", 0.5)
video_tutorial_condicionales.add_element(condicionales, 2)

documento_conferencia_condicionales = Activity("documento_conferencia_condicionales", 1)
documento_conferencia_condicionales.add_element(condicionales, 3)

ejercicios_practicos_condicionales = Activity("ejercicios_practicos_condicionales", 2)
ejercicios_practicos_condicionales.add_element(condicionales, 3)

#ciclos 8
video_tutorial_ciclos = Activity("video_tutorial_ciclos", 0.5)
video_tutorial_ciclos.add_element(ciclos, 2)

documento_conferencia_ciclos = Activity("documento_conferencia_ciclos", 1)
documento_conferencia_ciclos.add_element(ciclos, 3)

ejercicios_practicos_ciclos = Activity("ejercicios_practicos_ciclos", 2)
ejercicios_practicos_ciclos.add_element(ciclos, 3)

#metodos de cadena 9
video_tutorial_metodos_de_cadena = Activity("video_tutorial_metodos_de_cadena", 0.5)
video_tutorial_metodos_de_cadena.add_element(metodos_de_cadena, 2)

documento_conferencia_metodos_de_cadena = Activity("documento_conferencia_metodos_de_cadena", 1)
documento_conferencia_metodos_de_cadena.add_element(metodos_de_cadena, 3)

ejercicios_practicos_metodos_de_cadena = Activity("ejercicios_practicos_metodos_de_cadena", 2)
ejercicios_practicos_metodos_de_cadena.add_element(metodos_de_cadena, 3)

#funciones 10
video_tutorial_funciones = Activity("video_tutorial_funciones", 0.5)
video_tutorial_funciones.add_element(funciones, 2)

documento_conferencia_funciones = Activity("documento_conferencia_funciones", 1)
documento_conferencia_funciones.add_element(funciones, 3)

ejercicios_practicos_funciones = Activity("ejercicios_practicos_funciones", 2)
ejercicios_practicos_funciones.add_element(funciones, 3)

#decoradores 11
video_tutorial_decoradores = Activity("video_tutorial_decoradores", 0.5)
video_tutorial_decoradores.add_element(decoradores, 2)

documento_conferencia_decoradores = Activity("documento_conferencia_decoradores", 1)
documento_conferencia_decoradores.add_element(decoradores, 3)

ejercicios_practicos_decoradores = Activity("ejercicios_practicos_decoradores", 2)
ejercicios_practicos_decoradores.add_element(decoradores, 3)

#funciones_lambda 12
video_tutorial_funciones_lambda = Activity("video_tutorial_funciones_lambda", 0.5)
video_tutorial_funciones_lambda.add_element(funciones_lambda, 2)

documento_conferencia_funciones_lambda = Activity("documento_conferencia_funciones_lambda", 1)
documento_conferencia_funciones_lambda.add_element(funciones_lambda, 3)

ejercicios_practicos_funciones_lambda = Activity("ejercicios_practicos_funciones_lambda", 2)
ejercicios_practicos_funciones_lambda.add_element(funciones_lambda, 3)

#generadores 13
video_tutorial_generadores = Activity("video_tutorial_generadores", 0.5)
video_tutorial_generadores.add_element(generadores, 2)

documento_conferencia_generadores = Activity("documento_conferencia_generadores", 1)
documento_conferencia_generadores.add_element(generadores, 3)

ejercicios_practicos_generadores = Activity("ejercicios_practicos_generadores", 2)
ejercicios_practicos_generadores.add_element(generadores, 3)

#clases_decoradoras 14
video_tutorial_clases_decoradoras = Activity("video_tutorial_clases_decoradoras", 0.5)
video_tutorial_clases_decoradoras.add_element(clases_decoradoras, 2)

documento_conferencia_clases_decoradoras = Activity("documento_conferencia_clases_decoradoras", 1)
documento_conferencia_clases_decoradoras.add_element(clases_decoradoras, 3)

ejercicios_practicos_clases_decoradoras = Activity("ejercicios_practicos_clases_decoradoras", 2)
ejercicios_practicos_clases_decoradoras.add_element(clases_decoradoras, 3)

#clases_decoradoras 14
video_tutorial_clases_decoradoras = Activity("video_tutorial_clases_decoradoras", 0.5)
video_tutorial_clases_decoradoras.add_element(clases_decoradoras, 2)

documento_conferencia_clases_decoradoras = Activity("documento_conferencia_clases_decoradoras", 1)
documento_conferencia_clases_decoradoras.add_element(clases_decoradoras, 3)

ejercicios_practicos_clases_decoradoras = Activity("ejercicios_practicos_clases_decoradoras", 2)
ejercicios_practicos_clases_decoradoras.add_element(clases_decoradoras, 3)


#objetos 15
video_tutorial_objetos = Activity("video_tutorial_objetos", 0.5)
video_tutorial_objetos.add_element(objetos, 2)

documento_conferencia_objetos = Activity("documento_conferencia_objetos", 1)
documento_conferencia_objetos.add_element(objetos, 3)

ejercicios_practicos_objetos = Activity("ejercicios_practicos_objetos", 2)
ejercicios_practicos_objetos.add_element(objetos, 3)

#herencia 16
video_tutorial_herencia = Activity("video_tutorial_herencia", 0.5)
video_tutorial_herencia.add_element(herencia, 2)

documento_conferencia_herencia = Activity("documento_conferencia_herencia", 1)
documento_conferencia_herencia.add_element(herencia, 3)

ejercicios_practicos_herencia = Activity("ejercicios_practicos_herencia", 2)
ejercicios_practicos_herencia.add_element(herencia, 3)

#herencia_multiple 17
video_tutorial_herencia_multiple = Activity("video_tutorial_herencia_multiple", 0.5)
video_tutorial_herencia_multiple.add_element(herencia_multiple, 2)

documento_conferencia_herencia_multiple = Activity("documento_conferencia_herencia_multiple", 1)
documento_conferencia_herencia_multiple.add_element(herencia_multiple, 3)

ejercicios_practicos_herencia_multiple = Activity("ejercicios_practicos_herencia_multiple", 2)
ejercicios_practicos_herencia_multiple.add_element(herencia_multiple, 3)

activities = [video_tutorial_clases_decoradoras, video_tutorial_objetos, video_tutorial_herencia,
              video_tutorial_decoradores, video_tutorial_funciones, video_tutorial_operadores,
              video_tutorial_funciones_lambda, video_tutorial_metodos_de_cadena, video_tutorial_ciclos,
              video_tutorial_condicionales, video_tutorial_comprension_de_lista, video_tutorial_metodos_de_diccionario,
              video_tutorial_metodos_de_lista, video_tutorial_herencia_multiple, video_tutorial_tipos_basicos,
              video_tutorial_generadores, video_tutorial_colecciones,
              documento_conferencia_clases_decoradoras, documento_conferencia_objetos, documento_conferencia_herencia,
              documento_conferencia_decoradores, documento_conferencia_funciones, documento_conferencia_operadores,
              documento_conferencia_funciones_lambda, documento_conferencia_metodos_de_cadena, documento_conferencia_ciclos,
              documento_conferencia_condicionales, documento_conferencia_comprension_de_lista, documento_conferencia_metodos_de_diccionario,
              documento_conferencia_metodos_de_lista, documento_conferencia_herencia_multiple, documento_conferencia_tipos_basicos,
              documento_conferencia_generadores, documento_conferencia_colecciones,
              ejercicios_practicos_clases_decoradoras, ejercicios_practicos_objetos, ejercicios_practicos_herencia,
              ejercicios_practicos_decoradores, ejercicios_practicos_funciones, ejercicios_practicos_operadores,
              ejercicios_practicos_funciones_lambda, ejercicios_practicos_metodos_de_cadena,ejercicios_practicos_ciclos,
              ejercicios_practicos_condicionales, ejercicios_practicos_comprension_de_lista, ejercicios_practicos_metodos_de_diccionario,
              ejercicios_practicos_metodos_de_lista, ejercicios_practicos_herencia_multiple, ejercicios_practicos_tipos_basicos,
              ejercicios_practicos_generadores, ejercicios_practicos_colecciones]


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

results = search_good_strategy(env)
print(results)
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