from backend.Simulation.simulation import *
from backend.tools import *


def search_good_strategy(main_env):
    strategies = build_strategies(main_env)
    strats_eval = []
    for strat in strategies:
        strats_eval.append(objective_function(strat, main_env))
    for j in range(100):
        for i in range(len(strategies)):
            v = vns(strat, main_env)
            if strats_eval[i][0] < v[1][0]:
                strats_eval[i] = v[1]
                strategies[i] = v[0]
    best_strat = -1
    bs_index = -1
    for i in range(len(strats_eval)):
        if strats_eval[i][0] > best_strat:
            bs_index = i
            best_strat = strats_eval[i][0]
    content_order = []
    for i in strats_eval[bs_index][2]:
        if i.name not in content_order:
            content_order.append(i.name)
    print("Orden de aprendizaje de contenidos:")
    for i in range(len(content_order)):
        print(i+1,"--",content_order[i])
    print("Porcentaje de objetivos aprendidos:",strats_eval[bs_index][0],"%")
    print("Tiempo transcurrido:",round(-1*strats_eval[bs_index][1],1),"h")
    return [strategies[bs_index], best_strat, content_order, strats_eval[bs_index][0], round(-1*strats_eval[bs_index][1],1)]


def build_strategies(main_env):
    strategies = []
    add_attributes(main_env.student.goals, "dep_goals", [])
    goals = topological_sort(main_env.elements, main_env.student.goals)
    strategies.append(goals)
    for i in range(3):
        strategies.append(other_topological_sort(goals))
    return strategies


def vns(strategy, main_env):
    a = randint(0, len(strategy) - 1)
    b = randint(0, len(strategy) - 1)
    while b == a:
        b = randint(0, len(strategy) - 1)
    temp = strategy[a]
    temp2 = strategy[b]
    new_strategy = []
    for i in strategy:
        if i == temp:
            new_strategy.append(temp2)
            continue
        if i == temp2:
            new_strategy.append(temp)
            continue
        new_strategy.append(i)
    return [new_strategy, objective_function(new_strategy, main_env)]


def objective_function(strategy, main_env):
    strat_env = main_env.clone_environment()
    strat_env.student.goals = []
    ret_strategy = []
    for goal in strategy:
        strat_env.student.goals.append(goal)
        if strat_env.student.categories[goal] == "Not_learned":
            ret_strategy += fill_sub_strategy(goal, strat_env)
        else:
            ret_strategy.append(goal)
    return simulate(ret_strategy, main_env, 1)


def fill_sub_strategy(goal, strat_env):
    add_attributes(strat_env.elements, "available_points", 0)
    add_attributes(strat_env.elements, "learned_missing", 0)
    ldfss(goal, strat_env)
    strats = []
    strats.append(search_strat(goal, strat_env, "avp"))
    strats.append(search_strat(goal, strat_env, "lm"))
    strats.append(search_strat(goal, strat_env, "rnd"))
    strats_eval = []
    eval_avp = simulate(strats[0], strat_env, 3)
    eval_avp.append(2)
    eval_lm = simulate(strats[1], strat_env, 3)
    eval_lm.append(1)
    eval_rnd = simulate(strats[2], strat_env, 3)
    eval_rnd.append(0)
    strats_eval.append(eval_avp)
    strats_eval.append(eval_lm)
    strats_eval.append(eval_rnd)
    strats_eval.sort()
    delete_attributes(strat_env.elements, "available_points")
    delete_attributes(strat_env.elements, "learned_missing")
    return strats[0]


def search_strat(goal, env, strat_name):
    strat_env = env.clone_environment()
    strat = []
    if strat_name == "avp":
        avps_visit(goal, strat, strat_env, 0)
    elif strat_name == "lm":
        lm_visit(goal, strat, strat_env, 0)
    else:
        rnd_visit(goal, strat, strat_env, 0)
    return strat


def avps_visit(v, stack, env, behind_count):
    if env.student.categories[v] == "Learnable":
        return stack.insert(0, v)
    deps_needed = math.ceil(len(v.dependencies) * env.rules_params[0]) - learned_deps(v, env)
    maxs = []
    for dep in v.dependencies:
        if len(maxs) < deps_needed:
            maxs.append(dep)
            continue
        maxs.sort(key=lambda x: x.available_points)
        if dep.available_points > maxs[0].available_points:
            maxs.pop(0)
            maxs.append(dep)
    for dep in maxs:
        avps_visit(dep, stack, env, len(stack))
    return stack.insert(len(stack) - behind_count, v)


def lm_visit(v, stack, env, behind_count):
    if env.student.categories[v] == "Learnable":
        return stack.insert(0, v)
    deps_needed = math.ceil(len(v.dependencies) * env.rules_params[0]) - learned_deps(v, env)
    mins = []
    for dep in v.dependencies:
        if len(mins) < deps_needed:
            mins.append(dep)
            continue
        mins.sort(key=lambda x: x.learned_missing, reverse=True)
        if dep.learned_missing < mins[0].learned_missing:
            mins.pop(0)
            mins.append(dep)
    for dep in mins:
        lm_visit(dep, stack, env, behind_count)
    return stack.insert(len(stack) - behind_count, v)


def rnd_visit(v, stack, env, behind_count):
    if env.student.categories[v] == "Learnable":
        return stack.insert(0, v)
    deps_needed = math.ceil(len(v.dependencies) * env.rules_params[0]) - learned_deps(v, env)
    valid_indexes = []
    for j in range(len(v.dependencies)):
        if env.student.categories[v.dependencies[j]] != "Learned":
            valid_indexes.append(j)
    for i in range(deps_needed):
        r = randint(0, len(valid_indexes) - 1)
        rnd_visit(v.dependencies[valid_indexes.pop(r)], stack, env, behind_count)
    return stack.insert(len(stack) - behind_count, v)









