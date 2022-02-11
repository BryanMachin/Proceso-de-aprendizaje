from backend.Entities.category import *
from random import *
from copy import copy
import math


def add_attributes(elements, attribute, default_value):
    for element in elements:
        element.__setattr__(attribute, default_value)


def delete_attributes(elements, attribute):
    for element in elements:
        try:
            a = element.__delattr__(attribute)
        except:
            continue


def check_cycles(elements):
    add_attributes(elements, "color", None)
    for element in elements:
        if element.color is None:
            back_edge = check_cycles_visit(element)
            if back_edge is not None:
                delete_attributes(elements, "color")
                return back_edge
    delete_attributes(elements, "color")
    return None


def check_cycles_visit(v):
    v.color = "gray"
    for dependency in v.dependencies:
        if dependency.color is None:
            dependency.color = "gray"
            back_edge = check_cycles_visit(dependency)
            if back_edge is not None:
                return back_edge
        elif dependency.color == "gray":
            return [v, dependency]
    v.color = "black"
    return None



def rank(elements, goals):
    add_attributes(elements, "rank", 0)
    add_attributes(elements, "parent_goals", [])
    for i in goals:
        add_attributes(elements, "visited", None)
        rank_visit(i, 1)
        delete_attributes(elements, "visited")


def rank_visit(v, value):
    v.visited = 1
    v.rank += value
    for dependency in v.dependencies:
        if dependency.visited is None:
            rank_visit(dependency, value)


def estimate_time(student, activity, times):
    accum = 0
    for i in range(times):
        k = 0
        for element in activity.elements:
            k += student.elements[element]
        k /= len(activity.elements)
        k = k.__round__()

        if k < 5:
            k *= 0.1
            k = 0.5 - k
            k = round(activity.estimated_time * k, 1)
            accum += round(uniform(activity.estimated_time, activity.estimated_time + k), 1)
            continue
        if k > 5:
            if k < 10:
                k %= 5
                k *= 0.1
                k = round(activity.estimated_time * k, 1)
            else:
                k = round(activity.estimated_time * 0.5, 1)
                accum += round(uniform(activity.estimated_time - k, activity.estimated_time), 1)
                continue

        accum += activity.estimated_time
    return round(accum/times, 1)


def topological_sort(elements, goals):
    stack = []
    add_attributes(elements, "rank", 0)
    for goal in goals:
        add_attributes(elements, "visited", None)
        topological_sort_visit(goal, stack, goal, goals)
        delete_attributes(elements, "visited")
    delete_attributes(elements, "rank")
    return stack


def topological_sort_visit(v, stack, root, goals):
    for dependency in v.dependencies:
        if dependency.visited is None:
            topological_sort_visit(dependency, stack, root, goals)
    if v in goals:
        if v is not root:
            root.dep_goals.append(v)
        if v not in stack:
            stack.append(v)


def ldfss(goal, env):
    """Antes y despues de usarse deben agregarse y eliminarse respectivamente los atributos
    learned_missing y available points"""
    add_attributes(env.elements, "rank", 0)
    add_attributes(env.elements, "visited", None)
    visit(goal, env)
    delete_attributes(env.elements, "visited")
    delete_attributes(env.elements, "rank")


def visit(v, env):
    v.visited = 1
    for i in v.dependencies:
        if i.visited is None:
            visit(i, env)
    if env.student.categories[v] == "Learned":
        v.learned_missing = 0
    elif env.student.categories[v] == "Learnable":
        v.learned_missing = 1
        v.available_points = available_points(v, env.activities)
    else:
        v.learned_missing = lm_for_not_learned(v, env)
        v.available_points = av_for_not_learned(v, env)


def lm_for_not_learned(element, env):
    deps_needed = math.ceil(len(element.dependencies) * env.rules_params[0]) - learned_deps(element, env)
    mins = []
    for dep in element.dependencies:
        if len(mins) < deps_needed:
            mins.append(dep.learned_missing)
            continue
        mins.sort(reverse=True)
        if dep.learned_missing < mins[0]:
            mins[0] = dep.learned_missing
    return sum(mins)


def av_for_not_learned(element, env):
    deps_needed = math.ceil(len(element.dependencies) * env.rules_params[0]) - learned_deps(element, env)
    maxs = []
    for dep in element.dependencies:
        if len(maxs) < deps_needed:
            maxs.append(dep.available_points)
            continue
        maxs.sort()
        if dep.available_points > maxs[0]:
            maxs[0] = dep.available_points
    ret = 1
    for x in maxs:
        ret *= x
    return ret


def available_points(element, activities):
    a = 0
    for activity in activities:
        for e in activity.elements:
            if e is element:
                a += activity.elements[e]
    return a


def learned_deps(element, env):
    l = 0
    for dep in element.dependencies:
        if env.student.categories[dep] == "Learned":
            l += 1
    return l


def other_topological_sort(top_sort):
    no_indegree = []
    for i in top_sort:
        i.indegree = len(i.dep_goals)
        if not i.indegree:
            no_indegree.append(i)
    sort = []

    while no_indegree:
        r = randint(0, len(no_indegree) - 1)
        next = no_indegree.pop(r)
        sort.append(next)
        for i in top_sort:
            for j in i.dep_goals:
                if next.name == j:
                    i.indegree -= 1
                    if not i.indegree:
                        no_indegree.append(i)
    return sort
