from tools import estimate_time
from Agents.adviser import *


def simulate(sub_strategy, main_env, times):
    tracks = []
    for i in range(times):
        tracks.append(reps(sub_strategy, main_env, Adviser()))
    learning_percent = 0
    time = 0
    for i in range(times):
        learning_percent += tracks[i][0]
        time += tracks[i][1]

    return [learning_percent/times, -(time/times)]


def reps(strategy, main_env, adviser):
    env = main_env.clone_environment()
    time = 0
    rep_checker = -1
    while strategy:
        rep_checker += 1
        next_content = strategy[0]
        if adviser.stop(rep_checker):
            break

        if env.student.categories[next_content] == "Learned":
            strategy.pop(0)
            continue
        if env.student.categories[next_content] == "Not_learned":
            break
        activities = []
        for activity in env.activities:
            if next_content in activity.elements:
                activities.append(activity)
        if not activities:
            break
        front = make_front(activities, next_content, env.student)
        r = randint(0, len(front) - 1)
        time += env.perform_activity(front[r])
    p = 0
    for goal in env.student.goals:
        if env.student.categories[goal] == "Learned":
            p += 1
    t = len(main_env.student.goals)
    return [100 * p / t, time, env]


def make_front(activities, element, student):
    front = []
    comparable = False
    for activity in activities:
        for front_activity in front:
            comp = compare_activities(activity, front_activity, element, student)
            if comp == "better":
                comparable = True
                front.remove(front_activity)
                front.append(activity)
                break
            elif not comp == "not_comparable":
                comparable = True
                break
        if not comparable:
            front.append(activity)
    return front


def compare_activities(a, b, element, student):
    ret = ""
    a_estimated_time = estimate_time(student, a, 10)
    b_estimated_time = estimate_time(student, b, 10)
    if a_estimated_time > b_estimated_time and a.elements[element] > b.elements[element]:
        ret = "not_comparable"
    if a_estimated_time < b_estimated_time:
        if a.elements[element] >= b.elements[element]:
            ret = "better"
        ret = "not_comparable"
    if a.elements[element] > b.elements[element]:
        ret = "better"
    return ret
